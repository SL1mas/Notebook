from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, DateField, TextAreaField, PasswordField, \
    BooleanField, SubmitField, IntegerField, FloatField, HiddenField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from models import User


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

    def check_email(self, email):
        user = User.query.filter_by(
            email=email.data).first()
        if user:
            raise ValidationError(
                'This email is used!!! Choose another.')


class Login_form(FlaskForm):
    email = StringField(
        'Email', [DataRequired()], render_kw={"placeholder": ""})
    password = PasswordField(
        'Password', [Length(min=5), DataRequired()], render_kw={"placeholder": ""})
    submit = SubmitField('Login')
