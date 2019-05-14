# Milestone 4 

## Recipe App

Try it here now hosted on heroku <a href="https://recipe-app-paddy.herokuapp.com/"> Heroku Hosted App</a>

This is an app created to get users to interact with others through the love of food.
The idea of this is to be able to share and get inspired to "Cook & Create" new and 
old cullenery favourites from all over the world. With the ability to create, edit
and delete recipes making it a fun place to share and learn.

#### Code Institute Project to create a recipe app using

- HTML5
- CSS
- Pyhton
- Flask
- MongoDB/ mLab
- Materialize
- Heroku
- Github

#### HTML5
In this I have use basic HTML5 for the layout and started to use bootstrap but 
halfway through decided to use materialize as it seems to be a cleaner looking.
The framework is simpler than that of bootstrap in my opinion but doesn't have
a hugh depth across all aspect of web design. 

The app consists of
- base.html page where the frame of the app is created so that it is the same 
across the whole app. Its got the basic layout of the header and footer with a 
nav bar with 3 links/ buttons. Then for the mobile ready side it ahs the burger 
icon/ menu button with a side nav and links. The title name is a link to the 
index.html as it should. In the footer it has mirrored links for the app with a 
link to a github account.

- index.html page has very basic info as it is just the welcome page, and a button
to link it to the next page that they should land on.

- recipe.html is where the main amount of info is found as this is where the collection of 
recipes are displayed but only with a small amount of info and a read more link to the
full recipe posted and an edit button to make any changes to the recipe.

- thatRecipe.html page is the full description of the recipe and any additional info,
along with that the recipe has a delete button that will remove it from that database.

- editRecipe.html similar to the createRecipe.html page this just hold the info posted 
and displays it in the form as a placeholder and can be changed and save again



#### CSS
Using the preset CSS class helpers provided in Materialize, it is made very easy 
to style the project with spacing, color, font, button, headers and navbar. I 
have had to use very little of my own CSS code.

For the styling of the app as you can see i only have a base background colour if 
the page doesn't load the images. Then through out the app I have used the helpers 
for the sizing and colouring of the header, text, button and footer.

For the background of the app I used the parallax which makes for an interesting 
style as a whole. Using to seperate images for the background and gives it a nice 
animation when you scroll down the page.

The colour scheme I have tried to keep it to the complementing colours of green and
orange but with different levels of them colours

In the whole of the app I used the card class, I feel it create a nice look and feel 
to it. Layered inside one of another for holding the info.

#### Pyhton/ Flask

For a lot of the python/ flask  code used was very simplified, using render_template for
the links on the app and the find attribute to access the information on the database
Using the jinja code on the html side of the app for looping through the data, I did
come across a few errors in the calls that I using until I realised exactly what I
was doing. Thing to watch out for and to keep the same are what you are naming the mongo.db
in the python file and what you are using on the html side, also when you are coping a page 
that has a different name for the loop.. (ended up spending a lot of tume trying to figure out what I
had done to everything).
Using the post method to add the information to the database and getting to to write to
specific name with the request.form and using the request.form.getlist for the multiple select
menu that has the list of allergines.
The editRecipe and createRecipe code are pretty much the same except for the placeholder that has the 
info called from that database for the editRecipe so that you can see what was submitted.

I have other pieces of code that I would like to get implemented a some stage with a better layout
I have a categorie add function that I did use at one stage for populating the database but have since removed
it for the page, and I have an upvoter but can figure out how to link it up correctly.

There is the delete recipe function but I would like to in the future have it only for admins
or for user specific data e.g you can only delete you own recipes

#### MongoDB/ mLab

In this project I used mLab as the database.

Working with the database was interesting seeing how handy it is to populate 
data to a page and in reverse with the right functions

#### Wireframe

![DSC_0488](https://user-images.githubusercontent.com/33999607/57730106-a872af80-768f-11e9-91bb-6602124ad6ca.JPG)


