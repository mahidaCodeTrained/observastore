Return to the [README.md](README.md) file.

## Table of Contents

<details>
<summary>Click here for Table of Contents</summary>

- [Validation](#validation)

- [Lighthouse](#lighthouse)

- [User Story Testing](#user-story-testing)

- [Manual Testing](#manual-testing)

- [Bugs](#bugs)

## Validation

### HTML

| Page | URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| landing | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/homepagevalid.png) | Passed all checks |
| about | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/aboutpagevalidation.png) | The django adminsitration created the about model using summernote and the model is being delivered from the backend to the frontend it's an issue that isnt to do with the html all of the html passes fine only the summernote has an error out of control. |
| FAQ | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/faqpage.png) | Passed all checks |
| contact | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/contactpagevalid.png) | Passed all checks |
| profile | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/profilevalid.png) | Passed all checks |
| storefront | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/storefrontvalid.png) | Passed all checks |
| product details | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/productdetailvalid.png) | Passed all checks |
| shopping bag | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/shoppingbagvalid.png) | Passed all checks |
| checkout | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/checkoutvalid.png) | Only error is due to the loading spinner which was taken from Boutique Ado |
| checkout success | [W3C](https://validator.w3.org/) | ![screenshot](/documentation/validation/checkoutsuccessvalid.png) | Passed all checks |



### CSS
| Page | Jigsaw URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator) | ![screenshot](/documentation/validation/stylecssvalid.png) | Passed all checks |
| checkout.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator) | ![screenshot](/documentation/validation/checkoutcssvalid.png) | Passed all checks |
| profile.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator) | ![screenshot](/documentation/validation/profilecssvalid.png) | Passed all checks |


### JavaScript

| Page | JS Hint URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| script.js | [BeautifyTools](https://beautifytools.com/javascript-validator.php) | ![screenshot](/documentation/validation/script.jsvalidation.png) | Passed all checks |

- script.js is the only file that I wrote custom js in. The other files in the project countryfield.js and stripe_elements.js are taken from Boutique Ado. 
- JSHint is down leading to me using BeautifyTools it would not load no matter what.
- ![screenshot](/documentation/validation/jshinterror.png)


### Python 

- There are many files to upload for this portion but I'll start by showing the pep8 validation process that Observastore underwent. 
![screenshot](/documentation/validation/pep8flake8.png)

- flake8 was used in the terminal to bring all of the pep8 errors into light so it can become easy to manage and fix. Most of the code already was fixed by myself while it was being created with the pep8 guidelines in my mind at all times. I really wanted to get the validation for pep8 correct this time and I believe I have done it. The following table will present the outcome of the pep8 validation. 

| File | URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| about/admin.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/aboutadmin.png) | Passed all checks |
| about/urls.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/abouturls.png) | Passed all checks |
| about/models.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/aboutmodels.png) | Passed all checks |
| about/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/aboutviews.png) | Passed all checks |
| storefront/admin.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/storefrontadmin.png) | Passed all checks |
| storefront/urls.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/storefronturls.png) | Passed all checks |
| storefront/models.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/storefrontmodels.png) | Passed all checks |
| storefront/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/storefrontviews.png) | Passed all checks |
| storefront/forms.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/storefrontform.png) | Passed all checks |
| checkout/admin.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/checkoutadmin.png) | Passed all checks |
| checkout/urls.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/checkouturls.png) | Passed all checks |
| checkout/models.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/checkoutmodel.png) | Passed all checks |
| checkout/forms.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/checkoutform.png) | Passed all checks |
| checkout/signals.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/checkoutsignals.png) | Passed all checks |
| checkout/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/checkoutviews.png) | Passed all checks |
| webhook.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/webhookspyvalid.png) | Passed all checks |
| webhook_handler.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/webhookspy.png) | Passed all checks |
| bag/contexts.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/bagcontexts.py.png) | Passed all checks |
| bag/admin.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/bagurls.png) | Passed all checks |
| bag/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/bagviews.png) | Passed all checks |
| contact/admin.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/contactadmin.png) | Passed all checks |
| contact/forms.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/contactform.png) | Passed all checks |
| contact/models.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/contactmodel.png) | Passed all checks |
| contact/urls.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/contacturls.png) | Passed all checks |
| contact/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/contactview.png) | Passed all checks |
| faq/admin.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/faqadmin.png) | Passed all checks |
| faq/models.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/faqmode.png) | Passed all checks |
| faq/urls.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/faqurl.png) | Passed all checks |
| faq/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/faqview.png) | Passed all checks |
| profiles/forms.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/profileform.png) | Passed all checks |
| profiles/models.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/profilemodel.png) | Passed all checks |
| profiles/urls.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/profileurl.png) | Passed all checks |
| profiles/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/profileview.png) | Passed all checks |
| observastore/urls.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/observastoreurl.png) | Passed all checks |
| observastore/views.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/validation/observastoreview.png) | Passed all checks |

