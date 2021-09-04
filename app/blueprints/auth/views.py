"""Authentication View"""

from flask import request, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required

from app.services import user as user_service
from .forms import LoginForm, RegisterForm

def login():
    """Login View"""
    form = LoginForm()
    register_form = RegisterForm()
    login_message = ''

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = user_service.validate(email, password)

        if user: # user validated, login
            login_user(user)
            return redirect(url_for('main.feed'))

        login_message = 'Incorrect email or password'

    data = {
        'form': form,
        'register_form': register_form,
        'login_message': login_message,
    }
    return render_template('auth/login.html', **data)

@login_required
def logout():
    """Logout user"""
    logout_user()
    return redirect(url_for('auth.login'))

def register():
    """Register View"""
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = user_service.register(email, password)
        login_user(user)
        return redirect(url_for('main.feed'))
    
    return redirect(url_for('auth.login'))