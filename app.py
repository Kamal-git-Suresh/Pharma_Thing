from flask import Flask, redirect, render_template, request, url_for, session
import os
from login_form import LoginForm

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'totally_secret_key'

@app.route("/", methods= ['GET', 'POST'])
def main():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        session['logged_in'] = True
        return redirect(url_for('homepage', username = username))
    return render_template('login.html', form = form)

@app.route('/homepage/<username>', methods = ['GET', 'POST'])
def homepage(username):
    return render_template('homepage.html', message= username)

if __name__ == '__main__':
    app.run(debug='True')