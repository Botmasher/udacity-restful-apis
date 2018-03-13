from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)

# Use these once you set up an app
#foursquare_client_id = "PASTE_YOUR_ID_HERE"
#foursquare_client_secret = "YOUR_SECRET_HERE"

def findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
	lat, lng = getGeocodeLocation(location)

	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
	foursquare_token = "ECJVGNY0HGQAEUZEIMZL1VR3ST3DRSGHE15DO0TNW3QM2OAH"
	foursquare_v = "20180312"
	foursquare_ll = "%s,%s" % (lat, lng)
	foursquare_url = "https://api.foursquare.com/v2/venues/explore?oauth_token=%s&v=%s&query=%s&ll=%s" % (foursquare_token, foursquare_v, mealType, foursquare_ll)
	h = httplib2.Http()
	response, body = h.request(foursquare_url, "GET")
	data = json.loads(body)
	
	if not data['response']['groups']:
		return None

	#3. Grab the first restaurant
	restaurant_name = data['response']['groups'][0]['items'][0]['venue']['name']
	restaurant_id = data['response']['groups'][0]['items'][0]['venue']['id']
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	img_size = "300x300"

	address =""
	for line in data['response']['groups'][0]['items'][0]['venue']['location']['formattedAddress']:
		address += ", %s" % line

	#5. Grab the first image
	try:
		img_src = data['response']['groups'][0]['items'][0]['venue']['photos']['groups'][0]['items']['prefix'] + img_size + data['response']['groups'][0]['items'][0]['venue']['photos']['groups'][0]['items']['suffix']
		#img_url = "https://api.foursquare.com/v2/venues/%s/photos?oauth_token=%s&v=%s" % (restaurant_id, foursquare_token, foursquare_v)
		#img_data = json.loads(h.request(img_url, "GET")[1])
	#6. If no image is available, insert default a image url
	except:
		img_src = "https://placebear.com/300/300"
		#img_data = json.loads(h.request(img_src, "GET"))
	#7. Return a dictionary containing the restaurant name, address, and image url
	restaurant = {'name': restaurant_name, 'id': restaurant_id, 'address': address, 'img': img_src}
	print (restaurant)
	return restaurant

if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney Australia")