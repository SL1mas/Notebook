from flask_login import current_user
from flask import flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, DateField, TextAreaField, PasswordField, \
    BooleanField, SubmitField, IntegerField, FloatField, HiddenField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from models import User, Category


class Registration_form(FlaskForm):
    name = StringField("Name", [DataRequired()],
                       render_kw={"placeholder": ""})
    email = StringField('Email', [DataRequired(), Email()], render_kw={
                        "placeholder": ""})
    password = PasswordField(
        'Password', [DataRequired(), Length(min=5)], render_kw={"placeholder": ""})
    verified_password = PasswordField("Repeat password", [
        EqualTo('password', "The password must match.")], render_kw={"placeholder": ""})
    submit = SubmitField('Register')


class Login_form(FlaskForm):
    email = StringField(
        'Email', [DataRequired()], render_kw={"placeholder": ""})
    password = PasswordField(
        'Password', [Length(min=5), DataRequired()], render_kw={"placeholder": ""})
    submit = SubmitField('Login')


class Edit_note_form(FlaskForm):
    new_title = StringField("Title:")
    new_text = TextAreaField("Text:")
    picture = FileField("Add picture:", validators=[
                        FileAllowed(['jpg', 'png'])])
    update = SubmitField("Save")


class Add_note_form(FlaskForm):
    title = StringField("Title:")
    text = TextAreaField("Text:")
    category = QuerySelectMultipleField(query_factory=Category.query.all)
    picture = FileField("Add picture:", validators=[
                        FileAllowed(['jpg', 'png'])])
    save = SubmitField("Save")


class Delete_note_form(FlaskForm):
    delete = SubmitField('Yes')


class Add_category_form(FlaskForm):
    title = StringField("Title:", [DataRequired()], render_kw={
        "placeholder": "Category title"})
    submit_category_data = SubmitField('Add')


class Modify_category_form(FlaskForm):
    category = QuerySelectField(allow_blank=True, blank_text="Select category",
                                query_factory=Category.query.all, validators=[DataRequired()])
    new_title = StringField("Title:", [DataRequired()], render_kw={
        "placeholder": "Category title"})
    select_category = SubmitField('Select')
    submit_modified_category_data = SubmitField('Save')
    delete = SubmitField('Yes')


class Add_remove_category_form(FlaskForm):
    category = QuerySelectMultipleField(query_factory=Category.query.all)
    add_category = SubmitField('Add')
    remove_category = SubmitField('Remove')


class Search_form(FlaskForm):
    searched = StringField('Searched', [DataRequired()], render_kw={
                           "placeholder": "Search for title", "type": "search", "aria-label": "Search", "style": "width: 10rem"})
    submit = SubmitField('Search')
