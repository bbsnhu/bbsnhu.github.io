## Welcome to BBSNHU's CS499 Capstone Page
## **Repository:**
### [Link to project folder on GitHub.](https://github.com/bbsnhu/bbsnhu.github.io/tree/master/Final)
## Reflection
## Initial Artifacts
### Software Design and Engineering
- Artifact Name: Zoo Authentication System
- Origin: Foundation in Application Development
- Category: Transfer a project into a different language

For this category I want to transfer this program into Python.  I also want to add protection for invalid usernames and possibly the creation of new users.  I am also thinking about using the MongoDB (cat 3) as storage for the user names instead of a local file.  Pseudocode is below:

```
Function authSystemZoo():
	DECLARE variables
	CREATE loop for three login attempts
		EXIT if three failed attempts
		PROMPT user for username
			SAVE to variable
		PROMPT user for password
			SAVE to variable
		CONVERT password to MD5 hash
			SAVE MD5 hash to variable
		OPEN credentials.txt
		COMPARE username and MD5 hash to credential file
		GET user’s role
		OPEN associated user’s role file
		PRINT associated user’s role file contents
			ALLOW user logout
				LOOP to login prompt
				ALLOW user to quit program
```
### Algorithms and Data Structures
- Artifact Name: Data Structures and Algorithms Final Project
- Origin: CS 260: Data Structures and Algorithms
- Category: Expand complexity

For this category I want to use search and sort of various types in Python (instead of C++) using a document handling framework to search and sort from a local document.  Here I will be using a data source file to illustrate advanced search/sort methods and capabilities.

