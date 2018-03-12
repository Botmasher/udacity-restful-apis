# GET https://api.foursquare.com/v2/venues/search?query=&category=CAT_ID1,+CAT_ID_N&near=City,+STATE
#
# Pizza near Mountain View, California
# Category: 4bf58dd8d48988d1ca941735, LatLong: (37.392971, -122.076044)
curl -l "https://api.foursquare.com/v2/venues/search?oauth_token=ECJVGNY0HGQAEUZEIMZL1VR3ST3DRSGHE15DO0TNW3QM2OAH&v=20180311&query=pizza&near=Mountain+View,+CA"
# Sushi near Miami, Florida
# Category: 4bf58dd8d48988d1d2941735, LatLong: (25.773822, -80.237947)
curl -l "https://api.foursquare.com/v2/venues/search?oauth_token=ECJVGNY0HGQAEUZEIMZL1VR3ST3DRSGHE15DO0TNW3QM2OAH&v=20180311&query=sushi&near=Miami,+FL"
# Donuts near Washington, DC 
# Category: 4bf58dd8d48988d148941735, LatLong: (38.897478, -77.000147)
curl -l "https://api.foursquare.com/v2/venues/search?oauth_token=ECJVGNY0HGQAEUZEIMZL1VR3ST3DRSGHE15DO0TNW3QM2OAH&v=20180311&query=donuts&near=Washington,+DC"
# Salad near New York, New York
# Category: 4bf58dd8d48988d1bd941735, LatLong: (40.768349, -73.96575)
curl -l "https://api.foursquare.com/v2/venues/search?oauth_token=ECJVGNY0HGQAEUZEIMZL1VR3ST3DRSGHE15DO0TNW3QM2OAH&v=20180311&query=salad&near=New+York,+NY"

exit 0
