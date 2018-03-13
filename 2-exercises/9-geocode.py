import httplib2
import json

def getGeocodeLocation(inputString):
	# section 9
	google_api_key = "YOUR_API_KEY" 	# not safe for live code
	address = inputString.replace(" ", "+")
	url = ("https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, google_api_key))
	h = httplib2.Http()
	response, body = h.request(url, "GET")
	result = json.loads(body)
	# section 10
	latitude = result['results'][0]['geometry']['location']['lat']
	longitude = result['results'][0]['geometry']['location']['lng']
	return (latitude, longitude)

print(getGeocodeLocation("Anytown, USA"))
	