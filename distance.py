import math
#calculates distance between two points using the harvestein formula for spheric shapes.

#janeth smith house
inicio_lat =  44.040125#degrees in deciamls
inicio_lon = -123.080226

#7-11
final_lat =  44.045421
final_lon = -123.080192

def distance( ini_lat, fin_lat, ini_lon, fin_lon):
	dif_lat = math.radians(inicio_lat - final_lat)
	# print(dif_lat)
	dif_lon = math.radians(inicio_lon - final_lon)
	# print(dif_lon)

	earth_radio = 6371#in km

	#harversine formula to calculate distance from to points
	distance = (math.sin(dif_lat/2))**2 + math.cos(inicio_lat) * math.cos(final_lat) * (math.sin(dif_lon/2))**2
	c = 2 * math.asin(math.sqrt(distance))

	distancia = earth_radio * c * 1000#distance in meters


	return distancia#by 1000 to get it in kilometers.

print(distance(inicio_lat,final_lat,inicio_lon,final_lon))