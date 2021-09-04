"""Cli task for loading feeds"""

import requests
import feedparser

from app.services import subscription
from app.services import post

def main():
    """Load feeds, save to DB"""
    feeds = subscription.get_all()

    for feed in feeds:
        resp = requests.get(feed.url, timeout=10)
        data = feedparser.parse(resp.text)

        for item in data.entries:
            info = {
                'user_id': feed.user_id,
                'subscription_id': feed.id,
                'pub_date': item.published_parsed,
                'feed_title': data.feed.title,
                'url': item.link,
                'content': item.content,
            }

            feed.insert(**info)