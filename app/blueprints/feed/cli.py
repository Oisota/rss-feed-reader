"""Cli task for loading feeds"""

from datetime import datetime

import requests
import feedparser

from app.services import subscription
from app.services import post

def register_commands(bp):
    """Register CLI commands on blueprint"""
    bp.cli.command('load')(load)

def load():
    """Load feeds, save to DB"""
    feeds = subscription.get_all()

    for feed in feeds:
        resp = requests.get(feed.url, timeout=10)
        data = feedparser.parse(resp.text)

        for item in data.entries:
            try:
                pub = item.published_parsed
                pub_date = datetime(pub.tm_year, pub.tm_mon, pub.tm_mday, pub.tm_hour, pub.tm_min, pub.tm_sec)
                info = {
                    'user_id': feed.user_id,
                    'subscription_id': feed.id,
                    'pub_date': pub_date,
                    'feed_title': data.feed.title,
                    'title': item.title,
                    'url': item.link,
                    'content': item.summary,
                }

                post.insert(**info)
            except AttributeError as e:
                print('Error parsing feed: {}'.format(feed.url))