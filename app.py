import os
from flask import Flask, render_template, redirect, url_for, request
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
    recipeCollection=mongo.db.recipeCollection.find(),
    recipeCat = mongo.db.recipeCat.find())

@app.route('/create_recipe', methods = ['GET','POST'])
def create_recipe():
    return render_template('createRecipe.html',
    recipeCat = mongo.db.recipeCat.find(),
    recipeMeal = mongo.db.recipeMeal.find(),
    recipeAllergy = mongo.db.recipeAllergy.find())

@app.route('/add_recipe', methods=['GET','POST'])
def add_recipe():
    if request.method == 'POST':
        recipeCollection = mongo.db.recipeCollection
        recipeCollection.insert({
            'recipe_name': request.form['recipe_name'],
            'recipe_title': request.form['recipe_title'],
            'recipe_style': request.form['recipe_style'],
            'recipe_ingredients': request.form['recipe_ingredients'],
            'dish_allergy': request.form.getlist('dish_allergy'),
            'recipe_cooking': request.form['recipe_cooking'],
            'recipe_serving': request.form['recipe_serving'],
            'recipe_time_hr': request.form['recipe_time_hr'],
            'recipe_time_min': request.form['recipe_time_min'],
            'meat_free': request.form['meat_free'],
            'recipe_score': request.form['recipe_score'],
            'recipe_user': request.form['recipe_user'],
        })
    return redirect(url_for('see_recipes' ))
    
@app.route('/edit_recipe/<task_id>')
def edit_recipe(task_id):
    recipeCollection = mongo.db.recipeCollection.find_one({'_id': ObjectId(task_id)})
    recipeCat = mongo.db.recipeCat.find()
    recipeAllergy = mongo.db.recipeAllergy.find()
    return render_template('editRecipe.html', task=recipeCollection, categories=recipeCat, allergy=recipeAllergy)
    
@app.route('/that_recipe/<task_id>')
def that_recipe(task_id):
    that_recipe = mongo.db.recipeCollection.find_one({'_id': ObjectId(task_id)})
    return render_template('thatRecipe.html', task=that_recipe)
    
@app.route('/update_recipe/<task_id>', methods=['POST'])
def update_task(task_id):
    if request.method == 'POST':
        recipeCollection = mongo.db.recipeCollection
        recipeCollection.insert({
            'recipe_name': request.form['recipe_name'],
            'recipe_title': request.form['recipe_title'],
            'recipe_style': request.form['recipe_style'],
            'recipe_ingredients': request.form['recipe_ingredients'],
            'dish_allergy': request.form.getlist('dish_allergy'),
            'recipe_cooking': request.form['recipe_cooking'],
            'recipe_serving': request.form['recipe_serving'],
            'recipe_time_hr': request.form['recipe_time_hr'],
            'recipe_time_min': request.form['recipe_time_min'],
            'meat_free': request.form['meat_free'],
            'recipe_score': request.form['recipe_score'],
            'recipe_user': request.form['recipe_user'],
        })
    return redirect(url_for('see_recipes'))
    
@app.route('/recipeCat_add', methods=['POST'])
def recipeCat_add():
    recipeCat_add = mongo.db.recipeCat
    recipeCat_add_doc = {'recipe_style': request.form['recipeCat_add']}
    recipeCat_add.insert_one(recipeCat_add_doc)
    return redirect(url_for('see_recipes'))
    
# @app.route('/category/<meat_free>')
# def category(meat_free):
   
#     if meat_free == 'Vegetarian':
#         the_category = mongo.db.recipeCollection.find({"vegetarian": "Vegetarian"})
#     elif category_name == 'Vegan':
#         the_category = mongo.db.recipes.find({"vegetarian": "Vegan"})
#     else:
#         the_category = mongo.db.recipes.find({"category": category_name})
#     return render_template('category.html', category_name=category_name, category=the_category, picture_number=pic, all_categories=all_categories)

app.route('/recipe_score/<add_id>')
def recipe_score(add_id):
    recipeCollection = mongo.db.recipeCollection.find_one({"_id": ObjectId(add_id)})
    score = recipeCollection["recipe_score"]
    score += 1
    mongo.db.recipeCollection.update({'_id': ObjectId(add_id)}, { '$set': { "recipe_score": score }})
    return redirect(url_for('see_recipes', add_id=add_id))
    
@app.route('/delete_recipe/<task_id>')
def delete_recipe(task_id):
    mongo.db.recipeCollection.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('see_recipes'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            