import os
from flask import Flask, render_template, redirect, url_for, request, session, escape, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
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
    recipeCollection=mongo.db.recipeCollection.find())

@app.route('/create_recipe', methods = ['GET','POST'])
def create_recipe():
    return render_template('createRecipe.html',
    recipeCat = mongo.db.recipeCat.find(),
    recipeAllergy = mongo.db.recipeAllergy.find())

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        recipeCollection = mongo.db.recipeCollection
        ingredients = request.form['recipe_ingredients']
        cooking = request.form['recipe_cooking']
        recipeCollection.insert({
            'recipe_name': request.form['recipe_name'],
            'recipe_title': request.form['recipe_title'],
            'recipe_style': request.form['recipe_style'],
            'recipe_ingredients': ingredients,
            'dish_allergy': request.form.getlist('dish_allergy'),
            'recipe_cooking': cooking,
            'recipe_serving': request.form['recipe_serving'],
            'recipe_time': request.form['recipe_time'],
            'meat_free': request.form['meat_free'],
            'recipe_user': request.form['recipe_user'],
        })
    return redirect(url_for('see_recipes' ))
    
@app.route('/edit_recipe/<task_id>')
def edit_recipe(task_id):
    the_recipe = mongo.db.recipeCollection.find_one({'_id': ObjectId(task_id)})
    all_styles = mongo.db.style.find()
    return render_template('editRecipe.html', task=the_recipe, categories=all_styles)
    
@app.route('/that_recipe/<task_id>')
def that_recipe(task_id):
    that_recipe = mongo.db.recipeCollection.find_one({'_id': ObjectId(task_id)})
    return render_template('thatRecipe.html', task=that_recipe)
    
@app.route('/update_recipe/<task_id>', methods=['POST'])
def update_task(task_id):
    if request.method == 'POST':
        recipeCollection = mongo.db.recipeCollection
        recipeCollection.update( {'_id': ObjectId(task_id)},
        {
            'recipe_name':request.form.get['recipe_name'],
            'recipe_title':request.form.get['recipe_title'],
            'recipe_style': request.form['recipe_style'],
            'recipe_ingredients':request.form.get['recipe_ingredients'],
            'recipe_cooking': request.form.get['recipe_cooking'],
            'recipe_user': request.form.get['recipe_user'],
        })
    return redirect(url_for('see_recipes'))
    
@app.route('/delete_recipe/<task_id>')
def delete_recipe(task_id):
    mongo.db.recipeCollection.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('see_recipes'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            