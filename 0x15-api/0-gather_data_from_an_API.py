#!/usr/bin/python3
"""  a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""

from os import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    name = (requests.get(f"{url}users/{sys.argv[1]}").json().get("name"))
    todos = (requests.get(f"{url}user/{sys.argv[1]}/todos").json())
    total_tasks = len(todos)
    done_tasks = []
    done = 0
    for task in todos:
        if task.get("completed"):
            done += 1
            done_tasks.append(task)
    print(f"Employee {name} is done with tasks({done}/{total_tasks}):")
    for item in done_tasks:
        print(f"\t {item['title']}")
