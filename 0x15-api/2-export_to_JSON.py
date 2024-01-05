#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
"""
import json
from sys import argv
import requests


def get_todo_list():
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"users/{argv[1]}"
    todo_endpoint = f"todos"
    user_url = f"{base_url}/{user_endpoint}"
    user_todo_url = f"{user_url}/{todo_endpoint}"
    user_id = argv[1]
    user = requests.get(user_url).json()
    todos = requests.get(user_todo_url).json()
    tasks = []
    for todo in todos:
        task = {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
                }
        tasks.append(task)

    with open(f"{user_id}.json", "w") as f:
        f.write(json.dumps({f"{user_id}": tasks}))


if __name__ == "__main__":
    get_todo_list()
