#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {"limit": 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    response = requests.get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        data = results.get('data').get('children')
        for i in my_data:
            print(i.get('data').get('title'))
    except Exception:
        print("None")
