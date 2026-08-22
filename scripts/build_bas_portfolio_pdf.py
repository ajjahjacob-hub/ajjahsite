"""Build Anna Maria Kotua's Otago Polytechnic BAS application portfolio PDF."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageOps
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Anna-Maria-Kotua-Otago-Polytechnic-BAS-Portfolio.pdf"
CACHE = ROOT / "tmp" / "pdfs" / "bas-portfolio-assets"

PAGE_W, PAGE_H = landscape(A4)
MARGIN = 36

NAVY = HexColor("#142936")
NAVY_2 = HexColor("#1d3b4b")
TEAL = HexColor("#2d7d78")
TEAL_LIGHT = HexColor("#dceceb")
GOLD = HexColor("#d2a34a")
INK = HexColor("#18242c")
MUTED = HexColor("#5e6b72")
PALE = HexColor("#f2f5f4")
WHITE = HexColor("#ffffff")
LINE = HexColor("#d8dfdf")

FONT_REGULAR = "PortfolioArial"
FONT_BOLD = "PortfolioArialBold"
FONT_ITALIC = "PortfolioArialItalic"


def register_fonts() -> None:
    font_dir = Path("C:/Windows/Fonts")
    pdfmetrics.registerFont(TTFont(FONT_REGULAR, str(font_dir / "arial.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_BOLD, str(font_dir / "arialbd.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_ITALIC, str(font_dir / "ariali.ttf")))


def clean_image(relative_path: str) -> Path:
    """Return a web-safe, EXIF-free JPEG copy for embedding in the PDF."""
    source = ROOT / relative_path
    if not source.exists():
        raise FileNotFoundError(source)
    CACHE.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha1(str(source).encode("utf-8")).hexdigest()[:10]
    target = CACHE / f"{source.stem}-{digest}.jpg"
    if target.exists() and target.stat().st_mtime >= source.stat().st_mtime:
        return target
    with Image.open(source) as opened:
        image = ImageOps.exif_transpose(opened)
        if image.mode in {"RGBA", "LA"}:
            background = Image.new("RGB", image.size, "white")
            background.paste(image, mask=image.getchannel("A"))
            image = background
        else:
            image = image.convert("RGB")
        image.thumbnail((2600, 2600), Image.Resampling.LANCZOS)
        image.save(target, "JPEG", quality=90, optimize=True, progressive=True)
    return target


def wrap_lines(text: str, font: str, size: float, max_width: float) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        line = words[0]
        for word in words[1:]:
            trial = f"{line} {word}"
            if pdfmetrics.stringWidth(trial, font, size) <= max_width:
                line = trial
            else:
                lines.append(line)
                line = word
        lines.append(line)
    return lines


def draw_text(
    pdf: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    max_width: float,
    *,
    font: str = FONT_REGULAR,
    size: float = 10,
    leading: float | None = None,
    color=INK,
    max_lines: int | None = None,
) -> float:
    leading = leading or size * 1.35
    lines = wrap_lines(text, font, size, max_width)
    if max_lines is not None:
        lines = lines[:max_lines]
    pdf.setFillColor(color)
    pdf.setFont(font, size)
    for line in lines:
        pdf.drawString(x, y, line)
        y -= leading
    return y


def draw_image(
    pdf: canvas.Canvas,
    relative_path: str,
    x: float,
    y: float,
    width: float,
    height: float,
    *,
    background=WHITE,
) -> None:
    image_path = clean_image(relative_path)
    with Image.open(image_path) as image:
        image_w, image_h = image.size
    scale = min(width / image_w, height / image_h)
    draw_w = image_w * scale
    draw_h = image_h * scale
    draw_x = x + (width - draw_w) / 2
    draw_y = y + (height - draw_h) / 2
    pdf.setFillColor(background)
    pdf.roundRect(x, y, width, height, 5, fill=1, stroke=0)
    pdf.drawImage(
        ImageReader(str(image_path)),
        draw_x,
        draw_y,
        draw_w,
        draw_h,
        preserveAspectRatio=True,
        mask="auto",
    )


def draw_labeled_image(
    pdf: canvas.Canvas,
    relative_path: str,
    caption: str,
    x: float,
    y: float,
    width: float,
    height: float,
) -> None:
    caption_h = 20
    pdf.setStrokeColor(LINE)
    pdf.setLineWidth(0.7)
    pdf.roundRect(x, y, width, height, 6, fill=0, stroke=1)
    draw_image(pdf, relative_path, x + 1, y + caption_h, width - 2, height - caption_h - 1)
    draw_text(
        pdf,
        caption,
        x + 8,
        y + 6,
        width - 16,
        font=FONT_REGULAR,
        size=7.5,
        leading=8.5,
        color=MUTED,
        max_lines=1,
    )


def draw_footer(pdf: canvas.Canvas, page_number: int) -> None:
    pdf.setStrokeColor(LINE)
    pdf.setLineWidth(0.6)
    pdf.line(MARGIN, 28, PAGE_W - MARGIN, 28)
    pdf.setFont(FONT_REGULAR, 7.5)
    pdf.setFillColor(MUTED)
    pdf.drawString(MARGIN, 16, "ANNA MARIA KOTUA  |  OTAGO POLYTECHNIC BAS APPLICATION PORTFOLIO")
    pdf.drawRightString(PAGE_W - MARGIN, 16, f"{page_number:02d}")


def draw_tag(pdf: canvas.Canvas, text: str, x: float, y: float) -> float:
    width = tag_width(text)
    pdf.setFillColor(TEAL_LIGHT)
    pdf.roundRect(x, y - 3, width, 16, 8, fill=1, stroke=0)
    pdf.setFillColor(NAVY)
    pdf.setFont(FONT_BOLD, 6.7)
    pdf.drawString(x + 8.5, y + 1.4, text.upper())
    return x + width + 5


def tag_width(text: str) -> float:
    return pdfmetrics.stringWidth(text.upper(), FONT_BOLD, 6.7) + 17


def draw_cover(pdf: canvas.Canvas) -> None:
    pdf.setFillColor(NAVY)
    pdf.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    pdf.setFillColor(NAVY_2)
    pdf.circle(PAGE_W - 30, PAGE_H + 35, 215, fill=1, stroke=0)
    pdf.setFillColor(TEAL)
    pdf.rect(0, 0, 12, PAGE_H, fill=1, stroke=0)

    image_x, image_y, image_w, image_h = 365, 78, 432, 406
    pdf.setFillColor(WHITE)
    pdf.roundRect(image_x - 9, image_y - 9, image_w + 18, image_h + 18, 10, fill=1, stroke=0)
    draw_image(pdf, "images/Co Housing 2.png", image_x, image_y, image_w, image_h, background=PALE)

    pdf.setFillColor(GOLD)
    pdf.setFont(FONT_BOLD, 9)
    pdf.drawString(48, 526, "OTAGO POLYTECHNIC APPLICATION")
    y = 474
    y = draw_text(pdf, "Bachelor of\nArchitectural Studies", 48, y, 285, font=FONT_BOLD, size=29, leading=34, color=WHITE)
    y -= 8
    draw_text(pdf, "PORTFOLIO", 48, y, 285, font=FONT_BOLD, size=15, leading=18, color=GOLD)
    pdf.setStrokeColor(TEAL)
    pdf.setLineWidth(3)
    pdf.line(48, 346, 176, 346)
    draw_text(pdf, "Anna Maria Kotua", 48, 319, 285, font=FONT_BOLD, size=18, color=WHITE)
    draw_text(pdf, "12 selected works", 48, 286, 285, font=FONT_REGULAR, size=11, color=HexColor("#cbd8dc"))
    draw_text(
        pdf,
        "Architectural drawing, collaborative design, model-making, construction, adaptive reuse and creative material practice.",
        48,
        248,
        265,
        font=FONT_REGULAR,
        size=11,
        leading=16,
        color=HexColor("#e9f0f2"),
    )
    pdf.setFillColor(TEAL)
    pdf.roundRect(48, 74, 250, 67, 8, fill=1, stroke=0)
    pdf.setFillColor(WHITE)
    pdf.setFont(FONT_BOLD, 10)
    pdf.drawString(64, 115, "HIGHLIGHTS")
    pdf.setFont(FONT_REGULAR, 8.5)
    pdf.drawString(64, 96, "99% co-housing team result  |  ADNZ award")
    pdf.drawString(64, 82, "Consented built work  |  Gallery leadership")
    pdf.setFont(FONT_REGULAR, 7.5)
    pdf.setFillColor(HexColor("#cbd8dc"))


def draw_criteria_box(pdf: canvas.Canvas, number: str, title: str, detail: str, x: float, y: float) -> None:
    width, height = 192, 83
    pdf.setFillColor(PALE)
    pdf.roundRect(x, y, width, height, 7, fill=1, stroke=0)
    pdf.setFillColor(TEAL)
    pdf.setFont(FONT_BOLD, 8)
    pdf.drawString(x + 12, y + height - 19, number)
    pdf.setFillColor(INK)
    pdf.setFont(FONT_BOLD, 10.5)
    pdf.drawString(x + 39, y + height - 19, title)
    draw_text(pdf, detail, x + 12, y + height - 39, width - 24, size=8, leading=10.5, color=MUTED, max_lines=3)


def draw_context_page(pdf: canvas.Canvas, page_number: int) -> None:
    pdf.setFillColor(WHITE)
    pdf.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    pdf.setFillColor(TEAL)
    pdf.rect(0, PAGE_H - 12, PAGE_W, 12, fill=1, stroke=0)

    pdf.setFillColor(GOLD)
    pdf.setFont(FONT_BOLD, 8)
    pdf.drawString(MARGIN, PAGE_H - 43, "SELECTION FRAMEWORK")
    draw_text(pdf, "Criteria and practice context", MARGIN, PAGE_H - 69, 315, font=FONT_BOLD, size=24, leading=28, color=NAVY)
    draw_text(
        pdf,
        "The 12 assessed works are selected around Otago Polytechnic's published portfolio criteria. Team and collaborative contributions are identified, and evidence is available for the academic result, award and consented projects.",
        MARGIN,
        PAGE_H - 116,
        338,
        size=9.3,
        leading=13.2,
        color=MUTED,
    )
    draw_criteria_box(pdf, "01", "Composition", "Hierarchy, balance, proportion and spatial organisation.", 406, PAGE_H - 128)
    draw_criteria_box(pdf, "02", "Concepts", "Ideas, purpose, context and development of content.", 607, PAGE_H - 128)
    draw_criteria_box(pdf, "03", "Range of media", "Two- and three-dimensional, digital, built and material work.", 406, PAGE_H - 220)
    draw_criteria_box(pdf, "04", "Drawing skills", "Freehand perspective, design development and technical communication.", 607, PAGE_H - 220)

    y = 327
    pdf.setFillColor(NAVY)
    pdf.setFont(FONT_BOLD, 13)
    pdf.drawString(MARGIN, y, "Gallery practice, exhibitions and creative mentoring")
    draw_text(
        pdf,
        "Supporting work and life-experience context - not counted among the 12 selected works. A suicide-prevention initiative began in 2019 while Anna Maria worked for New Zealand Police. In 2021 it became a community initiative alongside the establishment of a local gallery, combining spatial curation, enterprise, public presentation, tutorials and people-centred leadership.",
        MARGIN,
        y - 20,
        PAGE_W - 2 * MARGIN,
        size=8.7,
        leading=11.3,
        color=MUTED,
        max_lines=3,
    )
    draw_text(
        pdf,
        "Application package: online form + cover letter + CV + this PDF. Any required no-NCEA-Design-or-Art mini-assignment will be submitted separately.",
        MARGIN,
        273,
        PAGE_W - 2 * MARGIN,
        font=FONT_BOLD,
        size=8,
        leading=10,
        color=TEAL,
        max_lines=2,
    )
    image_y, image_h, gap = 59, 190, 10
    image_w = (PAGE_W - 2 * MARGIN - 2 * gap) / 3
    gallery_images = [
        ("images/ART GALLERY stairs 1.jpg", "Curated arrival sequence"),
        ("images/ART GALLERY room 3.jpg", "Connected gallery rooms"),
        ("images/KAKA POINT EXHB OCT 2021.jpg", "Shared exhibition, 2021"),
    ]
    for index, (path, caption) in enumerate(gallery_images):
        draw_labeled_image(pdf, path, caption, MARGIN + index * (image_w + gap), image_y, image_w, image_h)
    draw_footer(pdf, page_number)


def draw_image_layout(
    pdf: canvas.Canvas,
    images: list[str],
    captions: list[str],
    layout: str,
    x: float = 36,
    y: float = 55,
    width: float = 518,
    height: float = 475,
) -> None:
    gap = 9
    if len(images) == 1:
        draw_labeled_image(pdf, images[0], captions[0], x, y, width, height)
        return
    if layout == "main-detail" and len(images) == 2:
        main_w = width * 0.65
        draw_labeled_image(pdf, images[0], captions[0], x, y, main_w, height)
        draw_labeled_image(pdf, images[1], captions[1], x + main_w + gap, y, width - main_w - gap, height)
        return
    if len(images) == 2:
        item_w = (width - gap) / 2
        for index in range(2):
            draw_labeled_image(pdf, images[index], captions[index], x + index * (item_w + gap), y, item_w, height)
        return
    hero_h = 287
    draw_labeled_image(pdf, images[0], captions[0], x, y + height - hero_h, width, hero_h)
    bottom_h = height - hero_h - gap
    item_w = (width - gap) / 2
    for index in range(2):
        draw_labeled_image(pdf, images[index + 1], captions[index + 1], x + index * (item_w + gap), y, item_w, bottom_h)


def draw_work_page(
    pdf: canvas.Canvas,
    page_number: int,
    number: str,
    category: str,
    title: str,
    metadata: str,
    description: str,
    role: str,
    criteria: Iterable[str],
    images: list[str],
    captions: list[str],
    *,
    evidence: str | None = None,
    layout: str = "default",
) -> None:
    pdf.setFillColor(PALE)
    pdf.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    pdf.setFillColor(TEAL)
    pdf.rect(0, PAGE_H - 12, PAGE_W, 12, fill=1, stroke=0)
    draw_image_layout(pdf, images, captions, layout)

    panel_x = 578
    panel_w = PAGE_W - panel_x - MARGIN
    pdf.setFillColor(WHITE)
    pdf.roundRect(panel_x - 12, 55, panel_w + 12, 475, 8, fill=1, stroke=0)
    pdf.setFillColor(GOLD)
    pdf.setFont(FONT_BOLD, 8)
    pdf.drawString(panel_x, 508, category.upper())
    pdf.setFillColor(TEAL)
    pdf.setFont(FONT_BOLD, 28)
    pdf.drawRightString(PAGE_W - MARGIN, 510, number)

    y = 478
    y = draw_text(pdf, title, panel_x, y, panel_w, font=FONT_BOLD, size=19.5, leading=23, color=NAVY)
    y -= 7
    y = draw_text(pdf, metadata, panel_x, y, panel_w, font=FONT_BOLD, size=8, leading=10.5, color=TEAL)
    pdf.setStrokeColor(LINE)
    pdf.line(panel_x, y - 4, PAGE_W - MARGIN, y - 4)
    y -= 22
    pdf.setFillColor(NAVY)
    pdf.setFont(FONT_BOLD, 8)
    pdf.drawString(panel_x, y, "WHY SELECTED")
    y -= 17
    y = draw_text(pdf, description, panel_x, y, panel_w, size=9, leading=12.3, color=INK)
    y -= 12
    pdf.setFillColor(NAVY)
    pdf.setFont(FONT_BOLD, 8)
    pdf.drawString(panel_x, y, "ROLE / CONTEXT")
    y -= 17
    y = draw_text(pdf, role, panel_x, y, panel_w, size=9, leading=12.3, color=INK)
    if evidence:
        y -= 12
        evidence_lines = wrap_lines(evidence, FONT_REGULAR, 8.2, panel_w - 20)
        box_h = max(42, 17 + 10.5 * len(evidence_lines))
        pdf.setFillColor(TEAL_LIGHT)
        pdf.roundRect(panel_x, y - box_h + 7, panel_w, box_h, 6, fill=1, stroke=0)
        draw_text(pdf, evidence, panel_x + 10, y - 6, panel_w - 20, font=FONT_BOLD, size=8.2, leading=10.5, color=NAVY)
        y -= box_h + 6
    y = max(y - 16, 92)
    pdf.setFillColor(NAVY)
    pdf.setFont(FONT_BOLD, 8)
    pdf.drawString(panel_x, y, "PORTFOLIO EVIDENCE")
    y -= 25
    tag_x = panel_x
    for tag in criteria:
        width = tag_width(tag)
        if tag_x != panel_x and tag_x + width > PAGE_W - MARGIN:
            y -= 22
            tag_x = panel_x
        tag_x = draw_tag(pdf, tag, tag_x, y)
    draw_footer(pdf, page_number)


def build_pdf() -> Path:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(OUTPUT), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    pdf.setTitle("Anna Maria Kotua - Otago Polytechnic BAS Application Portfolio")
    pdf.setAuthor("Anna Maria Kotua")
    pdf.setSubject("Bachelor of Architectural Studies application portfolio")

    draw_cover(pdf)
    pdf.showPage()
    draw_context_page(pdf, 2)
    pdf.showPage()

    works = [
        dict(
            number="01",
            category="Architectural ideas",
            title="Co-Housing Concept",
            metadata="SIT 2025  |  ACADEMIC TEAM PROJECT  |  RESULT: 99%",
            description="A coordinated residential proposal exploring multi-generational living, communal gathering, privacy, accessibility and environmental response across a shared site.",
            role="Anna Maria prepared all floor and site plans, elevations, 3D work, drawings and images, then assembled the final sheets and slides. Teammates contributed the cultural, social, environmental and external-cladding writing; the group presented the proposal collaboratively.",
            evidence="Confirmed team result: 99%. Supporting academic documentation is available.",
            criteria=["composition", "concepts", "digital 3D"],
            images=["images/Co Housing 2.png", "images/COHOUSINGVID1.png", "images/COHOUSINGVID2.png"],
            captions=["Co-housing overview prepared by Anna Maria", "Lead-house presentation view by Anna Maria", "Coordinated site visualisation by Anna Maria"],
        ),
        dict(
            number="02",
            category="Drawing and design development",
            title="Residential Concept Sketch",
            metadata="SIT 2025  |  INDIVIDUAL ACADEMIC WORK  |  FREEHAND",
            description="A perspective drawing used to test roof form, frontage, entry sequence, planting and the relationship between house and street before technical resolution.",
            role="Individual freehand concept development by Anna Maria, forming the first stage of the resolved residential design project.",
            criteria=["drawing skills", "composition", "concepts"],
            images=["RESIDENTIAL DESIGN page 0 sketch.jpeg"],
            captions=["Freehand perspective and early design development"],
        ),
        dict(
            number="03",
            category="Resolved design and model-making",
            title="Residential Design and 3D Model",
            metadata="SIT 2025  |  INDIVIDUAL ACADEMIC WORK  |  AWARD",
            description="A complete residential design developed into a hand-built model communicating massing, roof form, access, material relationships and landscape intent.",
            role="Individual design, technical drawing package, presentation and physical model-making by Anna Maria.",
            evidence="ADNZ Otago-Southland Branch Award - Best Presented Resolved Residential Design, 2025.",
            criteria=["concepts", "model-making", "technical drawing"],
            images=["images/3D Model Residential 1.jpg", "images/Award Yr 1.png"],
            captions=["Hand-built residential model", "Award documentation"],
            layout="main-detail",
        ),
        dict(
            number="04",
            category="Freehand spatial drawing",
            title="Block Perspective Studies",
            metadata="SIT 2025  |  INDIVIDUAL ACADEMIC WORK",
            description="A drawing sequence investigating proportion, construction lines and three-dimensional communication through orthographic, isometric, oblique, planometric and perspective methods.",
            role="Individual manual drawing study by Anna Maria. The selected pages show the transition from measured form into one-point and two-point perspective.",
            criteria=["drawing skills", "perspective", "spatial thinking"],
            images=["images/BLOCK SKETCH page 7.jpeg", "images/BLOCK SKETCH page 4.jpeg"],
            captions=["One-point and two-point perspective", "Shaded isometric and oblique studies"],
        ),
        dict(
            number="05",
            category="Built work",
            title="Transportable Timber Cabin",
            metadata="SELF-BUILT PROJECT  |  18 SQUARE METRES  |  COMPACT DWELLING",
            description="A compact timber cabin demonstrating small-space planning, structural construction, exterior-envelope decisions and coordinated material choices.",
            role="Anna Maria initiated and participated in the hands-on construction of the transportable cabin, working collaboratively through the build and interior completion.",
            criteria=["concepts", "construction", "3D outcome"],
            images=["images/CabinExterior1.png", "images/2.jpg", "images/7.jpg"],
            captions=["Completed transportable cabin", "Compact interior", "Finished bedroom and living space"],
        ),
        dict(
            number="06",
            category="Adaptive reuse",
            title="Three-Room Shipping Container Conversion",
            metadata="BUILT PROJECT  |  MATERIAL REUSE  |  THREE FINISHED ROOMS",
            description="A steel shell transformed through opening formation, insulation, interior lining, services and finishing into three independent usable rooms.",
            role="Anna Maria contributed hands-on and documented the conversion across its stages, from the original steel shell through lining and completion.",
            criteria=["concepts", "material reuse", "construction"],
            images=["images/SHIPPING CONTAINER CONVERSION 3 container outside.jpg", "images/SHIPPING CONTAINER CONVERSION 44.jpg", "images/SHIPPING CONTAINER CONVERSION 58.jpg"],
            captions=["Original steel container", "Openings and exterior fit-out", "Completed three-room conversion"],
        ),
        dict(
            number="07",
            category="Consented adaptive reuse",
            title="Bedroom-to-Kitchen Renovation",
            metadata="PRE-2020  |  CONSENTED AND BUILT  |  RESIDENTIAL ALTERATION",
            description="A former bedroom redesigned as a custom kitchen through hand-drawn plans, relining, joinery planning, storage resolution and construction.",
            role="Anna Maria stripped the room to its framing, designed the layout around view and workflow, coordinated the alteration and completed the project in her own home.",
            evidence="Consent documentation is available on request.",
            criteria=["drawing skills", "adaptive reuse", "built outcome"],
            images=["images/kitchen-renovation-before-original-room.jpg", "images/KITCHEN RENOVATION PLANS 8.jpg", "images/KITCHEN RENOVATION 15.jpg"],
            captions=["Original room and adjoining circulation", "Hand-drawn layout study", "Completed custom kitchen"],
        ),
        dict(
            number="08",
            category="Consented residential design",
            title="Residential Renovation and Covered Living",
            metadata="PRE-2020  |  CONSENTED AND BUILT  |  CLIENT PROJECT",
            description="A client renovation developed through plans and three-dimensional visualisation into a completed internal refit, covered deck and conservatory-linked outdoor space.",
            role="Anna Maria developed the design and consent documentation, communicated the proposal through drawings and 3D views, and documented the completed transformation.",
            evidence="Consent documentation and the detailed project record are available on request.",
            criteria=["concepts", "documentation", "built outcome"],
            images=["images/Jen Alex transform 2.png", "images/JenAlexfloorplan.png", "images/JenAlexcoveredporch2.png"],
            captions=["Before and completed transformation", "Spatial layout from project documentation", "Completed covered living area"],
        ),
        dict(
            number="09",
            category="Creative practice",
            title="Country Girl",
            metadata="2026  |  PAINTING AND SCULPTURAL TEXTURE",
            description="A forest figure composition using light, central perspective and a modelled foreground of hand-shaped flowers to move from painted depth into physical relief.",
            role="Original mixed-media artwork by Anna Maria. The paired detail demonstrates the depth and construction of the raised floral surface.",
            criteria=["composition", "concepts", "sculptural texture"],
            images=["images/ART 2026 country girl texture.jpg", "images/ART 2026 country girl texture close up.jpg"],
            captions=["Full composition", "Raised floral surface detail"],
            layout="main-detail",
        ),
        dict(
            number="10",
            category="Spatial painting",
            title="Kaka Point Lighthouse",
            metadata="2026  |  COASTAL LANDSCAPE PAINTING",
            description="A pathway establishes a strong spatial sequence while the lighthouse, landform, radiating sunset and contrasting water create focus, distance and movement.",
            role="Original painting by Anna Maria, selected for architectural subject matter, compositional hierarchy and the communication of depth.",
            criteria=["composition", "concepts", "spatial depth"],
            images=["images/ART 2026 kaka point light house 1.jpg"],
            captions=["Kaka Point Lighthouse, 2026"],
        ),
        dict(
            number="11",
            category="Figure drawing and scale development",
            title="Waterfall Embrace",
            metadata="PENCIL AND ACRYLIC  |  APPROXIMATELY 1.5 METRES  |  ARTISTIC NUDITY",
            description="A preliminary pencil composition developed into a large pencil-and-acrylic work, demonstrating figure drawing, tonal modelling and the translation of an idea across scale and media.",
            role="Original preliminary sketch and final large-format figure study by Anna Maria. The final work retains drawing as its foundation while extending the setting through painted waterfall marks.",
            evidence="Contains non-explicit artistic nudity.",
            criteria=["drawing skills", "figure study", "scale development"],
            images=["ART naked waterfall.jpg", "ART naked waterfall sketch.jpg"],
            captions=["Approximately 1.5-metre pencil-and-acrylic final work", "Preliminary pencil composition"],
            layout="main-detail",
        ),
        dict(
            number="12",
            category="Mixed media and metalwork",
            title="Steel Butterfly",
            metadata="METALWORK  |  GLASS  |  ACRYLIC  |  DECOUPAGE  |  RESIN",
            description="A reflective material study combining grinder-finished metal, glass fragments, acrylic colour, decoupage imagery and resin into a layered surface.",
            role="Material and surface development by Anna Maria. Selected to demonstrate experimentation beyond conventional drawing and painting media.",
            criteria=["range of media", "material testing", "surface design"],
            images=["images/METAL WORK GRINDING  WITH GLASS DECOUPAGE ACRYLIC steel buterfly.jpg"],
            captions=["Oblique view showing the layered reflective surface"],
        ),
    ]

    for page_index, work in enumerate(works, start=3):
        draw_work_page(pdf, page_index, **work)
        pdf.showPage()

    pdf.save()
    return OUTPUT


if __name__ == "__main__":
    result = build_pdf()
    print(result)