- Settings.py and env.py wont be included as settings.py has errors that are created by django and as per the criteria Im only showing files that I have worked on and created. The env.py file cant be shown because it holds sensitive information. 
- [Go Back To Top If You Want](#testingmd)


## Lighthouse

| Page   | Mobile                                                                                  | Desktop                                                                                   | Notes                                                                                                                                                                         |
| :----: | :-------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| base.html/index.html | ![screenshot](assets/readmefiles/lighthouse/homelighthousedesktop.jpg) | ![screenshot](assets/readmefiles/lighthouse/homelighthouse.jpg) | The low scores in best practices are because of Cloudinary and users posting their images for the blogs. |
| product_details.html | ![screenshot](/documentation/lighthouse/productdetailmobilelh.png) | ![screenshot](/documentation/lighthouse/prdtdetaildesktoplh.png) | The scores are overall solid 100 SEO. |
| about.html | ![screenshot](/documentation/lighthouse/aboutmobilelh.png) | ![screenshot](/documentation/lighthouse/aboutdesktoplh.png) | The performance is low due to the high render images however the rest is very good practice and SEO also its the summernote from the text generated from the about model |
| storefront.html | ![screenshot](/documentation/lighthouse/productdetailmobilelh.png) | ![screenshot](/documentation/lighthouse/productdesktoplh.png) | High Performance in the sight!. |
| faq_list.html | ![screenshot](/documentation/lighthouse/faqmobilelh.png) | ![screenshot](/documentation/lighthouse/faqdesktoplh.png) | High Performance in the sight!. |
| contact_form.html | ![screenshot](/documentation/lighthouse/contactlhmobile.png) | ![screenshot](/documentation/lighthouse/contactlhdesk.png) | 100 SEO |
| shopping_bag.html | ![screenshot](/documentation/lighthouse/shoppingbagmobilelh.png) | ![screenshot](/documentation/lighthouse/shoppingbagdesktoplh.png) | 100 SEO! |
| checkout.html | ![screenshot](/documentation/lighthouse/checkoutmobilelh.png) | ![screenshot](/documentation/lighthouse/checkoutdesktoplh.png) | page works very well and 100 SEO |
| checkout_success.html | ![screenshot](/documentation/lighthouse/checkoutsuccessmobilelh.png) | ![screenshot](/documentation/lighthouse/checkoutsuccessdsklh.png) | 100 SEO |
| profile.html | ![screenshot](/documentation/lighthouse/profilemobilelh.png) | ![screenshot](/documentation/lighthouse/profiledesktoplh.png) | 100 SEO |

- It is important to note that SEO was at the forefront of Observastore's development. There are meta description and keywords in place in the base.html that allow for the SEO to be at a primed level. 




## User Story Testing

| **User Story** | **Pass/Fail** | **Notes** |
|--------------|------------|-----------|
| As a site admin, I want to be able to delete any listed products or services and to ensure that 'delete' in CRUD functionality is present for the admin. | ✅ / ❌ | PASS |
| As a site admin, I want to be able to add new products and to ensure that these products are available for site users to purchase. | ✅ / ❌ | PASS |
| As an admin, I need to be able to check and view customer orders in the admin panel so they can be processed. | ✅ / ❌ | PASS |
| As a site admin I need to create a fully functional page that details products that users want to know more about. If they click on a product it will redirect them to a page they can learn more about the product. | ✅ / ❌ | PASS |
| As a site admin, I need to create products that can be seen on a specific page that showcases all of the products Observastore has to offer. | ✅ / ❌ | PASS |
| As a site admin, I want to be able to create an about app so I can upload any notices or the history of the website on a separate template for customers who come to the site wanting to know what it's about. | ✅ / ❌ | PASS |
| As a site admin, I need to be able to update existing products or services on the site to change their price, description and image and details. | ✅ / ❌ | PASS |
| As a shopper, I want to be able to easily be directed to what sort of items I want to purchase if it's just telescopes, T-shirts or custom planet globes. Additionally, be able to filter products by their price. | ✅ / ❌ | PASS |
| As a site user, I want to be able to use a search bar to check if any products are listed based on my search | ✅ / ❌ | PASS |
| As a shopper, I want to be able to delete products that I no longer intend to purchase in my shopping bag. | ✅ / ❌ | PASS |
| As a shopper, I want to be able to update my shopping bag and increase or decrease the quantity of item that I selected. | ✅ / ❌ | PASS |
| As a potential consumer at Observestore, I want to be able to view and have the option to purchase the products that I see displayed on the shopping list on the site knowing what they are with a picture and description of the item. | ✅ / ❌ | PASS |
| As a site admin, I want to create FAQ'S so site users either authenticated or not can view the most common questions and answers about Observastore. (I added the "As a site admin" as it's a user story that needs to be completed by the admin to offer this functionality to the site user. It's a part of viewing observastore as FAQ's were a choice to add in my development of Observastore as a custom model.) | ✅ / ❌ | PASS |
| As a site user, I want to be able to see that there is a contact form to contact the admin or the management of the site. In this contact form I should be able to input my email, select a product that I want to bring into attention and a box to submit whatever I need to say about the product | ✅ / ❌ | PASS |
| As a site user, I want to be able to sign up to a newsletter and be told that I have successfully subscribed to the newsletter so I can find out any new deals or offers. | ✅ / ❌ | PASS |
| As a user, I want to be able to create an account at Observastore so I can login and purchase goods and services that the e-commerce site offers and manage my user profile. | ✅ / ❌ | PASS |
| As a site user, I want to be able to login to my existing account at Observastore and see my history on the site in the sense of products saved to cart and bought. | ✅ / ❌ | PASS |
| As a site user, I want to be able to see my profile when I am logged in. I want to access my profile and see my orders, or my past history. | ✅ / ❌ | PASS |
| As a site user, I want to be able to logout of my account and view the site anonymously. | ✅ / ❌ | PASS |
| As a shopper, I want to be able to securely pay for my products that I have included in my bag. | ✅ / ❌ | PASS |
| As a shopper I want to be able to be redirected to a checkout page with all of the products in my shopping bag from my shopping bag. | ✅ / ❌ | PASS |
| As a site user/admin or shopper, I want to be able to see that there is a checkout visible on the shopping bag if there are items inside of the bag. | ✅ / ❌ | PASS |
| As a site user/consumer, I want to be able to select a quantity of the item that I would like to purchase at the store. | ✅ / ❌ | PASS |
| As a shopper, I want to be able to add a specific product into a shopping bag so it's stored in time for when I would like to purchase the item. | ✅ / ❌ | PASS |

