#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
"""
import json
from sys import argv
import requests


def get_todo_list():
    base_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(base_url).json()
    all_info = {}
    for user in users:
        todos = requests.get(f"{base_url}/{user['id']}/todos").json()
        tasks = []
        for todo in todos:
            task = {
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": user["username"]
                    }
            tasks.append(task)
        all_info[user['id']] = tasks

    with open(f"todo_all_employees.json", "w") as f:
        f.write(json.dumps(all_info))


if __name__ == "__main__":
    get_todo_list()
