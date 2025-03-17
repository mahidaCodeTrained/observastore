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
- [Features](#features)
- [User Stories](#user-stories)
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

- Viewing Observastore
- The 'Viewing Observastore' epic focused on making sure that the site display is functional and accessible to site users either if they are logged in or just anonymous. The epic consists of the user stories that seek to help the user interact with the store through creating stories that are focused no accessibility such as search bars and filters for users to find products with and to find all of the products which are listed.

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


## Design 
- The design of this website takes some inspiration from Code Institute's 'Boutqiue Ado' project. However, there are a plethora of customisations from that which gives Observastore its own unique feel. The visuals of the site follow a very dark space esque theme truly vitalising the colors of white and black and spacegray. The design choice was vital to give the functionality of the ecommerce site it's own space like feel.
- The design of the site lets users flow across the site seemlessly going from one page to another having the feel of being in an online store that is built for their needs which is for enjoyers of the constellations. There are visuals on pages that include images so the user always has something relevant to look at to keep them engaged.
- The design of the checkout and profile in this project do take alot of inspiration from Boutique Ado... its clean, minimilistic and its true goal is to get the site user to the end goal which is completing their purchase.

## Wireframes

- The initial wireframe of Observastore is alot different to what it is now. It's come a long way in terms of its scope. The wireframes are not as detailed and are what they are meant to be.. just initial mockups of how the site is to look and work. The wireframes that I created are descriptive in their nature as instead of focusing solely on how the site is to look. I wanted to envision what the site could become.

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

