# Testing

I have run my [HTML](https://validator.w3.org/#validate_by_input), [CSS](https://jigsaw.w3.org/css-validator/), [JavaScript](https://jshint.com/), and [Python](http://pep8online.com/) through the linked code verification services and eliminated any errors they have revealed, with some exceptions. For example the Javascript validator does not recognise jQuery code and flags it as erroneous. Likewise, the HTML validator is not built to recognise Jinja templating.

### Features that need to be tested: 
1. Creating an account.
1. Logging out of and into your account.
1. Creating a new, fully featured, method.
1. Editing your method.
1. Deleting your method.
1. Viewing methods created by other users.
1. Searching for a method.
1. Viewing your uploaded methods on your profile page.
1. As an admin, creating, editing, and deleting method categories.
1. All links functional, including social media links in the footer. 

### Non Functionality that must be tested (things the site must not do):

You must not be able to access any page that you cannot access through a link in the html, through the URL bar. This enapsulates various possibilities:
1. Non-registered users (NRUs) must not be able to access any page related to CRUD functions like adding, editing, and deleting either methods or method categories. This does not include making an account.
1. Registered, logged in users (LIUs) must not be able to access pages for logging in or creating an account. 
1. All LIUs and NRUs must be unable to access pages related to category adding, editing or deleting, with the exception of admin LIUs.
1. LIUs must not be able to access pages for editing and deleting methods that they did not create.
1. The sight must not throw an error page when a user attempts to access a page for a method or category that does not exist. Or rather, it must handle it in some appropriate way.

If all these features can be shown to work, then all the User Stories, outlined in this project’s ReadMe, will be completable. Below are steps explaining how to perform each test, with accompanying images from my own testing.

## Feature Testing

### Feature 1 (Creating an account)
1. Click the sign up button.
![Image of empty sign up form](static/assets/images/testing/feature11.png)

1. Fill in the sign up form with a unique username and password, making sure that your inputs meet the expected format. The format is between 5 and 15 characters (enforced on both front and backend), which can be any letter (upper or lowercase), or any digit (0-9).
![Image of filled sign up form](static/assets/images/testing/feature12.png)

1. You will now be redirected to your profile page.
![Image of profile page with welcome method showing](static/assets/images/testing/feature13.png)

### Feature 2 (Logging out of and back into your account)
1. Click the “log out” button, and be redirected to the login page. Alternatively, you can navigate to the login page from the nav bar.
![Image of log in page with log out message showing](static/assets/images/testing/feature21.png)

1. Enter your log in details and click log in.
![Image of log in page with details entered](static/assets/images/testing/feature22.png)

1. You will be redirected to your profile page.
![Image of profile page with log in message showing](static/assets/images/testing/feature23.png)

### Feature 3 (Creating a new, fully featured, method.)
1. Once logged in, click “Add New Method” from the nav bar or “make one now” from your profile page.

1. Fill out the method form with your method’s details, including a youtube link (you can use a sharing link or the link that you will find in your browser's url bar.) Click “Create Method” when done.
![Image of method creation form, filled in](static/assets/images/testing/feature31.png)

1. You will be redirected to the homepage, a flash message will inform you that you have successfully added a new method.
![Image of homepage, with method creation message showing](static/assets/images/testing/feature33.png)

1. Click “View Method” to see your new method in all its glory!
![Image of method page](static/assets/images/testing/feature34.png)

### Feature 4 (Editing your method)
1. From your methods page, when you are logged into your account, click the edit button in the top right of your method’s card.

1. Make any changes to the form for your method, which will be populated with the method’s current information by default.
![Image of method editing form, with changes made](static/assets/images/testing/feature42.png)

1. Click “Edit Method”, you will be redirected to your method’s page, where a flash message will inform you that your method has been updated.
![Image of method method page with with edit confirmation message showing](static/assets/images/testing/feature43.png)

### Feature 5 (Deleting your method)
1. When logged in, navigate to your method either from the homepage or your profile page.

1. When you are on your method’s page you will know that you are logged in if you can see the edit and delete buttons. Click the delete button.
![Image of method page, with edit and delete buttons showing](static/assets/images/testing/feature52.png)

1. A pop-up box will ask if you're sure you want to delete the method. Click “OK”
![Image of method page, with delete confirmation showing](static/assets/images/testing/feature53.png)

1. You will be redirected to the site’s homepage with a popup informing you that your method has been deleted. 
![Image of homepage with deletion confirmation showing](static/assets/images/testing/feature54.png)

### Feature 6 (Viewing method’s created by other users)
1. Either logged in or not, click on the method of another user from the homepage.

1. You will now be on the page for this method. You can view it in its entirety but you cannot edit or delete it (unless you have an admin account, which can delete methods it did not create).
![Image of a methods page without edit or delete buttons showing](static/assets/images/testing/feature62.png)

### Feature 7 (Searching for a method)
1. On the homepage, type a query into the search bar and click search (for testing purposes, make it something you know should produce results). This will produce a list of results that contain your search term in the title, description, or method steps.
![Image of homepage with search term in the search bar](static/assets/images/testing/feature71.png)

1. Click “reset”, this will return the default list of all the methods on the site.
![Image of homepage in default state](static/assets/images/testing/feature72.png)

1. For testing purposes, try searching for something you know wont produce any results, like a random string.

1. You should see nothing returned but a message saying “no results found”. You can press reset to return the list of all methods. 
![Image of homepage with search term in the search bar and no results found](static/assets/images/testing/feature73.png)

### Feature 8 (Viewing your uploaded methods on your profile page.)

1. Log into your account, you will be redirected to your account page. If you are already logged in, click “My Profile” from the nav bar. 
1. On your profile page scroll down, you should see a list of your submitted methods. You can access any of them from here.
![Image of profile page with method list showing](static/assets/images/testing/feature81.png)

### Feature 9 (As an admin, creating, editing, and deleting method categories.)

1. Log into your admin account. This is really only possible for me, as an account’s admin status is determined on the backend, but I will include the steps that I took to test this functionality anyway. 

1. From your profile page, you will see a list of the currently existing categories, click “add category”
![Image of profile page with category list showing](static/assets/images/testing/feature92.png)

1. You will now be on a page to add a new category, fill in its name and press “Create a category”.
![Image of category editing form with text being entered into the name field.](static/assets/images/testing/feature93.png)

1. Your will be redirected to your profile page and a flash message will inform you that you have created a new category.
![Image of profile page with new category added message showing](static/assets/images/testing/feature94.png)

1. Find the category you want to edit from the list and click edit, you will be sent to a form to edit the category.
![Image of category editing form with text prefilled in the name field.](static/assets/images/testing/feature95.png)

1. Rename the category whatever you want and click “edit category”, you will be redirected to your profile page and a flash message will say that your category has been successfully updated.
![Image of profile page with category successfully edited message showing.](static/assets/images/testing/feature96.png)

1. Find the category that you want to delete from the list, and click delete category, confirm the pop up box.
![Image of profile page with confirm deletion box showing.](static/assets/images/testing/feature97.png)

1. You will be redirected to your profile page and a flash message will inform you that the category has been deleted.
![Image of profile page with category successfully deleted message showing.](static/assets/images/testing/feature98.png) 

### Feature 10 (All links functional, including social media links in the footer.)

1. Click all the links on the site and make sure they do what you are expecting. You should have already done this with most of them except the footer social media links.
1. Ensure the social media links open in a new tab (not pictured).

## Non-Functionality Testing

Below are each of the possible situations where the site needs to prevent a user from doing something, with an image demonstrating how it responds. In all cases, it will kick the user back to the homepage with a message explaining why they were unsuccessful in doing the prohibited action.

### Non-Feature 1 (NRUs accessing method and category CRUD pages through the URL bar.)

* Add method page:
![image of sight behaviour when an NRU tries to access the add method page](static/assets/images/testing/non-functionality/nru-method-add.png)

* Edit method page:
![image of sight behaviour when an NRU tries to access the edit method page](static/assets/images/testing/non-functionality/nru-method-edit.png)

* Delete method page: 
![image of sight behaviour when an NRU tries to delete a method.](static/assets/images/testing/non-functionality/nru-method-delete.png)

* Add category page:
![image of sight behaviour when an NRU tries to access the add category page](static/assets/images/testing/non-functionality/nru-category-add.png)

* Edit category page:
![image of sight behaviour when an NRU tries to access the edit category page](static/assets/images/testing/non-functionality/nru-category-edit.png)

* Delete category:
![image of sight behaviour when an NRU tries to delete a category](static/assets/images/testing/non-functionality/nru-category-delete.png)

### Non-Feature 2 (LIUs must not be able to access login and sign up pages through the URL bar)

* Sign up page
![image of sight behaviour when an LIU tries to access the signup page](static/assets/images/testing/non-functionality/liu-signup.png)

* Login page
![image of sight behaviour when an LIU tries to access the login page](static/assets/images/testing/non-functionality/liu-login.png)

### Non-Feature 3 (LIUs must not be able to access category CRUD pages through the URL bar, NRU behaviour shown in Non-Feature 1)

* Add category page:
![image of sight behaviour when an LIU tries to access the add category page](static/assets/images/testing/non-functionality/nru-category-add.png)

* Edit category page:
![image of sight behaviour when an LIU tries to access the edit category page](static/assets/images/testing/non-functionality/nru-category-edit.png)

* Delete category:
![image of sight behaviour when an LIU tries to delete a category](static/assets/images/testing/non-functionality/nru-category-delete.png)

### Non-Feature 4 (LIUs must not be able to access edit and delete pages for methods they did not create through the URL bar)

* Edit method:
![image of sight behaviour when an LIU tries to edit another user's method](static/assets/images/testing/non-functionality/liu-method-edit-someones.png)

* Delete method:
![image of sight behaviour when an LIU tries to delete another user's method](static/assets/images/testing/non-functionality/liu-method-delete-someones.png)

### Non-Feature 5 (the site must respond appropriatly if a user tries to access a method or category that doesn't exist)

* Method:
![image of sight behaviour when a user tries to access a method that doesn't exist](static/assets/images/testing/non-functionality/method-does-not-exist.png)

* Category:
![image of sight behaviour when a user tries to access a method that doesn't exist](static/assets/images/testing/non-functionality/category-does-not-exist.png)

## The site across various screen sizes and browsers

[Here](https://drive.google.com/drive/folders/1RjGUIRetpx0L7lrQu5fdJ3qvGd-wv6X7?usp=sharing) are videos of me using the site across various screen sizes and browsers. Safari is not included because I don't have a mac.

## Lighthouse Reports

Below are the lighthouse reports for the pages of this site:

![Image of homepage lighthouse report](static/assets/images/testing/lighthouse/diyhomelighthouse.png)
![Image of signup lighthouse report](static/assets/images/testing/lighthouse/diysignuplighthouse.png)
![Image of method lighthouse report](static/assets/images/testing/lighthouse/diymethodhouse.png)
![Image of add method lighthouse report](static/assets/images/testing/lighthouse/diyaddmethodlighthouse.png)
![Image of add category lighthouse report](static/assets/images/testing/lighthouse/diyaddcategorylighthouse.png)
![Image of edit method lighthouse report](static/assets/images/testing/lighthouse/diyeditmethodlighthouse.png)
![Image of edit category lighthouse report](static/assets/images/testing/lighthouse/diyeditcategorylighthouse.png)
![Image of login lighthouse report](static/assets/images/testing/lighthouse/diyloginlighthouse.png)
![Image of profile lighthouse report](static/assets/images/testing/lighthouse/diyprofilelighthouse.png)