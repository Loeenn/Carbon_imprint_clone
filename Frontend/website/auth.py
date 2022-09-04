from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from Backend.database import checkEmail, get_user_hash, addUser, check_password
from Frontend.website import Users

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['submit_button'] == 'redirectToSignUp':
            return redirect(url_for('auth.sign_up'))
        email = request.form.get('email')
        password = request.form.get('password')

        user_exists = checkEmail(email)
        if user_exists:
            if check_password(password, get_user_hash(email)):
                flash('Logged in successfully!', category='success')
                login_user(Users.query.filter_by(email=email).first(), remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


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
        elif len(password1) > 72:
            flash('Password must be less than or equal to 72 characters', category='error')
        else:
            print("added")
            addUser(email, first_name, password1)
            login_user(Users.query.filter_by(email=email).first(), remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
