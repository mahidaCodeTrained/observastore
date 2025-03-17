# Observastore

Observastore is an online e-commerce site where aspiring astronomers and enjoyers of the great beyond of Space can gather to purchase the products tailor made to fit their needs whether it is a high end to budget telescope to observe the night skies or a custom globe built to detail planets or a designed t-shirt highlighting their love for space. Observastore is built to ensure that they have what they need when they come to purchase on the site.

- The project is extensive this README.md file will go through the process of creating Observastore from the business models, development approaches, features, tools and technologies, testing and more. As shopping at Observastore wishes to unlock your eyes to observe the night skies we will observe just how this e-commerce project Observastore came to be.

## Table of Contents
<details>

<summary>Click here for the Table of Contents</summary>

- [Agile Development](#agile-development)
- [CRUD Functionality](#crud-functionality)
- [Entity Relationship](#entity-relationship)
- [Business Model](#business-model)
- [Design](#design)
- [Wireframes](#wireframes)
- [Mockup Screenshots](#mockup-screenshots)
- [Features](#features)
- [Pages](#pages)
- [Tools & Technologies](#tools--technologies)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)
</details>

## Agile Development
Observastore was developed with Agile methodology at the forefront. The development process was always trying to follow the user stories that were created for this project which were uploaded onto a kanban board so that I could work on each issue one by one and pass the criterias that were set for it. The board was used extensively with this project having over 20 user stories all being completed within the board. In additon, the project has great use of milestones/epics to categorise user stories so specific user stories for example that relate to admin or relate to viewing Observastore can be grouped together for better access. It is paramount to remember that agile methodology is an adaptable and incrementive approach to development; improving the functionality and user experience bit by bit to get the finished article. The epics that were created for this project truly did help with planning, organising and giving an overview of what Observastore needs to accomplish. We will dive into each epic now.

- Admin
The 'Admin' epic is critical to making Observastore a functioning e-commerce site. The admin epic focused on ensuring that users can create accounts, that the admin can list products, edit products, delete products and create backend logic which will serve to help the site in engagement through creation of forms and pages. The admin can manage all users in the django administration by checking their emails and form submissions and their order history when they are users on the site.
### Admin User Stories
- As a site admin, I want to be able to delete any listed products or services and to ensure that 'delete' in CRUD functionality is present for the admin.
- As a site admin, I want to be able to add new products and to ensure that these products are available for site users to purchase.
- As an admin, I need to be able to check and view customer orders in the admin panel so they can be processed.
- As a site admin I need to create a fully functional page that details products that users want to know more about. If they click on a product it will redirect them to a page they can learn more about the product.
- As a site admin, I need to create products that can be seen on a specific page that showcases all of the products Observastore has to offer.
- As a site admin, I want to be able to create an about app so I can upload any notices or the history of the website on a separate template for customers who come to the site wanting to know what it's about.
- As a site admin, I need to be able to update existing products or services on the site to change their price, description and image and details.


- Viewing Observastore
- The 'Viewing Observastore' epic focused on making sure that the site display is functional and accessible to site users either if they are logged in or just anonymous. The epic consists of the user stories that seek to help the user interact with the store through creating stories that are focused no accessibility such as search bars and filters for users to find products with and to find all of the products which are listed.
### Viewing Observastore User Stories
- As a shopper, I want to be able to easily be directed to what sort of items I want to purchase if it's just telescopes, T-shirts or custom planet globes. Additionally, be able to filter products by their price.
- As a site user, I want to be able to use a search bar to check if any products are listed based on my search
- As a shopper, I want to be able to delete products that I no longer intend to purchase in my shopping bag.
- As a shopper, I want to be able to update my shopping bag and increase or decrease the quantity of item that I selected.
- As a potential consumer at Observestore, I want to be able to view and have the option to purchase the products that I see displayed on the shopping list on the site knowing what they are with a picture and description of the item.
- As a site admin, I want to create FAQ'S so site users either authenticated or not can view the most common questions and answers about Observastore. (I added the "As a site admin" as it's a user story that needs to be completed by the admin to offer this functionality to the site user. It's a part of viewing observastore as FAQ's were a choice to add in my development of Observastore as a custom model.)
- As a site user, I want to be able to see that there is a contact form to contact the admin or the management of the site. In this contact form I should be able to input my email, select a product that I want to bring into attention and a box to submit whatever I need to say about the product
- As a site user, I want to be able to sign up to a newsletter and be told that I have successfully subscribed to the newsletter so I can find out any new deals or offers.


- Registration and Accounts
- The next epic 'Registration and Accouunts was an important one to create for an online e-commerce site as you want to ensure that your site has users and those users can have features that no regular anonymous site user can. In this epic it was important to highlight user stories that relate to the creation of accounts to give the users a good experience when logging in with nice visuals still inherting from the base template. 
### Registration and Accounts User Stories
- As a user, I want to be able to create an account at Observastore so I can login and purchase goods and services that the e-commerce site offers and manage my user profile.
- As a site user, I want to be able to login to my existing account at Observastore and see my history on the site in the sense of products saved to cart and bought.
- As a site user, I want to be able to see my profile when I am logged in. I want to access my profile and see my orders, or my past history.
- As a site user, I want to be able to logout of my account and view the site anonymously.

- Purchase and Checkout
- 'Purchase and Checkout' was a highly important epic as it gave me the plans and ambition to create a functional checkout system for Observastore. The user stories in this are all tailored to creating the purchase flow for the store so users can have a traditional shopping experience with selecting an item, checking the price and total and delivery costs.. to then securely purchasing the item.
### Purchase and Checkout User Stories
- As a shopper, I want to be able to securely pay for my products that I have included in my bag.
- As a shopper, I want to securely enter my delivery details and I want my purchase to be delivered to the inputted address in a delivery form.
- As a shopper I want to be able to be redirected to a checkout page with all of the products in my shopping bag from my shopping bag.
- As a site user/admin or shopper, I want to be able to see that there is a checkout visible on the shopping bag if there are items inside of the bag.
- As a site user/consumer, I want to be able to select a quantity of the item that I would like to purchase at the store.
- As a shopper, I want to be able to add a specific product into a shopping bag so it's stored in time for when I would like to purchase the item.

## CRUD Functionality

*CRUD* functionality has been implemented throughout the project from when the user wants to read an about page or read the FAQ's which are built in the backend and are being delivered to the frontend for the user to read. CRUD Functionality additionaly exists when a user would like to add a product into their shopping bag where they can update the quantity of that product... all while being able to delete the product from their bag if it no longer peeks their interest to purchase. It is paramount that CRUD functionality was at the forefront of development for this project. The site user must be able to interact with a site to keep them engaged. This is why there are many options for users to submit forms for newsletters, profile or for a contact request. The CRUD functionality also exists for the superuser admin. 

Admin (Superuser only)
- *C*: Create new users, products, FAQ'S, about page statements.
- *R*: Read all of the entries in form data in the django admin.
- *U*: Update products and also update their quantity.
- *D*: Delete products, users.

Dashboard (Site Users)
- *C*: Create their own shopping bag by adding products into it for purchase
- *R*: View the about page and FAQ'S and the products that are listed which leads to their product details page.
- *U*: Users can update the quantity in their shopping bag and also update their profile details (if logged in user)
- *D*: Users can delete their profile information in their profile form, they can delete the products from their shopping bag.

## Entity Relationship
- Observastore has a plethora of models that have relationships between eachother on their functionality and their existence see the screenshot below which outlines the models that are within the project. We will dive into each model and discuss the relationships they have.

![screenshot](/documentation/entitydiagram.png)

- We will start of talking about the user. The user as a e-commerce store must uphold to achieve... has a one to many relationship with the 'Order' model. There is no limit to how many orders a user can place at Observastore. This is critical as you always want repeat shoppers in your business.
- The next relationship we will discuss is the relationship between the 'StoreGoods' model and the Category model. This is a many to one relationship as multiple StoreGoods which are essentially (products) can be assigned to a single category such as 'Telescopes', 'Globes' or 'T-Shirts' as is the case in this project. Furthermore, the relationship between the StoreGoods model and the OrderLineItem is a many to many relationship as many StoreGood (products) can be added to many OrderLineItem instances across Observastore.

- In addition, an OrderLineItem instance is tracked to every single order which allows each order to have multiple items. It's a very important model for a e-commerce site as it alows you to break down an order to find out the details of their purchase. This brings us to the UserProfile. The UserProfile model has a one to many relationship with the default user model. It allows mutliple users to have their own profiles. The UserProfile has a one to many relationship with the Order model as mutliple orders can be tracked within the UserProfile. 

- Another key entity relationship is for the ContactRequest model and the StoreGoods model. It's a many to one relationship as users or anonymous site watchers can submit contact forms about a particular product in the store acting in a way as a review. Multiple forms can be submitted based on the product that the StoreGoods model is showing.

There are additional models in place such as a newsletter and FAQ's and About which dont exactly link in with other models in terms of having a relationship but they are important to keep the site flowing and having a modern informative standard.
- We will dive into the details of each of the models.
### StoreGoods
The StoreGoods model has the following fields.
- Category
- SKU
- Name
- Description
- Price
- Sizes
- Weight
- Image

I will briefly touch on why each of these fields are included and are important.
- The Category field allows for the product to be assigned a Category.
- The SKU is important for an e-commerce site as it gives the product it's own shopping id.
- The name field is self explanatory a product must have a name so the user knows what they are looking at.
- The description field is also equally important as the item needs to be descriptive so a user can understand what the item does and if they truly need it.
- The price field is paramount to a functional e-commerce application as it allows a product to have a price which needs to be evident for functionality purposes and for the purpose that a potential customer needs to know the price of an item.
- Sizes. In this project the sizes field is an optional field. Some products do not have sizes whereas products under the category of T-Shirts do have sizes that can be selected.
- The weight field gives the product more description and its for the users sake to know how much a product weighs in the delivery. 
- The image field is essential to give the product a look which is critical in users purchasing not just online but anywhere.

### Order
- The Order model has the following fields.
- Order Number
- User Profile
- Full Name
- Email 
- Phone Number
- Country
- Postcode
- Street Address 1
- Street Address 2
- County
- Date
- Delivery Cost
- Grand Total
- Original Bag
- Stripe pid

I will go into some detail on these fields but will group up a majority of them.
- The Order Number field is important as it produces an original order number which acts as an ID that is saved onto a user profile and shown in message alerts to the user.
- Full Name, Email, Phone Number are important fields to give an order a placement to a certain person or entity. In an e-commerce site its important to provide these details so that you can follow up on your order and the site has your information if they need to follow up with you. 
- The delivery details such as Country all the way to County listed above are standard fiels just for providing a order some context for the delivery details when it will be shipped out.
- The costs of delivery and grand total allow the user to know what the order costs alltogether.
- The original bag gives the views context and the stripe pid is for stripe to process the order.

### OrderLineItem
- The OrderLineItem consists of...
- Order
- Product
- Product Size
- Quantity
- Line Item Total

- Order field is a foreign key relating to the Order model and it will take the order that was created and see the product, product size and quantity. It will show a line item total of the costs of the products in the order.

### UserProfile
- The UserProfile consists of...
- User
- Default Phone Number
- Default Delivery Options that were stated in the Order model....

- The UserProfile can be saved and its entries are always remembered for the user despite if they log off. Their entries are remembered and can be used as default when purchasing an item. 

These are the main e-commerce functional models that are present in this project. It was important to talk about them although the FAQ, ContactRequest and About model have their own importance they can be discussed later on in this README.md file.


## Business Model 
Observastore is an e-commerce platform specializing in astronomy-related products, including telescopes, planetary globes, and themed apparel (t-shirts). Our goal is to provide high-quality products to space enthusiasts, amateur astronomers, and professionals who are passionate about exploring the universe.

- Observastore operates as a B2C (Business to Consumer) site. It sells individuals who come to shop a Observastore telescopes, t-shirts and globes. It sells this to all consumers instead of just selling the products to businesses like observatories or science centers. 

- Observastore generates sales through the consumer on the platform whilst offering them free delivery if their shopping bag hits the 100 dollar total which encourages the consumer to go beyond to the next step when their shopping bag is at $99.99 to just put that extra cent in for free delivery. 

### Advantages 
- There are many advantages to shopping at Observastore than other retailers as Observastore is tailormade to serve as a hub for enthusiasts of space and exploration to get the most highly curated items built for their liking. The products are carefully selected from a range of basic to highly advanced telescopes and custom globes of planets.
- There is a seemless shopping experience with the intergration of stripe and a wide range of filtering options based on whatever category you are viewing on the site.

### Target Market 
Observastore caters to:

- Amateur Astronomers – Hobbyists looking for entry-level telescopes and accessories.
- Professional Astronomers – Individuals seeking advanced telescopes.
- Space Enthusiasts & Students – People interested in planetary globes, and space-themed merchandise.

### Store Personnel
- The admin manages the site operating on users contact requests and overseeing the delivery for orders that have been purchased by site users at Observastore. 
- The admin manages the FAQ's, about pages to provide site users with the latest updates and information that they should know about the store.

### Marketing 
- There is a newsletter built in custom made for this project. This newsletter has a subscribe button which will input their email input and send them a message that they have subscribed. The newsletter is a good way to access the targeted persons to remind them if any offers come about in the site or any reductions or updates to Observastore.

- There is a Facebook Page created just for Observastore.


## Design 
- The design of this website takes some inspiration from Code Institute's 'Boutqiue Ado' project. However, there are a plethora of customisations from that which gives Observastore its own unique feel. The visuals of the site follow a very dark space esque theme truly vitalising the colors of white and black and spacegray. The design choice was vital to give the functionality of the ecommerce site it's own space like feel.
- The design of the site lets users flow across the site seemlessly going from one page to another having the feel of being in an online store that is built for their needs which is for enjoyers of the constellations. There are visuals on pages that include images so the user always has something relevant to look at to keep them engaged.
- The design of the checkout and profile in this project do take alot of inspiration from Boutique Ado... its clean, minimilistic and its true goal is to get the site user to the end goal which is completing their purchase.

### Color Scheme 
- The use of color has been and always will be a clear development goal that is etched within the mind. In Observastore's inception the use of color was always at the forefront of my mind. To create a space, observatory and star like color pallete it was critical to use a certain select amount of colors to help bring this vision into life. These are the most important colors that were used across this project lets dive into them now.

- `black` this color was used throughout the project mainly in the navigation, footer and the text. It was important to bring the color black into the fold for this project because its clear goal is to reach Observatory lovers and lovers of the great beyond. Black is a color that is thematic with space. It is important to add black is also visually professional. It gives the site a modern touch.

- `white` this color was important as it is used as an anthisisis to black. The color white is visually impressive when put up against a black backdrop which is the case in this project Observastore. There are numerous accoutnts of this color being used in forms, as header text and navigation text against a black background.

- `#007bff` this color was used for alot of the buttons in the site its a visually striking color which was used as a hover for the product categories in the storefront template. It keeps the user engaged and it serves as a reminder that something that is the color blue is often interactive.

- `linear-gradient(45deg, #212121, #424242)` this color features only in the sign in and sign up and auth templates it is a great color fits the space theme very well.

-`#7CFC00` this color was used in alot of hover elements especially in the navigation. The color is akin to green its a baby lime type of green which semantically gives the assurance that if this is clicked then it can be accessed.

- `azure` was used in the checkout and checkout success templates as forms are usually placed with colors such as white, beige and azure. Azure gives the form that aesthetic that it was going for.

I used the website [coolers.co](https://coolors.co/) to generate my color pallete for this project.

![screenshot](/documentation/coolers.png)

### Typography 

Google Fonts was utilised for this project as there was a particular font I wanted most if not all of the text in the project to be within. That font is called Montserrat, sans-serif.
- 'Montserrat, sans-serif' is a popular font for many websites across the world. It gives off a professional easy on the eye visual to text across Observastore. In a certain way it almost seems space like and futuristic which is probably why I went for it. 

## Wireframes

- The initial wireframe of Observastore is alot different to what it is now. It's come a long way in terms of its scope. The wireframes are not as detailed and are what they are meant to be.. just initial mockups of how the site is to look and work. The wireframes that I created are descriptive in their nature as instead of focusing solely on how the site is to look. I wanted to envision what the site could become as time went on. There is alot of with placeholder and generic thoughts that popped up in my head when I created these intial wireframes. They aren't pretty but they helped me capture an image of what the site should look like.. and from these wireframes there is a lot of improvement and vision in the final deployed site.

### Landing Page 
![screenshot](/documentation/landingwireframe.png)
- This landing wireframe gave me the vision to create a landing page with a hero and a button that leads to the shop which instantly serves its purpose and tells the users on the site that this is an online shop.

### Product Page 
![screenshot](/documentation/productswireframe.png)
- This gave me the idea to put the products listed in rows and columms as it would be visually more impressive. It also is good user experience for desktop ensuring that the user can see many products straight away instead of having to scroll to view all of them one by one. That makes more sense for a mobile approach which is always at the heart of development to make it mobile friendly. You will see the initial wireframe below showing the mobile view for product listing.
![screenshot](/documentation/mobilewireframe.png)


### Profile Page 
![screenshot](/documentation/profilewireframe.png)
- The profile was one of the pages that in the intial wireframing had a clear indication of what I wanted to exactly put in here. In the image you can see the textareas where I wanted the details and also past orders of the user to be on this page. This is critical for an E-commerce site as users should be able to check their history of their orders. The next and final inital wireframe I will show you is of the checkout page where I had the clearest idea of how to format it. 

### Checkout Page 
![screenshot](/documentation/checkoutwireframe.png)
- Balsamiq which was used to create these wireframes had a template for a checkout page which I benefitted from using my own styling and also guidance from Boutique Ado. The Checkout page was initalised to be designed with the order being shown with a form active for the user to post their details and then stripe would secure their payment. 

- There are more pages in Observastore such as the contact page, FAQ and about page and also the shopping bag but the designs of them in my inital wireframing copy the format of my product pages. To avoid repititon I will not show those but instead the next section of this README.md file will explore the final mockup screenshots of the live site and we will see just how far we have come from these initial wireframes.


## Mockup Screenshots

## Features 
- Observastore being a e-commerce store is hailed by a plethora of features for the user to enjoy and for the user to experience. The site is fully interactive where the choices of the user will set their destinations on the site with links leading to new pages such as from the initial landing page the navigation is there for the user to go in any direction they want if that is straight to the products page or if they want to login or register first, or perhaps check the FAQS or check the about page to learn more about Observastore.

- We will dive into the vast number of functions that are in place at Observastore for the user to enjoy their experience from links... buttons.... prompts and more.

### Future Features

- Observastore seeks to go beyond in the future... there are more features that can be implemented that were in the pipeline but did not make the intial project. 
- One of these features are a repair service where the user can book in a repair slot for the store which is actually based on a fictional observatory called Observaverse made by me.
- Another feature is the inclusion of a rental service... to rent out a high grade telescope for a certain select amount of days.


## Tools & Technologies 
- This is the tools and technologies used in this project. 
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) this language was used as the forefront of the project with django.
- [CSS](https://en.wikipedia.org/wiki/CSS) was used to style html elements in the page.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used to add functionality to certain elements with the use of ids.
- [Django](https://www.djangoproject.com/) Django framework used to create the app and project.
- [Postgresql](https://www.postgresql.org/) was used as a relational database.
- [Cloudinary](https://cloudinary.com/home) was used as an image storage for featured_images to be used in project by users.
- [HTML](https://en.wikipedia.org/wiki/HTML) this was used to create the templates users will see.
- [Git](https://git-scm.com/) used to control the site via "git add, git commit -m, git push" and etc.
- [GitHub](https://github.com/) was used to store my code and acess my project repository. 
- [VScode](https://code.visualstudio.com/) used as an IDE
- [Pexels](https://www.pexels.com/) used to get images
- [Bootstrap 5](https://getbootstrap.com/) was used to style html and give it mobile first styling very quickly and easily.
- [Font Awesome](https://fontawesome.com/) was used to get alot of icons to use in the project
- [JQuery](https://jquery.com/) was used to create some logic for buttons.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) was used to deploy the project.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) was used to deploy the project.
- [Gunicorn](https://gunicorn.org/) was used as a Python WSGI HTTP Server for UNIX to support the deployment of the Django application. 
- [Django Template](https://jinja.palletsprojects.com) was used as a templating language for Django to display backend data to HTML through loading or blocking content.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication, registration, and account management.
- [Summernote](https://summernote.org/) was used as a WYSIWYG editor.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/stable/index.html) was used to render the forms and have them display very well.
- [Stripe](https://stripe.com/gb) was used to create the payment service for the project.

- These are a few more tools that I used in the inception of the project.
- [Coolors](https://coolors.co) was used to create a color palette for the website.
- [Balsamiq](https://balsamiq.com/) was used to create the wireframes.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used for code review and testing.
- [Favicon.cc](https://www.favicon.cc/) was used to create the site favicon.
