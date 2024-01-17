#!/usr/bin/python3
"""
gets the total number of subscribers
"""
from requests import get


def number_of_subscribers(subreddit):
    """
    gets the total number of subscribers
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')
    except Exception:
        return 0
