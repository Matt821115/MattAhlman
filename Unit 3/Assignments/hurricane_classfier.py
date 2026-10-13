#   hurricane classification
'''
Tropical Storm < 74 MPH
Category 1 < 96 MPH
Category 2 < 111 MPH
Category 3 < 130 MPH
Category 4 < 157 MPH
Category 5 >= 157 MPH
'''

def wind_speed_input():
    global wind_speed 
    wind_speed = input("What is the storm windspeed in MPH?\nMPH=")
    try:
        wind_speed = float(wind_speed)
        if wind_speed < 74:
            print("Tropical Storm")
        elif wind_speed < 96:
            print("Category 1")
        elif wind_speed < 111:
            print("Category 2")
        elif wind_speed < 130:
            print("Category 3")
        elif wind_speed < 157:
            print("Category 4")
        elif wind_speed >= 157:
            print("Category 5")
        else:
            print("INVALID ANSWER")
    except:
        print("INVALID INPUT")
        wind_speed_input()

wind_speed_input()