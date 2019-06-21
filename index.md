# Welcome to BBSNHU's CS499 Capstone Page

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
### Algorithms and Data Structures
### Databases