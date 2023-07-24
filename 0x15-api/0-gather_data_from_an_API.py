#!/usr/bin/python3

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
    sys.exit(1)

try:
    employee_id = int(sys.argv[1])
except ValueError:
    print("EMPLOYEE_ID must be an integer")
    sys.exit(1)

user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

try:
    user_response = requests.get(user_url)
    user_response.raise_for_status()
    user_data = user_response.json()
    employee_name = user_data['name']
except requests.exceptions.RequestException as e:
    print("Error getting user data: {}".format(e))
    sys.exit(1)
except KeyError:
    print("Error: Invalid user ID")
    sys.exit(1)

try:
    todo_response = requests.get(todo_url)
    todo_response.raise_for_status()
    todo_data = todo_response.json()
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task['completed']]
    num_done_tasks = len(done_tasks)
    task_titles = [task['title'] for task in done_tasks]
except requests.exceptions.RequestException as e:
    print("Error getting todo data: {}".format(e))
    sys.exit(1)

print("Employee {} is done with tasks({}/{}):".format(employee_name, num_done_tasks, total_tasks))
for title in task_titles:
    print("\t {}".format(title))