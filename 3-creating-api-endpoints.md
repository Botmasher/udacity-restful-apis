# Creating your own API Endpoints

## 1. Lesson 3 Intro
- we'll use Flask to build endpoints + backend + db
- check out the Flask documentation if you are unfamiliar
- (used in the Udacity FSF course, so try that if you want more exposure)

## 2. API Endpoints with Flask
- if you know Flask you know about the `@app.route` decorator
- that decorator helps render web pages or set up endpoints
- should also import `jsonify` to convert dicts into JSON objects
	- returns the Flask response object
	- that object already has the right headers
	- can be used with JSON responses
- next quiz: make basic API endpoints with Flask

## 3. Quiz: Making an Endpoint with Flask
- starter code saved to lesson 3 exercises Flask endpoints
- setting up a Flask web server about puppies
- server runs but app is missing the appropriate `@app.route` functions
- Can you get the endpoints to work?
	1. download [starter code](https://github.com/udacity/APIs/tree/master/Lesson_3/03_Making%20an%20Endpoint%20with%20Flask/Starter%20Code)
	2. create `@app.route` functions
	3. run the server
	4. run the Python test

## 4. Quiz: Respond to the Different Kinds of Requests
- by default `@app.route` responds to `methods=['GET']`
- now add POST, PUT and DELETE methods
- starter code saved to lesson 3 exercises section 4
- (the file takes some wrangling to work with `python3`)
- (also, you will need to import Flask `requests` and note that)

## 5. Quiz: Serializing Data from the Database
- starter code saved to lesson 3 exercises section 5
- the endpoints work, so it's time to add a db
- the `models.py` contains the db configuration
- now the project code is refactored to use SQLAlchemy
	- runs the CRUD operations
	- uses a puppies.db file 
- please add a serialized decorator to the models
- then run your server
- and run the Python tester

## 6. Quiz: Adding Features to your Mashup
- starter code saved to lesson 3 exercises section 6
- put everything together into one app
- not the puppies, the menu stuff again
- meal or restaurant finder mashup that:
	1. takes a city and meal type
	2. geocodes the loc
	3. finds nearby restaurant with that meal type
	4. stores restaurant in a db
	5. returns restaurant JSON object to user
- exercise process including changes you will need to make:
	1. `views.py` endpoint `/restaurants` handle returning all restaurants in db
		- name, id, address and img
	2. `views.py` endpoint `/restaurants/<int:id>` returns same info for just one restaurant
		- an update to this endpoint should update any of that info
		- a delete to this endpoint should remove that info from the db
	3. `findARestaurant.py` needs updated with your client ID and secret
	4. use Python tester to check your endpoints

## 7. Lesson 3 Wrap Up
- next time you'll add security to your endpoints
- implement token-based authentication
- rate limiting
- next time!
