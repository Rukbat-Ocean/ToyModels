from flask import Blueprint, Flask, redirect, render_template, url_for, request, flash, session

from config import USER_DATABASE

login_module = Blueprint('login', __name__, template_folder='templates')

@login_module.route('/')
def login():
    return render_template('login.html')

@login_module.route('/to_main', methods = ['GET', 'POST'])
def to_main():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in USER_DATABASE:
            if USER_DATABASE[username] == password:
                session['logged_in'] = True
                session['username'] = username
                return redirect(url_for('main'))
            else:
                flash('密码错误', 'error')
        else:
            flash('用户名不存在', 'error')
    session['logged_in'] = False
    return render_template('login.html')





        



