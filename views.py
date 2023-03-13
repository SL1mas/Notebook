from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db, login_manager, bcrypt
import forms
from models import User, Note, Category


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
    # form_select_project = forms.Select_project_form()
    # form_modify_project = forms.Modify_project_form()
    notes = Note.query.all()
    categories = Category.query.all()
    # try:
    #     selected_project_id = form_select_project.client_to_pick.data.id
    #     update_project_infor = Project.query.filter(
    #         Project.id == form_select_project.client_to_pick.data.id).first()
    # except:
    #     selected_project_id = 0
    #     update_project_infor = Project.query.filter(Project.id == 1).first()
    # if form_modify_project.submit_new_project_data.data and form_modify_project.validate():
    #     update_project_infor.client = form_modify_project.new_client_name.data
    #     update_project_infor.pricing_information = form_modify_project.pricing_information.data
    #     update_project_infor.price_per_month = form_modify_project.price_per_month.data
    #     update_project_infor.final_payment_claim_date = form_modify_project.final_payment_claim_date.data
    #     db.session.commit()
    #     flash(
    #         f'Modified {Project.query.filter_by(id=form_select_project.client_to_pick.data.id).first().client}\
    #              data was saved successfully!', 'success')
    #     return redirect(url_for('base'))
    return render_template('base.html', notes=notes, categories=categories)


@ app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@ app.errorhandler(500)
def server_error(error):
    return render_template('server_error.html'), 500
