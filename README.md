# DIYourself - A DIY sharing platform.

DIYourself is a site that allows its users to create formatted DIY method guides and share them with other practical people. Users make accounts that allow them to create, edit and delete DIY guides. All guides are viewable by all users, that includes those who do not yet have an account. Users with accounts may only edit and delete their own guides. Included in each method is an optional field that allows users to include a link to a video for their guide, should one exist. 
 
## UX

The UX for this site is being driven by three main considerations:

1. Functionality: the site must perform as outlined above.
1. Simplicity: the site must perform this functionality in as straightforward a manner as possible.
1. Theme: the site must achieve the first two considerations while also being appropriately thematized around DIY, making things, and practical self-sufficiency.
 
These considerations are ranked in importance already, ie. 1 is most important and 3 is the least, though I do not think that many sacrifices will need to be made to the less important considerations of theme. The majority of what consideration 3 demands, I think, can be achieved through colour, font, and image choice. 1 and 2, on the other hand, inform the structure of information directly. 

In order to meet these requirements, I have decided on a layout that looks roughly as belown (displayed are wireframes for the desktop site, wireframes for the tablet and phone experiences are available in assets/images/wireframes):

![image of homepage wireframe on desktop](/static/assets/images/wireframes/homepage-desktop.png)

![image of login page wireframe on desktop](/static/assets/images/wireframes/login-desktop.png)

![image of method form wireframe on desktop](/static/assets/images/wireframes/method-form-desktop.png)

![image of profile wireframe on desktop](/static/assets/images/wireframes/profile-desktop.png)

![image of project wireframe on desktop](/static/assets/images/wireframes/project-desktop.png)

![image of signup wireframe on desktop](/static/assets/images/wireframes/signup-desktop.png)

As you can see, the homepage consists simply of a list of DIY methods each with an expandable description, a search bar,  and an image that conveys something about the theme. If a user wishes to view the method in its entirety, they may click the “Learn More” button (I may change the text here to something more direct like “View Method”). Clicking view method takes you to a method page which will be different depending on whether the user viewing the page is logged in as the method’s author. If they are, then it will look as depicted, as they are permitted to edit and delete said method. Otherwise, these buttons will not be displayed. 

There are also log in and sign up pages that I think are very self explanatory. 

To help explain why I think the above layout is appropriate for this project I will outline some potential user stories to show how my UX meets their needs.

### User 1 (DIY fan, new to site)

I am looking for a site to help me find new DIY methods to help me upholster a chair. I navigate to DIYourself and notice a list of various method guides on the home page. I spot the search bar and try searching for “chair”, this produces a tailored list of results and one of them looks like it might tell me what I need to know. I click “Learn More” and peruse the method. I decided to give it a go myself. It works well but during the time I spend upholstering the chair, an idea occurs to me for a new DIY method, inspired by the one I tried. 

I return to DIYourself and click the button in the header to create a new method. The site prompts me to create a new account, so I go through the account creation process and then navigate back to the method creation form. I write out the steps to my method using the easy to follow form and then click publish. 

### User 2 (DIY fan, returning)

I have made a post on DIYourself but I want to edit it. I return to the website and navigate to the “My Profile” section (from the nav bar) where the posts that I have made are stored. I find the one I am looking for and click “Learn More”, then “Edit”. I use the form to make the edits that I need to, it looks just like the method creation form except that its fields are prefilled with the data that I put there for my initial method.

### User 3 (Developer)

I am a developer who is on DIYourself either randomly or because they want to check out Joseph Keable’s work. I try making an account, making a method, and decide that I want to contact the developer of the site (Joseph Keable). To do so I can scroll to the bottom of any page and use the social media links found there to contact the site’s developer.

## Theming

In order to achieve a “DIY feel” for my site, I will be using a carefully selected combination of images, colours, and fonts. Below are some samples of each that are intended to convey a sense of where I would like to go thematically. They are not my final choices! The live website may vary from what is shown, though I think the vibe will be the same. 

### Color Palette

![image of brown and red colour palette](/static/assets/images/color/colour-pallete1.png)

![image of brown and red colour palette](/static/assets/images/color/colour-pallete2.png)

### Fonts

![image of rustic font sample](/static/assets/images/fonts/font1.png)

![image of rustic font sample](/static/assets/images/fonts/font2.png)

### Theme Images 

![image of woodworking tools](/static/assets/images/theming/woodwork-tools-min.jpg)

![image of woodworking tools](/static/assets/images/theming/woodwork-tools2-min.jpg)

![image of a guitar](/static/assets/images/theming/guitar-min.jpg)

![image of christmas decorations](/static/assets/images/theming/christmas-min.jpg)

![image of candles being made](/static/assets/images/theming/candles-min.jpg)

![image of woodworking tools](/static/assets/images/theming/woodwork-tools3-min.jpg)
 
<!--Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.-->

## Features

1. Site-wide:
    1. A header: This element allows users to navigate around the site. By default it contains a title, a subtitle and three buttons. The buttons: log in, create a new account, and create a new method (if you are not logged on, this simply prompts you to create an account). If you are logged in, the “create account” and login buttons are replaced by a logout button and a “my profile” button. 
    1. A footer: This element allows users to view basic copyright information about the site and contains links to the developers social media, so that they can contact said developer if wanted
1. Homepage:
    1. A search bar: this allows you to filter the site’s DIY methods by keywords.
    1. A dynamic list of the site’s methods: each method has an expandable description as well as a button link to its own method page. This allows users to peruse methods in search of something interesting. 
1. DIY Method page:
    1. Contents of the method page fill out dynamically based on the method that it is for.
    1. “Edit” and “Delete” buttons are available for the author of the method only. 
1. Create DIY method page:
    1. This contains a form where users can fill out the details of their DIY method. The form contains fields for: Method Title (Text, Required), Method type (Text, Dropdown, Required), a video link (Text, Link Format, Optional) and Step 1 (Text, Required). It also has a button that allows users to add additional steps (which are all optional). 
1. Edit DIY method page:
    1. The same as the create page, except the form has been filled in with the details of your existing post. 
1. Sign up page:
    1. This contains a form for new users to register to the site. They must provide an alphanumeric username and password with no special characters between 5 and 25 characters long. The password must be confirmed to register. This helps prevent users creating an account with the wrong password by accident. 
    1. There is also a link directing users to log in, if they already have an account. 
1. Login page:
    1. This is the same as the sign up page except it is for existing users. Therefore the form contains no “Confirm Password” field.
    1. The form also instead prompts users to sign up if they have not yet done so. 


<!--- In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future: --->

### Features Left to Implement
- Comments section + ability to reply to comments.
- Ability to upvote and downvote comments and posts
- Embedded videos on pages.
- Custom images for different methods (on a type by type basis).

<!---## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Bugs

- bug discovered where form validation for confirm password stopped working on sign up page. 
- bug discovered where method page does not immidiately update after editing, requires reload.
- bug discovered where " appears at the end of method description strings when read from the db...

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

https://www.programiz.com/python-programming/datetime/current-datetime
https://www.programiz.com/python-programming/methods/list/reverse
https://www.dwuser.com/education/content/the-basics-of-overlaying-content/
https://developer.mozilla.org/en-US/docs/Web/CSS/white-space
https://stackoverflow.com/questions/9139075/how-to-show-a-confirm-message-before-delete/19973570

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X--->

