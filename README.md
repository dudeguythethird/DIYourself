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
    1. A dynamic list of the site’s methods: each method has a description as well as a button link to its own method page. This allows users to peruse methods in search of something interesting. 
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
1. Profile Page:
    1. This page contains all of a user’s posts to the site.
    1. Also contains options to add, edit, and delete categories, if the logged in user is an admin. Admin status is determined with the boolean field “is_admin” in the user objects within the project’s database. It is not possible to alter the value of this through the site itself, you have to change it manually in the database on mongoDB. By default, the value of “is_admin” for newly created accounts is “false”. This prevents users from granting themselves admin rights.

### Features Left to Implement
- Comments section + ability to reply to comments.
- Ability to upvote and downvote comments and posts
- Custom images for different methods (on a type by type basis).

## Technologies Used

*   [HTML5]
    *   This project uses **HTML5** to provide structure and content to the site.
*   [CSS3] 
    *   This project uses **CSS3** to provide styling, layout and basic interactivity to the structure and content defined by HTML5.
*   [JavaScript]
    *   This project uses **JavaScript** to provide it with interactivity as well as editing the functionality provided by Materialize.
*   [Python]
    *   This project uses **Python** to determine the logic of database interactions for the site and to manipulate that data in useful ways.
*   [Materialize](https://materializecss.com/)
    *   This project uses Materialize to simplify and speed up the process of creating an attractive and intuitive front end. It provides access to boilerplate code for various elements on the sight like the nav bar, footer, and form input elements.
*   [Google Fonts](https://fonts.google.com/)
    *   This project uses **Google Fonts** to allow the adding of more interesting fonts to the project.
*   [Font Awesome](https://fontawesome.com/)
    *   This project uses **Font Awesome** to allow the inclusion of icons. 
*   [MongoDB](https://www.mongodb.com/)
    *   This project uses **MongoDB** to host a database that stores all the data that the site uses (user data, project data, and category data)
*   [Flask]
    *   This project uses **Flask**, to determine how the project is built by the browser, incorporating data from the database.
*   [Werkzeug]
    *   This project uses **Werkzeug** to provide an easy way to hash and salt passwords before storing them in the database.




<!---
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
--->
## Bugs

1. Bug discovered where form validation for confirm password stopped working on sign up page. 
    - This bug was caused by non-functional onclick and onkeyup event handlers which I improved. The code is now as bellow:

    ```javascript
    if (window.location.pathname == '/sign_up') {
    var password = document.getElementById("password")
        , confirm_password = document.getElementById("password_confirm");

    function validatePassword() {
        if (password.value != confirm_password.value) {
            confirm_password.setCustomValidity("Passwords Don't Match");
        } else {
            confirm_password.setCustomValidity('');
        }
    }

    $("#password").change(validatePassword);
    $("#password_confirm").keyup(validatePassword);
    }
    ```

1. Bug discovered where method page does not immediately update after editing, requires reload.
    - Bug squashed by using `return redirect(url_for('method', method_id=method_id))` to redirect to the method page after method editing is complete. This takes new changes into account.

1. Bug discovered where profile page for admins does not 
immediately update after adding a new category. (suspect cause is same as last bug)
    - Bug squashed by using `return redirect(url_for('profile', username=session['user']))` to redirect to the profile page after category editing is complete. This takes new changes into account.
    
1. Bug discovered where " appears at the end of method description strings when read from the DB.
    - Bug squashed by removing a rogue close quotes from edit_method.html.

1. Bug discovered where users who are not logged into an account were unable to view method pages. This was caused by the app.py code for rendering the page assuming the existence of a session user. If one were not present, the page is unable to load as it is trying to call a variable that doesn't exist.
    - Fixed with a simple `if session:...`



## Deployment

This project is deployed on Heroku through my GitHub Account. In order to do this I needed both GitHub and Heroku profile. The GitHub profile is used to store the code for the project (to create a local copy of the code and do this yourself with this code, see below). I also am using MongoDB to host my site’s database. This needs a separate account also.

To deploy a project like mine on Heroku, provided one already has the project files on their GitHub account, you must:

1. Go to Heroku and create a new app, call it something appropriate and select the region nearest you. 
1. Select the “Deploy” tab, under “deployment method” select GitHub.
1. Under “Apps connected to GitHub”, log in to your GitHub account and search for the project name of the project you are deploying. Select the appropriate project. 
1. Enable automatic deploys.
1. Go to the settings tab and define your Config Vars. These are key value pairs. The keys you will need to provide values for are “IP”, “MONGO_DBNAME”, “MONGO_URI”, “PORT”, and “SECRET_KEY”. The values that you need to associate with these keys will be determined by how you configure your Database on MongoDB, they should be unique to your project.
1. In the “Deploy” tab, scroll down to “Manual deploy” and select the branch you wish to deploy, there will probably be only one option.

### How to run this project locally
 
1. Create a [GitHub](https://github.com/) account.
1. Using Chrome, install the gitpod [browser extension](https://www.gitpod.io/docs/browser-extension/).
1. Restart the browser after installation.
1. Log in to GitPod with your GitHub account.
1. Go to the project [repository](https://github.com/dudeguythethird/DIYourself) on GitHub.
1. Click the green git pod button, this will trigger a new workspace to be created in GitPod with the project in it.
1. You must install the project requirements by typing “pip3 install requirements.txt” in the command line.
1. If you want to do further development on this project and run preview in the browser, through GitPod, you will need to create an env.py file in the project. This will need to be formatted as follows:

```python
import os

os.environ.setdefault("KEY", “VALUE”)
```
Each of the key value pairs from the heroku config vars need to be present in this file. You should also make sure that you add the env.py file to a .gitignore file so that it is not uploaded to your public GitHub. This would effectively give the world access to your private database.

 
### Cloning this project
 
Want to make some changes to this project and develop on your own version?
 
1. Got to this GitHub [repository](https://github.com/dudeguythethird/DIYourself).
1. Under the name, click the ‘code’ drop down, then clone or download.
1. Copy the URL in the HTTPS section.
1. Go to your local IDE and open the terminal.
1. Navigate to the folder you would like to clone the code in.
1. Type “git clone ” then paste the URL you copied in step 3.
1. Press enter!
1. Make sure you install all the requirements detailed in requirements.txt and set up your env.py file. How to do this in GitPod is detailed above.

Following these steps there will be no differences between deployed and development versions.
 




<!---
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.
--->


## Credits

* This taught me how to import datetime and use that data in my project: https://www.programiz.com/python-programming/datetime/current-datetime
* This alerted me to the ability to reverse lists, so the posts would display in order of upload with the most recent first: https://www.programiz.com/python-programming/methods/list/reverse
* This helped me style the background image on the main page: https://www.dwuser.com/education/content/the-basics-of-overlaying-content/
* This helped me properly format the method steps imported from the DB: https://developer.mozilla.org/en-US/docs/Web/CSS/white-space
* This helped me create a confirm message for deletion of posts and categories: https://stackoverflow.com/questions/9139075/how-to-show-a-confirm-message-before-delete/19973570
* This helped inspire the algorithm I would eventually write to correctly format youtube links for display on a method’s page, regardless of whether the user submits a sharing link or one from the browser’s search bar: https://stackoverflow.com/questions/29781974/convert-youtube-link-into-an-embed-link/29782133

### Content
* All text content on the site is original.
* Credit to YouTubers [Spawn Wave](https://www.youtube.com/channel/UCoIXnB865l9Ex9zs4OIXTdQ) and [Linus Tech Tips](https://www.youtube.com/channel/UCXuqSBlHAE6Xw-yeJA0Tunw) for the videos that are currently embedded on the site.

### Media
The photos used in this site were obtained from:
* https://unsplash.com/@thdef
* https://unsplash.com/@film2024
* https://unsplash.com/@romankraft
* https://unsplash.com/@drscythe
* https://unsplash.com/@barnimages
* https://unsplash.com/@pjswinburn
* https://unsplash.com/@roselyntirado
* https://unsplash.com/@umby
* https://unsplash.com/@sidekix
* https://unsplash.com/@wardhanaaditya
* https://unsplash.com/@samthewam24
* https://unsplash.com/@honza_kahanek

### Acknowledgements

- I received inspiration for this project from my Code Institute course and a variety of online people (in credits above).
- I am also indebted to my mentor Akshat Garg, who as ever, provided ample, patient feedback on this project. 