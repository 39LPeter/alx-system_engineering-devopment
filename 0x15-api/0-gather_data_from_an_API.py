#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
'''imports the requests module to handle HTTP requests'''
"""sys module to access command-line arguments."""
import requests
import sys
"""ensures that the code within this block is only executed if the script is run directly, not when it is imported as a module."""

if __name__ == "__main__":
    """This sets the base URL for the API endpoints used in the script. jsonplaceholder.typicode.com is a free online REST API that you can use for testing and prototyping."""
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
