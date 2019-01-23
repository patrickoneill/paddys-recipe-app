import os
from flask import Flask, render_template, redirect, url_for, request
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
    return render_template('index.html')
    
@app.route('/see_recipes')
def see_recipes():
    return render_template('recipes.html', 
    recipeCollection=mongo.db.recipeCollection.find(),
    style=mongo.db.style.find())
    
@app.route('/create_recipe', methods = ['GET','POST'])
def create_recipe():
    return render_template('createRecipe.html',
    style=mongo.db.style.find())

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    recipeCollection = mongo.db.recipeCollection
    recipeCollection.insert_one(request.form.to_dict())
    return redirect(url_for('see_recipes'))
    

@app.route('/edit_recipe/<task_id>')
def edit_recipe(task_id):
    the_recipe = mongo.db.recipeCollection.find_one({'_id': ObjectId(task_id)})
    all_styles = mongo.db.style.find()
    return render_template('editRecipe.html', task=the_recipe, categories=all_styles)
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            