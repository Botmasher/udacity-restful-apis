# Securing Your API

## 1. Lesson 4 Intro
- security concerns for RESTful endpoints
- implement features for authentication and authorization from endpoints
- start by helping a few small businesses secure their web APIs

## 2. Adding Users and Logins
- concept of "user" for security and custom info
- not storing password but storing hash of user password
	- map digital data of arbitrary size to fixed-size digital data
	- one-way functions to generate hash from pwd but not the other way around
	- deterministic
	- hard to decode if compromised
- starter code https://github.com/udacity/APIs/tree/master/Lesson_4/02_Adding%20Users%20and%20Logins
1. use `passlib` like this: `from passlib.apps import custom_app_context as pwd_context`
	- `custom_app_context` is easy and based on SHA256
2. now add two new methods to `User` model:
	- `hash_password` that sets `self.password_hash` to the result of `.encrypt(password)`
		- called whenever user registers or changes password
	- `verify_password` that checks a plain password against the hash with `.verify(password, self.password)`
		- called whenever user provides credentials to be validated 
- see example code in `models.py` for lesson 4, section 2

## 3. User Registration
- make a `views.py` since the user model is in place
1. structure an endpoint so that client can post to `/users`
	- request body should be a JSON object with username and pwd
2. define the `new_user` function
	- `request.json.get()` and store the username and password in variables
	- check if they are None and `abort(400)`
	- check if the username already exists and `abort(400)`
	- create new `user = User(username=username)`
	- hash the password with `user.hash_password(password)`
	- add and commit the session changes
	- return the jsonified username and `201`
3. check to see that server responds with new user created (`HTTP/1.1 201 CREATED`)
4. note how this should be handled in live app
	- login done over a *secure* HTTPS connection
	- login in plain text is easy for a hacker to see over network
	- check out Udacity courses on security

## 4. Password Protecting a Resource
- users can now log in, but how to protect the resources they have access to?
- assume there's a resource at `/protected_resource` only made available to registered users
1. import Flask auth: `from flask_httpauth import HTTPBasicAuth`
	- basic authentication for Flask routes
	- protects endpoints decorated with `@auth.login_required`
2. give the basic auth more info to know how to validate user credentials
	- use the `@auth.verify_password` decorator and write a `verify_password` function
	- the function takes a username and password
	- the function filters for the specific user
	- the function returns `False` if there is no user or if the password does not verify
	- the function sets `g.user = user` and returns `True`
3. check what happens if you use incorrect vs correct username and password
- see the resulting updates to `views.py` in section 04 of the exercises

## 5. Quiz: Mom & Pop's Bagel Shop
- starter code for their bagel shop API
	- the `/bagels` route exposes all bagels in inventory
	- only their registered members can view this
1. help them add users to their models
	- securely store username and hashed password
2. add route for users to register
	- user makes a post request to `/users`
3. protect the bagels inventory endpoint
	- only members can view
4. use the Python tester to check that your code works

## 6. Token Based Authentication
- 
