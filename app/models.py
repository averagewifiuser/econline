from datetime import datetime
from app.extensions import db, login_manager
from flask_login import UserMixin
import uuid

@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(60), nullable = False)