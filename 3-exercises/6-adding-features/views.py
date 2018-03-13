from findARestaurant import findARestaurant
from models import Base, Restaurant
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

#import sys
#import codecs
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)

#foursquare_client_id = ''

#foursquare_client_secret = ''

#google_api_key = ''

engine = create_engine('sqlite:///restaurants.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

@app.route('/restaurants', methods = ['GET', 'POST'])
def all_restaurants_handler():
	#YOUR CODE HERE
	if request.method == 'POST':
		# add one restaurant
		location = request.args.get("location", "")
		meal_type = request.args.get("mealType", "")
		restaurant_data = findARestaurant(meal_type, location)
		if restaurant_data is not None:
			restaurant = Restaurant(restaurant_name=restaurant_data['name'], restaurant_address=restaurant_data['address'], restaurant_image=restaurant_data['image'])
			session.add(restaurant)
			session.commit()
			return jsonify(restaurant=restaurant.serialize)
		else:
			return jsonify({'error': "No restaurants found for %s in %s" % (meal_type, location)})
	elif request.method == 'GET':
		# return all restaurants
		restaurants = session.query(Restaurant).all()
		return jsonify(restaurants=[i.serialize for i in restaurants])

@app.route('/restaurants/<int:id>', methods = ['GET','PUT', 'DELETE'])
def restaurant_handler(id):
	#YOUR CODE HERE
	restaurant = session.query(Restaurant).filter_by(id=id).one()
	if request.method == 'GET':
		return jsonify(restaurant=restaurant.serialize)
	elif request.method == 'PUT':
		name = request.args.get('name')
		address = request.args.get('address')
		image = request.args.get('image')
		if name: restaurant.restaurant_name = name
		if address: restaurant.restaurant_address = address
		if image: restaurant.restaurant_image = image
		session.commit()
		return jsonify(restaurant=restaurant.serialize)
	elif request.method == 'DELETE':
		session.delete(restaurant)
		session.commit()
		return jsonify({'message': "Restaurant deleted"})

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
