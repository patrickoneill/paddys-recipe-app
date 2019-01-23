import os
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "some_secret"

app.config["MONGO_DBNAME"] = "recipes-app"
app.config["MONGO_URI"] = "mongodb://admin:dragon99@ds159387.mlab.com:59387/recipes-app"

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
    )
    
@app.route('/see_recipes')
def see_recipes():
    return render_template('recipes.html', 
    recipeCollection=mongo.db.recipeCollection.find(),
    style=mongo.db.style.find())
    
@app.route('/create_recipe', methods = ['GET', 'POST'])
def create_recipe():
    return render_template('create-recipe.html')
    
@app.route('/edit_recpies')
def edit_recipe():
    return render_template('edit-recipe.html')
    
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            