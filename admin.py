from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from models import User, Note, Category


class CustomModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.email == "test@test.lt"


admin = Admin(app)
admin.add_view(CustomModelView(Note, db.session))
admin.add_view(CustomModelView(Category, db.session))
admin.add_view(CustomModelView(User, db.session))
