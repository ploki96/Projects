from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/dashboard')
def dashboard():
    data = {
        'id': session['id']
    }
    user = User.single_user_w_recipes(data)
    recipes = Recipe.get_all()
    return render_template('dashboard.html', user = user, recipes = recipes)

@app.route('/recipes/new')
def new_recipe():
    return render_template('new_recipe.html')

@app.route('/recipes/create', methods=["POST"])
def add_recipe():
    data = {
    'user_id': session['id'],
    'name': request.form['name'],
    'description': request.form['description'],
    'instructions': request.form['instructions'],
    'thirtymin': request.form['thirtymin'],
    'date': request.form['date'],
    }
    if not Recipe.validate_recipe(data):
        return redirect('/recipes/new')
    Recipe.add_recipe(data)
    return redirect('/dashboard')

@app.route('/recipes/edit/<int:num>')
def edit_recipe(num):
    return render_template('edit_recipe.html',id = num)

@app.route('/recipes/edit/<int:num>/process', methods=['POST'])
def process_edit_recipe(num):
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'thirtymin': request.form['thirtymin'],
        'date': request.form['date'],
        'id': num
    }
    if not Recipe.validate_recipe:
        s = f'/recipes/edit/{num}/process'
        return redirect(s)
    Recipe.edit_recipe(data)
    return redirect ('/dashboard')

@app.route('/recipes/delete/<int:num3>')
def delete_recipe(num3):
    data={
        'id': num3
    }
    Recipe.delete_recipe(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:num2>')
def recipe(num2):
    data = {
        'id': num2
    }
    recipe = Recipe.get_recipe(data)

    data2 = {
        'id': session['id']
    }
    user = User.single_user_w_recipes(data2)
    return render_template('recipe.html', recipe = recipe[0], user = user)