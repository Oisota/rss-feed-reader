"""Cli task for loading feeds"""

from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

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
    with ThreadPoolExecutor(max_workers=8) as pool:
        pool.map(load_feed, feeds)

def load_feed(feed):
    """Load Feed"""
    headers = {
        # pretent to be edge browser on windows lolz
        # this was need to fix some webservers not responding to python requests user agent
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' 
    }
    resp = requests.get(feed.url, headers=headers, timeout=10)
    data = feedparser.parse(resp.text)

    for item in data.entries:
        try:
            if hasattr(item, 'published_parsed'):
                pub = item.published_parsed
            else:
                pub = item.updated_parsed
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