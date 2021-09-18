"""Feed Routes"""

from flask import render_template, request
from flask_login import login_required, current_user

from app.services import subscription as subscription_service
from app.services import post as post_service
from .forms import SubscriptionForm

@login_required
def feed():
    """Load whole feed"""
    page = int(request.args.get('page', '1'))
    per_page = 20
    posts = post_service.get_all(current_user, page=page, per_page=per_page)
    data = {
        'posts': posts
    }
    return render_template('main/feed.html', **data)

@login_required
def saved():
    page = int(request.args.get('page', '1'))
    per_page = 20
    posts = post_service.get_saved(current_user, page=page, per_page=per_page)
    data = {
        'posts': posts
    }
    return render_template('main/saved.html', **data)

@login_required
def toggle_save_post(post_id):
    """Updated saved status for post"""
    post = post_service.toggle_save(post_id)
    data = {
        'post': post,
    }
    return render_template('main/post.html', **data)
    
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