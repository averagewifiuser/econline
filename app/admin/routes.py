from dotenv import load_dotenv
from flask import Blueprint, render_template, request, redirect, url_for
from ..forms import LoginForm, NewAdminForm
from ..functions import is_valid_uuid
import uuid
import os

load_dotenv()

admin = Blueprint('admin', __name__)

@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST' and  form.validate_on_submit():

        if form.email.data == os.getenv("EC_USERNAME") and form.password.data == os.getenv("EC_PASSWORD"):
            return redirect(url_for('admin.add_super_admin'))
        
            #do the validation for superadmins here

            #redirect to the elections landing page
    return render_template('login.html', form=form)


@admin.route('/add-super-admin/encrypted/<string:code>', methods=['GET', 'POST'], defaults={'code': str(uuid.uuid4())})
def add_super_admin(code):
    valid_uuid = is_valid_uuid(code)
    if not valid_uuid:
        return redirect(url_for('admin.login'))

    form = NewAdminForm()

    return render_template('new-admin.html', form=form)

    
