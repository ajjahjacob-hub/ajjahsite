File to add general notes on the project

To add a new image to any place in the project, use the following line:
<img src="images/NameOFYourImage.something" width="600" height="400" alt="Add a short description here">
Thanks  Jacob
On the gallery page is there any chance you can create that page as a link page to folders.
So for example when you click on the Co-Housing picture it then links you to the content of that project portfolio? If you dont understand I'll chat with you.
Total subpages: 5 minimum
TODO: Fix margin issues with gallery/project page figures
TODO: Fix gallery images not aligning with figure outline
TODO: Fix footer width
TODO: Consider changing gallery page to "Projects" page
TODO: Verify alignment and text consistency across pages
TODO: Consider adding a dedicated back button to each of the project subpages. Alternatively,
a seperate, vertical navigation menu on the left for the different projects.
TODO: Add organised subfolders for images based on the webpage/category the belong to
TODO: Potentially increase font size/bold for the name/heading of each project

Just noticed the formatting issues on gallery pages after update, should be an easy fix (only apparent on some screen sizes)

TODO: Add view fullscreen/larger when clicking project images

<a href="images/1 CO HOUSING PLANS COVER SHEET.png">
<img src="images/1 CO HOUSING PLANS COVER SHEET.png" width="800" height="600" alt="Project image 1 placeholder">
</a>

Updated list of issues, including non-essential (may 2026):

Urgent: Remove the placeholder inquiry form on contact page (done)
Urgent: Mismatched titles between gallery page projects and the project pages
Urgent: Remove placeholder images from the following project pages:
PROJECT 1: 2025 Co-Housing Concept Design, PROJECT 3: WOODEN CABIN, PROJECT 6: ART GALLERY (done)
Urgent: Fix video formatting on the following project pages to match image formatting:
PROJECT 4: SHIPPING CONTAINER CABIN (done)
Urgent: Gallery contains both a "Gallery" and "Projects" title at the top
Urgent: "Projects" title and description below are not correctly aligned with projects section (done)
Urgent: About page title not aligned with page content
Urgent: Fix mobile hamburger menu so text is centered and clickable area cover the entire line width within the dropdown (done)
Urgent: Embedded google form not fitting correctly on smaller screen sizes (done)
Urgent: Fix about page content alignment/margin issues
Urgent: Fix dropdown box clickable area (done)
Urgent: Screen sizes below ~410px in width experience overlap between menu nav and logo/company name

Look at centering the google form (done)
Consider removing map from the contact page?
Footer formatting across all pages (mostly done)
"View" button for each project needs additional left padding (done)
Adding a dedicated back button to each project page, returning the user to the gallery page
Optional polish for later: add a drop-down menu under the "Gallery" in the nav bar with a list containing 
links to each seperate project page
Add a more obvious colour shift for blue buttons across the site

Google form needs a text entry for some sections with the option to select "other"

Note for CSS rule:
#gallery img{
  aspect-ratio: 4/3;
  object-fit: cover;
  width:100%; height:auto;
}
Switching to contain will allow the full gallery images to fit and be fully visible within their 4:3 frames.
The drawback is that black bars will be added to achieve this without compromising image aspect ratio, note
that the images are fully visible by clicking to open a fullscreen view. Need to decide whether to take this 
approach or to stay with the current setup.


04/05/26 updates for current week

ESSENTIALS

Home Page:
Fix image 2 of the home page to look more realistic (bushes growing from decking!?)

Services page:
Check content is still accurate and up to date. The current content quantity is ideal.

Gallery/Project pages:
Confirmation for gallery page naming. Currently contains "Gallery" header and "Projects" subheader
Title for each project on the gallery page should match the title of the corresponding project page
Decide on cut vs fitted images for gallery/projects
Check that images and videos on project pages are appropriate and professional
Tidy project titles and description across the gallery and projects pages (Both wording and style)
Confirm direction for project6 page (currently displays other projects but is not yet functional)

About page:
The content (images and text) between "Anna Maria Kotua" and "Approach & Values" has an inconsistent amount of 
side margins. Remove/reduce to align with other content. Appeary to be margin attached to the <figure> element
Ideally a clearer picture of Anna Maria could be used for this page.
Change "KOTUA" to "Kotua"?

Contact page:
Contact details should be consistent between the "contact" section and the inquiry form, 2 different emails are given
Validate inquiry form, some questions with "other" as an option, do not currently give the user a text entry to fill
Decide on if a map is needed for the contact page (likely no, the less, the better)
Embedded inquiry form has an added scroll bar on smaller screen sizes???

Header/footer/navigation/misc:
Check spelling and grammar is correct, including inquiry form
Screen sizes below ~410px in width experience overlap between menu nav and logo/company name

NON-ESSENTIALS:
Ideally add a more drastic colour change when blue buttons are hovered, includes both gallery and other buttons
Ideally a higher resolution image should be used for home page 1st image
Elements of the header appear to have a fixed max-width. Footer elements appear to stretch further than intended.
If possible, add an X button to images opened from the project pages, a further improvement could be made to add
< and > buttons to switch to the previous/next image of that project page.
Remove the underline when hovering the logo in the footer
