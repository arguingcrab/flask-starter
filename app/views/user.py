from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user

from ..forms.user import UserForm
from ..models import db
from ..models.user import User


bp = Blueprint('user', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()

    if form.validate_on_submit():
        try:
            user = User.register(
                email=form.email.data,
                password=form.password.data)
            login_user(user)
            return redirect(url_for('admin.posts'))
        except db.NotUniqueError:
            form._errors = True

    return render_template('register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = UserForm()

    if form.validate_on_submit():
        try:
            user = User.validate_login(
                email=form.email.data,
                password=form.password.data)
            login_user(user)
            return redirect(url_for('admin.posts'))
        except User.DoesNotExist:
            form._errors = True

    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))