- The User Stories for Observastore have all been fulfilled apart from one. The Repair Service user story. This is a future feature that has not made the release of Observastore but it's something that is going to be added in later stages of agile development as it is not needed for this project yet.

### Unittest

- During the development of Observastore there was a high use of unittesting when writing my code and checking if the functions are behaving as intended. Through the use of the terminal and writing failed cases I ended up building full functionality of my views and models. There is a wide range of commits in my git repository for unittesting. It is often committed with "Unittest:". For the sake of letting this TESTING.md file flow without the use of more pictures as it can get excessive.. the git commmit history is open for all to see. 

## Manual Testing

### Products

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Adding Products to Bag | All products can be added to the bag by all users. | Pass |  |
| Updating Quantity of Products | The quantity of products can be updated in the bag by decreasing or increasing. | Pass |  |
| Remove Product from Bag | The remove button is on all products in the bag and can be removed. | Pass |  |
| Search Bar | Users can successfully enter search queries on the site | Pass |  |
| Product Detail Page | The product detail page shows the relevant field in the model | Pass |  |


#### About 

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| About View | Users will be able to see the sites about view with the status and the created_on date | Pass |  |
| Availability | Users can access the *About* page without needing to log in | Pass |  |
| Backend Management | The contents of the *About* page can be managed in the */admin* panel | Pass | 

