"""Blueprint URLS"""

from . import views

def register_urls(bp):
    """Register routes on blueprint"""
    bp.add_url_rule('/', view_func=views.feed, methods=['GET'])
    bp.add_url_rule('/saved', view_func=views.saved, methods=['GET'])
    bp.add_url_rule('/posts/<post_id>', view_func=views.delete_post, methods=['DELETE'])
    bp.add_url_rule('/posts/<post_id>/toogle-save', view_func=views.toggle_save_post, methods=['POST'])
    bp.add_url_rule('/subscriptions', view_func=views.subscriptions, methods=['GET', 'POST'])