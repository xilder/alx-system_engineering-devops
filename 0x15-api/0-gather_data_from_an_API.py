#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
"""
import requests
from sys import argv


def get_todo_list():
    """
    prints some api data from a given website
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"users/{argv[1]}"
    todo_endpoint = f"todos"
    user_url = f"{base_url}/{user_endpoint}"
    user_todo_url = f"{user_url}/{todo_endpoint}"

    user = requests.get(user_url).json()
    todos = requests.get(user_todo_url).json()
    done = [x for x in todos if x["completed"] is True]
    print(f"Employee {user['name']} is done with " +
          f"tasks({len(done)}/{len(todos)}):")
    for todo in done:
        print(f"\t {todo['title']}")


if __name__ == "__main__":
    """
    runs programme
    """
    get_todo_list()