#### Profile

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Order History | Users can view all of their order history straight away once they place an order that order will be there. | Pass |  |
| Email Confirmations | Email confirmations are sent after orders. | Pass |  |
| Details | The user details appear if they press the button in checkout that allows them to save their information to their profile | Pass |  |
| Update Details | The user can update their default details and this will be shown on checkout speeding the process. | Pass |  |
| Orders can be accessed again | Users can open up their orders in their profile which will send them to a view where they can see their order. | Pass |  |
| Users cant go to another users profile or access their order | Users cannot open up any other users orders or go into their profile an error message will be printed. | Pass |  |

#### Accounts

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Sign In | Users can sign in successfully | Pass |  |
| Sign Out | Users can sign out. | Pass |  |
| Sign Up | The user can sign up to the site and give their email address to which they will recieve a email confirmation that they can choose to click in their email. | Pass | The email verification although it sends does not do much if anything on the site. It was not in the pipeline in the short term when making this project. I want all users to be able to login without the hassle of the email verification just for this project.  |
| Forgot Password | The user if they have forgotten their password can click a link to get a new one which is sent in email. | Pass |  |

#### Payment

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Checkout Button | The user clicking the checkout button is redirected straight to the checkout where they can pay. | Pass |  |
| Secure Payment | Users can securely pay with stripe and in the stripe dashboard it shows as success in the webhook. | Pass |  |
| Correct Totals | The totals based on quantity are evident and correct sitewide.  | Pass |  |
| Fields are required for payment to be accepted | There are error messages in place to stop payments from happening if parts of the form that need to be completed are not completed. | Pass |  |

- There was an extensive period of testing that underwent this project. There was testing with Unittest, manually testing each function to ensure it behaves as intended and another test within the stripe dashboard to make sure the webhook endpoint is recieving the commands from the code and posting '200' instead of '500' or '400' errors.

### Devices View

| Device               | Outcome                                             | Pass/Fail |
|----------------------|-----------------------------------------------------|-----------|
| Google Pixel 6a      | Slight delay in responsiveness under heavy load.   | Pass      |
| Samsung Galaxy Tab S8 | Perfect functionality and responsiveness.          | Pass      |
| Lenovo Yoga Tab 11   | Minor UI scaling issues in landscape mode.         | Pass      |
| Dell XPS 15          | Smooth appearance and responsiveness overall.      | Pass      |
| HP Spectre x360 14   | No issues with appearance or functionality.        | Pass      |
| OnePlus 11R          | Perfect responsiveness and appearance.             | Pass      |
| iPhone 14 Pro Max    | No issues with responsiveness or functionality.     | Pass      |

### Browser View

Browser | Outcome | Pass/Fail
| --- | --- | --- |
| Safari | No appearance, responsiveness, or functionality issues. | Pass |
| Google Chrome | No appearance, responsiveness, or functionality issues. | Pass |
| Microsoft Edge | No appearance, responsiveness, or functionality issues. | Pass |
| Mozilla Firefox | No appearance, responsiveness, or functionality issues. | Pass |
| JoyUI Native Browsers | No appearance, responsiveness, or functionality issues. | Pass |

## Bugs

- This project encountered many bugs which were fixed from users being able to access other users orders and steal their orders and make it on their profile. That was fixed and now it can no longer happen as there is verification in place. 
- Observastore's other bugs came in design with the navigation pushing upwards and having padding due to the fontawesome icon. I decided to leave that as it does genuinely fit the site and is seemless.
- There are few local bugs to do with registration where it gives off a response due to email and using gmail. These dont happen in the deployed Heroku app. users can make accounts with no issues.

- There were issues with forms and mandatory fields which has now been fixed. 
- It's important to understand that (users can only checkout if they are signed up users of the site) was a decision I undertook to ensure the need for true profile validation and to avoid bogus entries. It makes more sense for users to truly sign up and checkout. Emails work for order confirmations and for email verifications.

- Observastore is a success it has come a long way since it's inception and the article that it is now is something that I am extremely proud of the testing went smoothly.
[Return to Readme](README.md)