from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.purchase import Purchase
from flask_app.models.login_info import Login_Info


@app.route('/dashboard')
def dashboard():
    data = {
        'id': session['id']
    }
    user = User.single_user_w_purchases(data)
    return render_template('dashboard.html', user = user)


@app.route('/purchase/create', methods=["POST"])
def add_purchase():
    data = {
    'site': request.form['site'],
    'name': request.form['name'],
    'link': request.form['link'],
    'user_id': session['id']
    }
    Purchase.add_purchase(data)
    if 'site' not in session:
        session['link'] = ""
    session['link'] = request.form['link']
    if request.form['site'] == 'amazon':
        return redirect('/amazon' )
    if request.form['site'] == 'bestbuy':
        return redirect('/bestbuy')
    if request.form['site'] == 'target':
        return redirect('/target')


@app.route('/amazon')
def amazon():
    bought = Purchase.amazon()
    session.pop('link')
    if bought:
        Purchase.purchased()
    return redirect('/dashboard')


@app.route('/bestbuy')
def bestbuy():
    bought = Purchase.bestbuy()
    session.pop('link')
    print(bought)
    if bought:
        Purchase.purchased()
        print('reshgseghesg')
    return redirect('/dashboard')

@app.route('/target')
def target():
    data = {
        'link': session['link']
    }
    Purchase.target(data)
    session.clear(session['link'])
    return redirect('/dashboard')


@app.route('/purchase/delete/<int:num3>')
def delete_purchase(num3):
    data={
        'id': num3
    }
    Purchase.delete_purchase(data)
    return redirect('/dashboard')

@app.route('/login_info')
def login_info():
    data={
        'id': session['id']
    }
    user = User.single_user_w_logins(data)
    return render_template('user_settings.html', user = user)

@app.route('/login_info/add')
def add_login():
    data = {
        'user_id': session['id'],
        'website': request.form['website'],
        'username': request.form['username'],
        'password': request.form['password']
    }
    Login_Info.add_login_info(data)
    return redirect('/login_info')