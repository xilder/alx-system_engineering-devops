#!/usr/bin/python3
"""
gets the total number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    gets the total number of subscribers
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    user_agent = {"User-Agent": "My-User-Agent"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    if response.status_code >= 300:
        return 0
    else:
        data = response.json()
        return data["data"]["subscribers"]
