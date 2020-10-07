from math import cos, sin, asin, radians, sqrt
#calculates distance between two points using the harvestein formula for spheric shapes.
def distance(ini_lat, ini_lon, fin_lat, fin_lon):

	dif_lat = radians(ini_lat) - radians(fin_lat)
	dif_lon = radians(ini_lon) - radians(fin_lon)
	earth_radio = 6371 #radius in km
	distance = (sin(dif_lat/2))**2 + cos(radians(ini_lat)) * cos(radians(fin_lat)) * (sin(dif_lon/2))**2
	distancia = earth_radio * asin(sqrt(distance)) * 2 * 1000 # multiply by 1000 to convert to 	distance in meters

	return distancia