![alt text](http://bbsnhu.github.io/Images/Flowchart2.png "Logo Title Text 1")

### Databases
In this category I will use MongoDB as persistent storage for my program.  Here I hope to add the functionality of adding results from previous categories as well as using the database for user management.


```
CREATE Mongo Client
CREATE DB and Collection
CREATE index for username lookup (possibly others depending on DS and algs used.)
	CATCH errors
```

## Finished Artifacts
### Software Design and Engineering
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import (Built-Ins)
from os import system, name
import hashlib
import random
import sys
import time
from bson import json_util
import json
import pymongo
import pprint

# Import (Custom)
from resources.quicksort import partition, quickSort
from resources.bubble import bubbleSort
from resources.pystack import PyStack
from resources.pyqueue import PyQueue


# Meta
__author__ = "Bryan Bagley"
__version__ = "0.1.0"
__license__ = "MIT"
__email__ = "bryan.bagley@snhu.edu"
__status__ = "Development"

# Globals
userNamePrompt = "Please enter your Username: "
userPassPrompt = "Please enter your Password: "
credFile = "credentials.txt"
elementCount = 1000
myDocument = {}
userAuthenticated = False

# Mongo Init
client = pymongo.MongoClient('localhost', 27017, serverSelectionTimeoutMS=1000)
db = client['CS499']
collection = db['Senators']

# PPrint Init
pp = pprint.PrettyPrinter(indent=4)


def addUser(u, p):
    """Adds a new user to credentials.txt file
    Arguments: u = User Name, p = Password (Required)
    Returns: Bool status if user was added
    """
    userFound = False
    # Check if user already exists in credFile
    try:
        with open(credFile) as f:
            credentials = [x.strip().split(':', 1) for x in f]
            f.close()

    except Exception as ex:
        print("Error with credentials.txt file.  More info: ", ex)

    for userName, _ in credentials:
        if u.lower() == userName:
            userFound = True
            print("User Already Exists!")
            f.close()
            return False

    # If user is not found, add it (formating locally)
    if userFound is False:
        try:
            with open(credFile, 'a') as f:
                f.write("\n%s:%s" % (u.lower(), hashIt(p)))
                print("User %s added!" % u.capitalize())
                return True
        except Exception as ex:
            print("Error with credentials.txt file. More info:", ex)
        finally:
            f.close()


def authenticate(u, p):
    """
    Authentication function
    Input: u = username (string), p = password (string)
    Returns: True if user is found, False if not
    """
    try:
        with open(credFile) as f:
            credentials = dict([x.strip().split(':', 1) for x in f])
    except Exception as ex:
        print("Error with credentials.txt file.  More info: ", ex)
    finally:
        f.close()

    if u.lower() in credentials and p == credentials[u.lower()]:
        print("Authentication Success")
        return True


def getLoginInfo():
    """Prompts user for authentication information"""
    print("")
    print("")
    userName = (str(input(userNamePrompt)))
    userPassP = (str(input(userPassPrompt)))
    userPassE = hashIt(userPassP)
    return (userName, userPassE)


def welcomeMessage():
    print(r"""
             __        __   _                          _
             \ \      / /__| | ___ ___  _ __ ___   ___| |
              \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
               \ V  V /  __/ | (_| (_) | | | | | |  __/_|
                \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)
    """)


def displayMenu(u):
    """Menu driver"""
    print("")
    print("")
    print("Welcome,", u.capitalize())
    print("---------------------------------")
    print("********** MAIN MENU ************")
    print("---------------------------------")
    print("")
    print("----- Data Structure Tests ------")
    print("1. Stack Test")
    print("2. Queue Test")
    print("-------- Algorithm Tests --------")
    print("3. Bubble Sort Test")
    print("4. Quick Sort Test")
    print("----------Database Tests---------")
    print("5. Display From DB")
    print("6. Agg Pipe Test From DB")
    print("7. (NYI) Amazing Mongo Thing")
    print("---------------------------------")
    print("8. Add User")
    print("9. Logout")
    print("0. Exit")
    print("")
    print("")
    return input("Please make a selection: ")


def clear():
    """Clear console - platform independent"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def hashIt(i):
    """
    Hash function
    Input: password (Plain text - String)
    Output: Hashed password (MD5 - String)
    """
    return str(hashlib.md5(i.encode()).hexdigest())


def makeAList(n, intRange=1000):
    """
    Returns a 'n' element list of ints random 1-1000
    intRage param (optional - default 1000) maximum element value
    """
    # TODO: add return Strings as element type
    return [random.randint(1, intRange) for _ in range(0, n)]


def main():
    welcomeMessage()

    try:
        userAuthenticated = False
        loginCount = 0

        while loginCount < 3 and not userAuthenticated:
            loginUser, loginPassE = getLoginInfo()
            userAuthenticated = authenticate(loginUser, loginPassE)

            while userAuthenticated:

                selection = displayMenu(loginUser)

                # Check selection is valid against master list
                if selection not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    print("Invalid Selection, Try Again.")

                # TODO: SELECTIONS 1-4 (DS AND ALG)
                if selection == '1':  # STACK OPTION
                    myList = ["apple", "grapes", "banana", "pineapple"]
                    print("")
                    print("____STACK TEST - LIFO____")
                    print("")
                    print("Test List:", myList)
                    print("")
                    print("Creating New Stack object..")
                    myStack = PyStack(myList)
                    print("Done..")
                    print("")
                    print("Pushing 'Coconut' to Stack..")
                    myStack.push("Coconut")
                    print("Done..")
                    print("")
                    print("Requesting Pop..")
                    myStack.pop()

                if selection == '2':  # QUEUE OPTION
                    # TODO: FIX THIS MESS
                    myList = ["apple", "grapes", "banana", "pineapple"]
                    print("")
                    print("____QUEUE TEST - FIFO____")
                    print("Test List:", myList)
                    print("")
                    print("Creating New Queue object..")
                    myQueue = PyQueue(myList)
                    print("Done..")
                    print("")
                    print("Pushing 'Coconut' to Queue..")
                    myQueue.enqueue("Coconut")
                    print("Done..")
                    print("")
                    print("Requesting Pop..")
                    myQueue.dequeue()

                if selection == '3':  # BUBBLE
                    print("")
                    print("Creating List..")
                    myList = makeAList(elementCount)
                    print(myList)
                    print("")
                    print("Bubble Sorting List..")
                    print("")
                    # TODO: Make stopwatch a decorator
                    start_time = time.time()
                    print(bubbleSort(myList))
                    end_time = time.time()
                    print("")
                    print("Completed in %g seconds" % (end_time - start_time))

                if selection == '4':  # QUICKSORT
                    print("")
                    print("Creating List..")
                    myList = makeAList(elementCount)
                    print(myList)
                    print("")
                    print("QuickSorting..")
                    print("")
                    start_time = time.time()
                    quickSort(myList, 0, len(myList) - 1)
                    end_time = time.time()
                    print(myList)
                    print("")
                    print("Completed in %g seconds" % (end_time - start_time))
                    print("")

                if selection == '5':  # TODO: DB DISPLAY
                    document = collection.find_one()
                    print(json.dumps(document, indent=4,
                                     default=json_util.default))

                if selection == '6':  # TODO: DB AGG PIPE
                    pipeSearch = [
                        {"$project": {
                            "_id": 0,
                            "last_name": 1,
                            "first_name": 1,
                            "party": 1,
                            "state_name": 1
                        }
                        }
                    ]
                    results = list(collection.aggregate(pipeSearch))
                    print(json.dumps(results, indent=4, default=json_util.default))

                if selection == '7':  # TODO: Make something amazing
                    pass

                if selection == '8':  # ADD USER
                    print("** Add New User **")
                    newName = input("Enter NEW Username: ")
                    newPass = input(
                        "Enter NEW password for {}").format(newName)
                    addUser(newName, newPass)

                if selection == '9':  # LOGOUT
                    print("Logged out, returning to Main Menu..")
                    main()

                if selection == '0':  # EXIT
                    userAuthenticated = False
                    loginCount = 0
                    print("\nBye!")
                    sys.exit(0)

            else:
                print("Authentication Error")
                loginCount += 1
                if loginCount < 3:
                    print("Please Try Again.")

                else:
                    print("Exiting...")
                    sys.exit(0)

    except KeyboardInterrupt:
        print("\nKeyboard Interrupt Detected, Closing.")


if __name__ == "__main__":
    # app.run(port="8080", debug=True)
    main()
```

### Algorithms and Data Structures
### Bubbly.py
```python
def bubbleSort(list):
    i = len(list)

    for j in range(i):

        for k in range(0, i-j-1):
            if list[k] > list[k+1]:
                list[k], list[k+1] = list[k+1], list[k]

    return list
```
### Quicksort.py
```python
def partition(list, low, high):
    i = (low-1)
    pivot = list[high]
    for j in range(low, high):
        if list[j] <= pivot:
            i = i+1
            list[i], list[j] = list[j], list[i]

    list[i+1], list[high] = list[high], list[i+1]
    return (i+1)


def quickSort(list, low, high):
    if low < high:
        part = partition(list, low, high)
        # Recursively calls itself to continue
        # partitioning
        quickSort(list, low, part-1)
        quickSort(list, part+1, high)
```
### PyStack.py
```python
class PyStack():

    def __init__(self, list):
        self.__stack = []
        for value in list:
            self.__stack.append(value)

    def push(self, value):
        self.__stack.append(value)
        print(self.__stack)

    def pop(self):
        if len(self.__stack) > 0:
            index = len(self.__stack) - 1
            print("Pop Requested..")
            print("Popping", self.__stack[index])
            a = self.__stack.pop(index)
            print(self.__stack)
            return a
        else:
            print("Stack is empty.")
            return False
```
### PyQueue.py
```python
class PyQueue():

    def __init__(self, list):
        self.__queue = []
        for value in list:
            self.__queue.append(value)

    def enqueue(self, value):
        print("Adding " + str(value))
        self.__queue.append(value)
        print(self.__queue)

    def dequeue(self):
        if len(self.__queue) > 0:
            print("Removing " + str(self.__queue[0]))
            a = self.__queue.pop(0)
            print(self.__queue)
            return a
        else:
            print("Queue is empty.")
            return False
```