import httplib2
import json

def getGeocodeLocation(inputString):
	google_api_key = "AIzaSyBaNcLWDGKiY2mOz1-V4z9sSaHcqNKZSwk" 	# not safe for live code
	address = inputString.replace(" ", "+")
	url = ("https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, google_api_key))
	h = httplib2.Http()
	response, body = h.request(url, "GET")
	result = json.loads(body)
	latitude = result['results'][0]['geometry']['location']['lat']
	longitude = result['results'][0]['geometry']['location']['lng']
	return (latitude, longitude)
