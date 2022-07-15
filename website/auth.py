from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, UserMixin
from database import checkEmail, userHash, userId, addUser, getUserById
# from __init__ import User



auth = Blueprint('auth', __name__)


class User(UserMixin):
    def __init__(self, id, active=True):
        user_data = getUserById(id)
        self.name = user_data["first_name"]
        self.id = user_data["id"]
        self.active = active

    def is_active(self):
        #паста карбанара цезарь с курицей махито картофель фри
        # Here you should write whatever the code is
        # that checks the database if your user is active
        return self.active

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True




@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['submit_button'] == 'redirectToSignUp':
            return redirect(url_for('auth.sign_up'))
        email = request.form.get('email')
        password = request.form.get('password')

        user_exists = checkEmail(email)
        if user_exists:
            if check_password_hash(userHash(email), password):
                flash('Logged in successfully!', category='success')
                login_user(User(userId(email)), remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html")    #, user=current_user


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        if request.form['submit_button'] == 'redirectToLogin':
            return redirect(url_for('auth.login'))
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        email_exists = checkEmail(email)
        if email_exists:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            print("aded")
            addUser(email, first_name, generate_password_hash(
                password1, method='sha256'))
            login_user(User(userId(email)), remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
