from flask import Flask, redirect, render_template, url_for, request, flash, session
from login_module import login_module

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.register_blueprint(login_module,url_prefix = "/login")


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/to_login", methods = ['GET', 'POST'])
def to_login():
    if request.method == 'POST':
        return redirect(url_for('login.login'))

@app.route("/to_logout", methods = ['GET', 'POST'])
def to_logout():
    session.pop('logged_in', None) # 移除 'logged_in' 键
    session.pop('username', None) # 移除 'username' 键
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run()