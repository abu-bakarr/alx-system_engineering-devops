#!/usr/bin/python3
"""Gather data from an API"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    url_string = url + 'users/?id=' + user_id
    people = json.loads(requests.get(url_string).text)
    url_string = url + 'todos/?userId=' + user_id
    total_tasks = json.loads(requests.get(url_string).text)

    data_file = open(user_id + '.csv', 'w')
    csv_writer = csv.writer(data_file, quoting=csv.QUOTE_ALL)

    for task in total_tasks:
        row = []
        row.append(str(user_id))
        row.append(people[0]['username'])
        row.append(task['completed'])
        row.append(task['title'])
        csv_writer.writerow(row)
    data_file.close()
