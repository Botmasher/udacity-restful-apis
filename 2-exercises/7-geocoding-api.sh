uri="maps.googleapis.com/maps/api/geocode/json"
addresses=("Tokyo,+Japan" "Jakarta,+Indonesia" "Maputo,+Mozambique" "Geneva,+Switzerland" "Los+Angeles,+California,+USA")
key="&key=YOUR_KEY_HERE"

for address in "${addresses[@]}"
	do
		echo "https://${uri}?address=${address}${key}"
		curl -l https://${uri}"?address="${address}${key}
	done
exit 0
