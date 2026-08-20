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

-----------------------------------------------------------------------------------------------------------------------------------

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

-----------------------------------------------------------------------------------------------------------------------------------

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
Too much space between the "Projects" title and the text below, this is likely due to these elements
being contained within the section with id="gallery"

About page:
The content (images and text) between "Anna Maria Kotua" and "Approach & Values" has an inconsistent amount of 
side margins. Remove/reduce to align with other content. Appeary to be margin attached to the <figure> element
Ideally a clearer picture of Anna Maria could be used for this page
Change "KOTUA" to "Kotua"?

Contact page:
Contact details should be consistent between the "contact" section and the inquiry form, 2 different emails are given
Validate inquiry form, some questions with "other" as an option, do not currently give the user a text entry to fill
Decide on if a map is needed for the contact page (likely no, the less, the better)
Embedded inquiry form has an added scroll bar on smaller screen sizes???

Header/footer/navigation/misc:
Check spelling and grammar is correct, including inquiry form
Screen sizes below ~410px in width experience overlap between menu nav and logo/company name, website functionality needs to be ensured 
for screen sizes of 375px and higher.
Files structure needs a complete overhaul. File/folder names should be consistent, descriptive, and follow correct naming conventions.
Additionally, each page may need to be placed into an individual folder named after the appropriate / of the page. Example:
about.html should be placed in a folder named "about". This may be required for url to look like ajjaharchitecture.co.nz/about
An alternative approach to storing images within folders is to either: create subfolders within the imgaes folder to organize images or
to create an image folder within each page folder. The latter is likely more organized.
Image names need to be updated to remove spaces and to be more accurate/descriptive
On smaller screen sizes, the footer is too tall, consider reducing verical margin of the footer content after top-down overlap is reached 
at around 560px width
On smaller screen sizes, too much white space is given between the end of the content and footer
IMPORTANT: Don't forget to setup google analytics to cover page views, click tracking, traffic, user behaviour, etc. 
Should only require a small JS snippet to each page.
Do a final clean of all code, formatting, remove old comments. CSS needs particular attention.

NON-ESSENTIALS

Ideally add a more drastic colour change when blue buttons are hovered, includes both gallery and other buttons
Ideally a higher resolution image should be used for home page 1st image
Elements of the header appear to have a fixed max-width. Footer elements appear to stretch further than intended.
If possible, add an X button to images opened from the project pages, a further improvement could be made to add
< and > buttons to switch to the previous/next image of that project page
Remove the underline when hovering the logo in the footer
Improve the overall formatting/styling, some areas look clunky

Discussion points/other notes:
Importance of SEO, custom domain, hosting options, post-deployment development, and cost efficiency
Reworking/recreating website - will be much easier once all content is finalised and organised
Hosting can be done for free directly through github pages with no downside except a 100gb/month traffic limit (unlikely to reach limit)
Recommended custom domain: ajjaharchitecture.co.nz - This should be included on the business card
Setup google analytics to cover page views, click tracking, traffic, user behaviour, etc. This will help to see how many people are actually
visiting the website, where they go, what they click, etc
Annual fee for the custom domain would likely be classed as a business expense and therefore deductible.

SEO improvement
The key things that would help for local search:
Google Business Profile - free, and arguably the most impactful single thing for local search. Shows up in Google Maps results and the local business panel. Critical for "architect Balclutha" type searches.
Page content - pages should mention the location and services explicitly. "Architecture services in Balclutha, Otago" in headings and body text helps Google understand relevance.
Meta descriptions - the site has these already on some pages which is good.
Backlinks - getting listed on NZ architecture directories or local business directories builds authority over time.
Site age - nothing to do here except get the domain registered sooner rather than later so it starts building history.

Google Business Profile is the priority since it directly targets local searches and is free.
How it works:
The client creates a free profile at business.google.com
They enter business details - name, address, phone, website URL, services, photos
Google verifies the business (usually via a postcard sent to the business address or a phone call)
Once verified, the business appears in Google Maps and the local search panel when people search for relevant terms nearby
What it does:
Shows the business on Google Maps
Displays contact details, opening hours, and website link directly in search results
Allows clients to leave Google reviews, which significantly impacts local search ranking
Free to set up and maintain

GBP should be setup after the website is already live with the correct URL
-----------------------------------------------------------------------------------------------------------------------------------

19/08/26 updates for current week

GENERAL NOTES

- Attract clients/professional - architectural focus
- Link to app
- Home/Services - professional side
- Gallery to projects, architecture - more professional section, 1 folder for student stuff locked to access code, other projects.
- 

1. Are you connected directly to GitHub, using a local folder/repository, or editing through the GitHub website?
2. Which GitHub repository and branch do you currently modify?
3. Do you commit directly to main, or can you create branches and pull requests?
4. Is there any uncommitted work, saved workspace, or local copy that contains changes not yet on GitHub?
5. What service publishes the live website, and does a push to main publish it automatically?
6. Do you have access to any other connected services for this project, such as the Home Brief site, Stripe, a domain provider, or hosting?
7. Are there any project instructions, configuration files, or workflows that another developer should know about?
