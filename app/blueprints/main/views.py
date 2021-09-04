"""Feed Routes"""

from flask import render_template
from flask_login import login_required, current_user

from app.services import subscription as subscription_service
from app.services import post as post_service
from .forms import SubscriptionForm

@login_required
def feed():
    """Load whole feed"""
    posts = post_service.get_all(current_user)
    data = {
        'posts': posts
    }
    return render_template('main/feed.html', **data)
    
@login_required
def subscriptions():
    """Load subscriptions"""
    form = SubscriptionForm()
    subscriptions = subscription_service.get_all(current_user)

    if form.validate_on_submit():
        url = form.url.data
        subscription_service.add(current_user, url)
        subscriptions = subscription_service.get_all(current_user) # refresh subscriptions

    data = {
        'form': form,
        'subscriptions': subscriptions,
    }
    return render_template('main/subscriptions.html', **data)