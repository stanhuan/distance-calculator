import csv
import googlemaps
import geopy.distance

def main():
  DESTINATION = input("Enter destination to calculate distance to: ")
  CSV_FILE_LOCATION = input("Enter file location to CSV: ")
  total_distance = 0.0

  GOOGLE_MAPS_API_KEY = input("Enter the Google Maps API key: ")
  gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

  destination_result = gmaps.geocode(DESTINATION)
  destination_coord = (destination_result[0]['geometry']['location']['lat'], destination_result[0]['geometry']['location']['lng'])

  with open(CSV_FILE_LOCATION) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      if line_count == 0:
        line_count += 1
      else:
        distance = calculate_distance(destination_coord, row[1], row[0], gmaps)
        print("Adding distance from " + row[1] + ", " + str(distance) + " (x" + row[0] + ")")
        total_distance += distance
  
  print("Total Distance: " + str(total_distance))

def calculate_distance(destination_coord, origin, count, gmaps):
  origin_result = gmaps.geocode(origin)
  origin_coord = (origin_result[0]['geometry']['location']['lat'], origin_result[0]['geometry']['location']['lng'])
  return geopy.distance.vincenty(origin_coord, destination_coord).km * int(count)

if __name__== "__main__":
  main()
