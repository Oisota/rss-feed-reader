"""Feed Routes"""

import logging

from flask import render_template, request
from flask_login import login_required, current_user

from app.services import subscription as subscription_service
from app.services import post as post_service
from .forms import SubscriptionForm

log = logging.getLogger(__name__)

@login_required
def feed():
    """Load whole feed"""
    page = int(request.args.get('page', '1'))
    per_page = 20
    saved = request.args.get('saved', '').lower() == 'true'
    if saved:
        posts = post_service.get_saved(current_user, page=page, per_page=per_page)
    else:
        posts = post_service.get_all(current_user, page=page, per_page=per_page)
    data = {
        'posts': posts
    }
    return render_template('feed/feed.html', **data)

@login_required
def feed_list():
    """Load feed list"""
    page = int(request.args.get('page', '1'))
    per_page = 20
    saved = request.args.get('saved', '').lower() == 'true'
    if saved:
        posts = post_service.get_saved(current_user, page=page, per_page=per_page)
    else:
        posts = post_service.get_all(current_user, page=page, per_page=per_page)
    data = {
        'posts': posts
    }
    return render_template('feed/feed-list.html', **data)

@login_required
def post_content(post_id):
    """Render content for single post"""
    # TODO turn this into a class based view
    if request.method == 'GET': # return post content
        post = post_service.get_one(post_id)
        data = {
            'post': post,
        }
        return render_template('feed/post-content.html', **data)
    elif request.method == 'DELETE': # delete post
        post_service.delete(post_id)
        return '', 200

@login_required
def toggle_save_post(post_id):
    """Updated saved status for post"""
    target_id = request.headers.get('HX-Target')
    post = post_service.toggle_save(post_id)
    data = {
        'post': post,
    }
    # check which element triggered the request, adjust template accordingly
    log.debug('Target ID %s', target_id)
    if target_id == 'post-{}'.format(post.id):
        template = 'feed/post.html'
    else:
        template = 'feed/post-content.html'

    return render_template(template, **data)

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
    return render_template('feed/subscriptions.html', **data)