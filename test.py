from distance import distance
from directions import get_name
#two points,
#janeth smith house
inicio_lat =  44.040125#degrees in decimals
inicio_lon = -123.080226

#7-11
final_lat =  44.045421
final_lon = -123.080192

#test 2
# inicio_lat =   44.032259#degrees in decimals
# inicio_lon = -123.080378
# final_lat =   44.028837
# final_lon = -123.080349

#test 3
# inicio_lat = 44.038997#degrees in decimals
# inicio_lon = -123.086235
# final_lat =  44.038962
# final_lon = -123.077736
print ("{:.2f} meters".format(distance(inicio_lat, inicio_lon, final_lat, final_lon)))


#here is where we enter the coordinates and state. Data for testing, this script could be import for main program
lat =   44.040125
long = -123.080226
state = "or"
#my personal key I got when I registered to the website.
key = "bf20a5bb85774b0c9e9b7b319c92040f"

# print(get_name(lat, long, state, key))
