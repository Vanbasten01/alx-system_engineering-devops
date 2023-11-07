#!/usr/bin/python3
""" top_ten model """
import requests


def recurse(subreddit, hot_list=[], after=""):

    if not subreddit:
        return None
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {"User-Agent": "0x16. API advanced/Task0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        after = data.get('data', {}).get('after', '')
        if after == "":
            return hot_list
        posts = data.get('data', {}).get('children', [])
        if posts:
            for post in posts:
                hot_list.append(post.get('data').get('title'))
        return recurse(subreddit, hot_list, after)
