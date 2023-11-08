import requests
"""  a recursive function that queries the Reddit API, parses
the title of all hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces. Javascript
should count as javascript, but java should not)."""


def count_words(subreddit, word_list, after="", counts=None):
    """ """
    if not subreddit:
        return None

    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {"User-Agent": "0x16. API advanced/Task0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return counts

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        title = post.get('data', {}).get('title', "").lower()
        for keyword in word_list:
            keyword = keyword.lower()
            if f' {keyword} ' in f' {title} ':
                counts[keyword] = counts.get(keyword, 0) + 1
    next_page = data.get('data', {}).get('after')
    if next_page:
        return count_words(subreddit, word_list,
                           after=next_page, counts=counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print(f"{keyword}: {count}")
