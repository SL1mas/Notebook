from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from __init__ import app, db, login_manager, bcrypt
import forms
from models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/register", methods=['GET', 'POST'])
def register():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for('base'))
    form = forms.Registration_form()
    if form.validate_on_submit():
        form.check_email(email=form.email)
        encrypted_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(
            first_name=form.name.data, email=form.email.data, password=encrypted_password)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('base', id=current_user.id))
    form = forms.Login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(
            email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('base'))
        else:
            flash('Login failed. Check your email address and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/base", methods=['GET', 'POST'])
@login_required
def base():
    return render_template('base.html')


@ app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@ app.errorhandler(500)
def server_error(error):
    return render_template('server_error.html'), 500
