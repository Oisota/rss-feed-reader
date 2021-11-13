"""Blueprint URLS"""

from . import views

def register_urls(bp):
    """Register routes on blueprint"""
    bp.add_url_rule('/', view_func=views.feed, methods=['GET'])
    bp.add_url_rule('/feed-list', view_func=views.feed_list, methods=['GET'])
    bp.add_url_rule('/posts/<post_id>', view_func=views.post_content, methods=['GET', 'DELETE'])
    bp.add_url_rule('/posts/<post_id>/toogle-save', view_func=views.toggle_save_post, methods=['POST'])
    bp.add_url_rule('/subscriptions', view_func=views.subscriptions, methods=['GET', 'POST'])