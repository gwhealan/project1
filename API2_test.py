from API2 import APIAccessor

dataProccesser = APIAccessor("b6d494f2bc814deba53ee27461307703", '4.1')
folder = ""


# helpers
def checkPath(address):
    if address[1:2] == ":\\":
        path = address
    else:
        path = folder + address
    return path


# Testers
def test_AccessCode(inpt):
    print("testing access code...", end='\t')
    # Get input
    key = inpt[1]
    if inpt[2][0].lower() != "t" and inpt[2][0].lower() != "f":
        print(f"\n\tError, result must be either \'t,\' \'f,\' \'T,\' \'F\'. Not \'{inpt[2]}\'")
        return False  # error
    result = inpt[2][0].lower() == 't'
    # Test
    error = False

    try:
        APIAccessor(key, '4.1')
    except Exception:
        error = True
    # Result
    if error != result:  # XOR, Only true of error false and test true or reverse
        print('SUCCESS')
    else:
        print('FAILURE')
    return True  # XOR, Only true of error false and test true or reverse


def test_RG(inpt):
    # Proccess input
    print("testing Reverse Geocoder...", end='\t')
    path = checkPath(inpt[1])
    try:
        tmp = open(path)
        if not inpt[1].endswith('.gpx'):
            print("\n\tError: File is not GPX format.")
            return False
    except BaseException as err:
        print("\n\tError: GPX file could not be found")
        print(f"\'{err}\'")
        return False
    tmp.close()
    # Run Test
    result = dataProccesser.getRouteAddresses(path)
    for point in result:
        print(f"{point['StreetAddress']} {point['City']}, {point['State']}")
    return True


def quiter(inpt=None):
    return False


# Main
def main():
    line = "+----------------------------------------------+"
    string = "Data Processer Testing"
    padding = " " * ((len(line) - len(string) - 2) // 2)
    print(line)
    print(f"|{padding}{string}{padding}|")
    print(line)
    while True:
        ret = input("Enter test file (enter nothing to quit):")
        try:
            file = open(ret, "r")
            global folder
            for i in range(len(ret), 0, -1):
                if ret[i - 1] == '/' or ret[i - 1] == '\\':
                    folder = ret[0:i]
            break
        except FileNotFoundError:
            if ret.lower() == "":
                return
            print("Could not open file.")
    switch = {  # Add new test functions here
        "testCreate": test_AccessCode,
        "testReverseGeocoder": test_RG,
        "quit": quiter
    }
    while True:
        inpt = file.readline().strip(' \t\n')
        print(inpt)
        if len(inpt) == 0:
            break
        parsed = inpt.split(' ')
        func = switch[parsed[0]]
        if type(func) is None:
            print(f"\tError: \'{parsed[0]}\' is not a valid command")
            break
        if not func(parsed):
            break
    return


if __name__ == "__main__":
    main()
