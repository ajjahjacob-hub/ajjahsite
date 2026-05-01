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
PROJECT 1: 2025 Co-Housing Concept Design, PROJECT 3: WOODEN CABIN, PROJECT 6: ART GALLERY
Urgent: Fix video formatting on the following project pages to match image formatting:
PROJECT 4: SHIPPING CONTAINER CABIN (done)
Urgent: Gallery contains both a "Gallery" and "Projects" title at the top
Urgent: "Projects" title and description below are not correctly aligned with projects section
Urgent: About page title not aligned with page content
Urgent: Fix mobile hamburger menu so text is centered and clickable area cover the entire line width within the dropdown
Urgent: Embedded google form not fitting correctly on smaller screen sizes (done)
Urgent: Fix about page content alignment/margin issues
Urgent: Fix dropdown box clickable area (done)

Look at centering the google form (done)
Consider removing map from the contact page?
Footer formatting across all pages (mostly done)
"View" button for each project needs additional left padding (done)
Adding a dedicated back button to each project page, returning the user to the gallery page
Optional polish for later: add a drop-down menu under the "Gallery" in the nav bar with a list containing 
links to each seperate project page

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
