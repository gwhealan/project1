import requests

#HOLA
#testing waters
#probando 


def get_name(lat, long, st, key):
    origen = "http://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/Rest/?lat=" + str(lat) + "&lon=" + str(long) + "&state=" + str(state) + "&apikey=" + key + "&format=json&notStore=false&version=4.10"
    answer = ""
    response = requests.get(origen).json()
    result = response['StreetAddresses'][0]['StreetAddress']#only gets the name of the avenue or street

    # remove the addres number, leaving only the street or avenue name.
    signal = 0
    for i in result:
        if i == ' ':#exeption if the name of the street has numbers i.e 19th avenue, Eugene
            signal = 1
        if i not in "0123456789" or signal == 1:#deletes the first numbers house. i.e. 1790 Alder St. is converted to Alder St.
            answer += i

    return answer[1:]

#here is where we enter the coordinates and state. Data for testing, this script could be import for main program
lat =   44.587662
long = -123.256691
state = "or"
#my personal key I got when I registered to the website.
key = "bf20a5bb85774b0c9e9b7b319c92040f"

print(get_name(lat, long, state, key))
