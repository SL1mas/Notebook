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
    form_edit_note = forms.Edit_note_form()
    form_add_note = forms.Add_note_form()
    form_delete_note = forms.Delete_note_form()
    form_add_remove_category = forms.Add_remove_category_form()
    notes = Note.query.all()
    categories = Category.query.all()
    note_id = request.values.get("note_id")
    user_id = request.values.get("user_id")
    new_note_text = request.values.get("form_edit_note")
    edit_note = Note.query.filter(Note.id == note_id).first()
    if form_add_note.save.data and form_add_note.validate():
        note = Note(title=form_add_note.title.data,
                    text=form_add_note.text.data, user_id=user_id)
        db.session.add(note)
        db.session.commit()
        flash(
            f'New note "{note.title}" was saved successfully!', 'success')
        return redirect(url_for('base'))

    if form_add_remove_category.add_category.data and form_add_remove_category.validate():
        for category in form_add_remove_category.category.data:
            category = Category.query.get(category.id)
            edit_note.categories.append(category)
            db.session.commit()
        flash(
            f'Some categories were added to the note "{edit_note.title}".', 'success')
        return redirect(url_for('base'))

    if form_add_remove_category.remove_category.data and form_add_remove_category.validate():
        for category in form_add_remove_category.category.data:
            category = Category.query.get(category.id)
            for note_category in edit_note.categories:
                if note_category == category:
                    edit_note.categories.remove(category)
                    db.session.commit()
        flash(f'Note "{edit_note.title}" category list was updated.', 'success')
        return redirect(url_for('base'))

    if form_edit_note.update.data and form_edit_note.validate():
        edit_note.title = form_edit_note.new_title.data
        edit_note.text = new_note_text
        db.session.commit()
        flash(
            f'"{edit_note.title}" note data was updated successfully!', 'success')
        return redirect(url_for('base'))

    if form_delete_note.delete.data and form_delete_note.validate():
        note = Note.query.filter(Note.id == note_id).delete()
        print(note)
        db.session.commit()
        flash(f'{current_user.first_name} note was deleted.', 'success')
        return redirect(url_for('base'))
    return render_template('base.html', notes=notes, categories=categories, form_edit_note=form_edit_note,
                           form_add_note=form_add_note, form_delete_note=form_delete_note,
                           form_add_remove_category=form_add_remove_category)


@app.route("/add_category", methods=['GET', 'POST'])
@login_required
def add_category():
    db.create_all()
    form = forms.Add_category_form()
    if form.submit_category_data.data and form.validate():
        category = Category(title=form.title.data)
        db.session.add(category)
        db.session.commit()
        flash(
            f'Category"{form.title.data}" was added successfully!', 'success')
        return redirect(url_for('base'))
    return render_template('add_category.html', form=form)


@app.route("/modify_category", methods=['GET', 'POST'])
@login_required
def modify_category():
    categories = Category.query.all()
    form_modify_category = forms.Modify_category_form()
    try:
        selected_category_id = form_modify_category.category.data.id
        modify_category = Category.query.filter(
            Category.id == selected_category_id).first()
    except:
        selected_category_id = 0
        modify_category = Category.query.filter(Category.id == 1).first()
    if form_modify_category.submit_modified_category_data.data and form_modify_category.validate():
        modify_category.title = form_modify_category.new_title.data
        db.session.commit()
        flash(f'Category was updated successfully!', 'success')
        return redirect(url_for('base'))
    return render_template('modify_category.html', form_modify_category=form_modify_category, categories=categories,
                           selected_category_id=selected_category_id)


@ app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@ app.errorhandler(500)
def server_error(error):
    return render_template('server_error.html'), 500
