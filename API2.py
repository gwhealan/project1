import requests
import xml.etree.ElementTree as ET


class APIAccessor:
    URL = "https://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/HTTP/default.aspx"
    Format = 'json'

    def __init__(self, apiKey, version):
        self.APIKey = apiKey
        self.Version = version
        #self.Storage = dict() <-- May not be necessary saving just in case
        # test if works
        if self.__concatCall(44.044248, -123.072729)['QueryStatusCode'] != 'Success':
            raise Exception("Cannot access GeoServicer, access code may be incorrect.")

    # formats and calls HTML call to geoservice
    def __concatCall(self, lat: float, lon: float, state=None, geom=None, includeHeader=None):
        call = APIAccessor.URL + "?apiKey=" + self.APIKey + "&version=" + self.Version + "&lat=" + str(
            lat) + "&lon=" + str(lon) + "&format=" + APIAccessor.Format + "&notStore=true"
        if state is not None:
            call += "&geom=" + state
        if geom is not None:
            call += "&geom=" + state
        if includeHeader is not None:
            call += "&includeHeader=" + includeHeader
        r = requests.get(call).json()
        return r

    # Public method to get a specific address
    def getAddress(self, lat: float, lon: float, state=None):
        # Make sure lat/lon are valid
        if not (-90.0 <= lat <= 90.0):
            raise ValueError(str(lat) + " is out of range (-90 to 90).")
        if not (-180.0 <= lon <= 180.0):
            raise ValueError(str(lon) + " is out of range (-180 to 180).")
        # check back Store                              +
        #if (lat, lon) in self.Storage:                 | May not be necessary
        #    address = self.Storage[(lat, lon)]         | Saving just in case
        #    return address                             |
        # get address                                   |
        #else:                                          |
        #    r = self.__concatCall(lat, lon, state)     |
        #    address = r['StreetAddresses'][0]          |
        #    self.Storage[(lat, lon)] = address         |
        #    return address                             +
        r = self.__concatCall(lat, lon, state)
        address = r['StreetAddresses'][0]
        self.Storage[(lat, lon)] = address
        return address

    #Public method to get all addresses from a gpx file
    def getRouteAddresses(self,
                          gpx_file: str):  # Slow. Must be reworked. Ideas: Multithreading, Mesh type loop (check every 4, if same street don't check inbetween).
        points = APIAccessor.ParseGPX(gpx_file)
        addresses = []
        state = ""
        firstPass = True
        for point in points:
            if firstPass:
                ret = self.getAddress(point[0], point[1])
                state = ret['State']
            else:
                ret = self.getAddress(point[0], point[1], state)
            addresses.append(ret)
        return addresses

    # parse the lat/lon points into an array of point pairs (lat, lon)
    @staticmethod
    def ParseGPX(filename):
        if not filename.endswith('.gpx'):
            raise Exception("File is not a gpx file")
        qname = '{http://www.topografix.com/GPX/1/1}'
        root = ET.parse(filename).getroot()  # XML parser
        try:
            path = root.find(qname + 'trk').find(qname + 'trkseg')
        except BaseException:
            raise Exception("File not readable, may not be a valid gpx file")
        points = []
        for point in path.findall(qname + 'trkpt'):
            points.append((float(point.attrib['lat']), float(point.attrib['lon'])))
        return points

    # TODO
    def distance(self):
        return

    # TODO
    @staticmethod
    def check_turn(addy1, addy2):
        return
