#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    people = json.loads(requests.get(url + 'users').text)

    data = {}

    for employee in people:
        url_string = url + 'todos/?userId=' + str(employee['id'])
        all_tasks = json.loads(requests.get(url_string).text)
        tasks = []
        for task in all_tasks:
            tmp = {'task': task['title'],
                   'completed': task['completed'],
                   'username': employee['username']}
            tasks.append(tmp)
        data[employee['id']] = tasks

    with open("todo_all_people.json", "w") as outfile:
        json.dump(data, outfile)
