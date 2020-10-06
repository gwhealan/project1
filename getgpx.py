import gpxpy
gpx_file = open('09_27_20.gpx', 'r')
gpx = gpxpy.parse(gpx_file)

print(len(gpx.tracks))
print(len(gpx.tracks[0].segments))
print(len(gpx.tracks[0].segments[0].points))

data = gpx.tracks[0].segments[0].points
## Start Position
start = data[0]
## End Position
finish = data[-1]
print("Start %s, End %s", start, finish)