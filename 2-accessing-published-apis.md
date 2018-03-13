# Lesson 2: Accessing Published APIs

## 1. Lesson 2 Intro
- explore APIs of popular apps
- explore documentation for APIs
- test APIs in your Python app

## 2. Parts of an HTTP Request
- first understand the components of the client-server HTTP flow
- HTTP as "pull protocol"
	- comm initiated by client
	- HTTP request sent to server
	- server responds with message
	- messages as bodies of text for machine to interpret
		- as actions
		- as images
		- as multimedia content
- components of HTTP request
	1. message header
		- first line is the "request line": HTTP verb + URI + HTTP version
		- optional request headers in name: value, name: value, ... pairs
	2. blank line between
	3. message body (optional)
		- additional info about request we want to send server
- look at example requests

## 3. HTTP Response
- breakdown of a response:
	1. header
		- starts with the "status line": HTTP version + status code + reason phrase
		- reason phrase explains status code in English
		- name: value pairs again for other optional headers
	2. blank line
	3. body (optional)
		- contains data requested by client
- web browser takes care of creating requests and rendering responses
- API devs at times do need to create and dissect messages

## 4. Sending API Requests with Postman and Curl
- browser conceals complexities
- dev needs to dig into requests and responses
- tools we can use to generate HTTP requests and view responses:
	- `curl -l` sends HTTP requests (though can transmit other protocols)
	- Postman is good for those preferring GUI (Chrome extension to build/view HTTP mssgs)
- choose a tool and get used to it; you'll need it for the exercises!
- cURL:
	- https://curl.haxx.se/docs/manpage.html
	- https://www.ethanmick.com/getting-started-with-curl/
- Postman:
	- https://www.getpostman.com/docs/v6/
- rec: know/research query strings to pass variables directly from the URI

## 5. Quiz: Sending API Requests
- CRUD to HTTP mapping for most use cases:
	- HTTP <--> CRUD
	- GET <--> READ
	- POST <--> CREATE
	- PUT <--> UPDATE/CREATE
	- PATCH <--> UPDATE
	- DELETE <--> DELETE
- run the small API server py file (stored as exercises 2 section 5)
- use cURL or Postman to send messages to the server
- Question: how does the server respond to the following requests?
	- GET localhost:5000/readHello
	- POST localhost:5000/createHello
	- PUT localhost:5000/updateHello
	- DELETE localhost:5000/deleteHello
- Answer: I got the printed response from `/readHello` but `Method Not Allowed` for the others

## 6. Searching for API Documentation
- accessing other APIs
- check out SoundCloud
	- how do they protect their resources?
	- how do they want devs to communicate with their API?
- create a client account
	- get Client ID
	- get Client Secret
- embed the above data in your request to get successful access to their API servers
- dig into SoundCloud's HTTP API Reference documentation
	- POST, PUT, DELETE methods mostly protected by access tokens
	- can build requests to view content though
- example API call
	- build playlist with new ID
	- add my Client ID in the URI query params
	- build and send using cURL or Postman
	- view successful response!
	- permalink response can be viewed in browser
- UPDATE: SoundCloud no longer accepts API signups

## 7. Quiz: Delving into APIs
- ok, stop watching instructor do it and do it yourself!
- work with API providers in the next two quizzes
- you'll also be able to leverage these code snippets in the final project
- Google Maps API
	- Geocoding API takes in string rep of loc
	- can use that to find lat/long coords
- Question: using cURL/Postman and the Geocoding API, what are the lat/long coords of these cities?
	- Tokyo, Japan
	- Jakarta, Indonesia
	- Maputo, Mozambique
	- Geneva, Switzerland
	- Los Angeles, California, USA

## 8. Quiz: Using the Foursquare API
- Foursquare gives search results tailored to user, places they visit, other users' advice, ...
- focuses on places to go near user
- use search feature to find restaurant using lat/long
- Question: using Geocoding and Foursquare API, what's a restaurant in a city for each meal type?
	- pizza in 37.392891, -122.076044
	- sushi in 25.773822, -80.237947
	- donuts in 38.897478, -77.000147
	- salad in 40.768349, -73.96575

## 9. Requesting from Python Code
- create requests and responses in Python for our app
- start with a simple py app that does geocoding called `geocode.py`
	1. import HTTP client library and library for serializing py objs in JSON: `httplib2` and `json`
	2. define `getGeocodeLocation(inputString)`
	3. create variable to store API key
	4. replace spaces in `inputString` with `"+"`
	5. build the URL to the API
	6. create an instance of `httplib2.Http()`
	7. use the instance to create a GET request and assign the returned array to `response, content`
	8. call `json.loads()` on the `content`
	9. return the formatted result
- now run Python from the terminal, import the function from your file and test it with a location!
- great! but how to parse through all the info in the response?

## 10. Parsing Your Response
- there seems to be NW, NE, SE, SW bounds for the map but then a central location for whole city
- storing the results in `city`, can access `city.keys()` -> `[u'status', u'results']`
- Question: dig into the `results` accounting for lists vs dicts, how do you get a city's longitude?
	- Answer: `your_data_var_name['results'][0]['geometry']['location']['lng']`
- now modify the geocoding function so it just returns longitude and latitude in a tuple

## 11. Quiz: Make Your Own API Mashup
- challenge to create own mashup using Google Maps Geocoding and Foursquare API data
- write `findARestaurant`
	- take a `mealType` and `location`
	1. geocode the location
	2. search for restaurants
	3. parse response and return one restaurant
	- returned value should be a dictionary with name, address and img URL
	- recommended to use the `browse` parameter when sending off Foursquare call
- intended to be tough!

## 12. Lesson 2 Wrap Up
- take time to explore other APIs like Wikipedia and StackExchange and whatnot
- read and study documentation
- next time create your own!
