# Distance Calculator

Calculates the total distance given a csv of origins and one destination

## Running program
Install dependencies
```
pip install geopy
pip install -U googlemaps
```

Run program
```
python3 distance-calculator.py
```

You'll be prompted for the following
```
Enter destination to calculate distance to: <PLACE_QUERY>
Enter file location to CSV: <LOCATION_TO_CSV>
Enter the Google Maps API key: <GOOGLE_MAPS_API_KEY>
```

CSV should be in this format: `"current_city","count"`

You'll see the following output similar to this when running
```
Adding distance from <LOCATION>, <DISTANCE_IN_KM> (x<COUNT>)
Adding distance from <LOCATION>, <DISTANCE_IN_KM> (x<COUNT>)
Adding distance from <LOCATION>, <DISTANCE_IN_KM> (x<COUNT>)
...
Total Distance: <DISTANCE_IN_KM>
```