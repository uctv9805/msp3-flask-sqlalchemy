# Toys Team - Toy Inventory

As a budding toy collector I struggle to keep track of purchases, when and where I bought them, what they came with etc...etc. If this sounds like you then my simple Toy inventory tool will help you manage your inventory and keep track of when you bought an item so you can then track the value in the future. 

It was designed with fellow Toy enthusiasts in mind who can benefit from keeping track of what they buy, as we all know sometimes we get carried away.  

This site is targeted towards anyone who is a toy/game enthusiast and wants to keep track of there ever growing collection - It initially started as a way for our facebook group to showcase items for sale and could still grow to this in the future, I want to let the community decide what features are added and how it will evolve. 

Initially this site will be used by myself and fellow group members who have surplus stock that will be used in group giveaways/competitions/live events. It will develop further in time as authentication steps are added. 

You can visit my live site [from here](https://toys-team-toy-inventory-80ed09c090ba.herokuapp.com/)

My site is fully responsive and works across muliptle devices, I have tested this using [AmIResponsive](https://ui.dev/amiresponsive?url=https://toys-team-toy-inventory-80ed09c090ba.herokuapp.com/)

## Planning Stage

### Target Audiences:

- Anyone who is a fellow Toy enthusiast.
- Age 16 and over purely due to the fact it will be used with members of a Facebook group and they have age limitations.
- Anyone wanting to catalogue their Toys - Initially it will be known members who want to catalogue their surplus stock along with mine for our group sales/competitons/giveaways. 

### User Stories:

- As a user, I want to keep track of my toy purchases.
- As a user, I want to be able to categorise my items. 
- As a user, I want to be able to add descriptions and a date when I bought the item. 
- As a user, I want to be able to illustrate whether or not the item is crossposted for sale on other platforms. 
- As a user, I want to be able to edit items, and delete them from the database if they are sold/given away.
- As a user, I want to be able to organise in sale date order. 
- As a user, I want to be able to add new categories as and when required, when I start buying a new toy line. 
- As a user, I want to be able to edit and delete categories as my collection grows/changes. 

### Site Aims:

- To provide the user with a simple, clean, easy to use toy cataloging app.
- To make it easy to add categories and then new items to the category. 
- Offer an easy to read system to keep track of items in purchase date order. 
- To be able to easily edit and delete entries as and when required. 

### How this is achieved:

- Simple, readable buttons offering the ability to add category and add item, these each have there own page reachable by using a nice, clean navbar.

- The edit and delete item buttons are easily readable and colour coded for good user experience. 

- The add item page is a nice, readable form for users to add each section and detail required, as well as date purchased and then opportunity to add to a category.  


## Wireframes

I created wireframes using Balsamiq to properly plan my project and get a good idea of the layout and how to use the available space. Below are the links to the wireframes which includes layouts for desktop, mobile and tablet versions of the site.

The design has stayed mostly the same as the wireframes throughout this project, simplicity was key for me so apart from visual styling the overall layout from the wireframe was acheived in the final project.

## Color profile

I wanted to create something which was aesthectically pleasing with simple colours to keep the clean, organised feel to the project. The simple orange palette used is fun and works nicely with the playful nature of the toys aspect - I used one of the color palettes within the Materialize framework and kept it consistent througout the site. 

## Features

### Navbar

- I used the Materilaize framework and implemented their navbar which I changed the html to make it work for my site - I used this throughout the site for good UX and I also implemented the side nav element for responsiveness on smaller devices.

### Homepage

- The homepage is a simple, clean, easy to read site that offers the user an instant look at the current inventory. These are all available to acces using Materialize collapsibles - it shows the user the title and date and then when clicked shows the full detail of the item. I wanted this information to be viewable on the first page as it is the main purpose of the site - to track items. There is an option to add further items straight away at the top of the site. The information is complemented by a simple navbar and the sticky footer at the bottom shows who designed it and a link to my instagram page. 

### New Item

- New item takes you straight to a form to add a new item. The form is simple and clean and has icons to illustrate the purpose of each section as well as wording. Again using a Materilaize form and editing it so that it suits the need for the user. The form elements are required so that it cannot be submitted without each section being filled out keeping the website consistent. The navbar and footer are consistent again with the homepage, this will continue throughout the site. 

### Categories

- Categories allows the user to add a new category as and when new lines/toys are introduced to their collection - so that the items can be categorized to help organize them. These are set up in such a way that if edited it will edit through to the item in the category - and if they are deleted it will delete all items within the category.  

## The Footer

The footer simply offers a copyright notation and a link to my instagram page for contact purposes. 

## Features Left to Implement

### Authentication

- I want to add authentication to the site so that only people who are given access to the site can edit or delete items, currently it does not have this so it gives those who know about it free roam to control the site. 

### Modals

- I also want to add a system that produes a modal when a user tries to delete an item or a category - Something that explains - Are you sure you want to delete this item? Yes, No. And - Are you sure you want to delete this category, all items within this category will also be deleted - this cannot be undone - Yes, cancel. 

# Testing

I have created a separate document for the testing section with everything covered - [TESTING.md](TESTING.md)

# Deployment

I deployed the app on Heroku using the following steps:

1. Log in to Heroku and click New, then create new app. 
2. Choose a name and region then click create app.  
3. Go to the settings tab and click reveal config vars.
4. Add a cofig var using the database URL from your PostgreSQL from Code Institute.
5. Add each of my other environment variables as a Config Var. 
6. Navigate to the deploy tab of the app.
7. In the deployment method section, click 'connect to GitHub', find my repo and then connect.
8. Using the manual deploy section, click deploy branch.
9. With the project in place, the tables need adding to the database. 
10. Click 'more' then run database.
11. Type Python3 into the console to run.
12. Run from taskmanager import db, then, db.create_all(), then exit() the terminal.
13. My app was up and running, I clicked Open App - and it opened in a new browser successfully.

    Click here to be directed to the live site [Toys Team - Toy Inventory](https://toys-team-toy-inventory-80ed09c090ba.herokuapp.com/)

# Credits

Here is a list of people and resources I turned to throughout the project for support, without which I would not have succeeded.

### General

- Code Institute - My design took inspiration from a number of code-along projects that have been taught on the course so far, however I have adapted and created my own code so as not to simply copy and paste the ideas.

- W3Schools has been invaluable in helping me with ideas for code and problem solving issues when they arose. 

### Content

- All content for the site was written by myself.

- The icons used throughout the site were from Font Awesome [Font Awesome](https://fontawesome.com/)