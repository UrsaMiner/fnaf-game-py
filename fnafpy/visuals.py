# visuals (what is shown to the player)
def powerBar(power): # return power bar in squares (1 square represents 20% (rounded))
    temp_power = power - 10
    no_squares = temp_power // 20
    squares = ""
    for i in range(5):
        if len(squares) <= no_squares:
            squares += "■"
        else:
            squares += "□"
    return squares



def openOrClosed(boolean): # converts True or False to "Closed" or "Open"
    if boolean:
        return "Closed"
    else:
        return "Open"

def doorStatus(left_door_closed,right_door_closed): # outputs the status of both the left and right doors
    string = "Left Door Status: "
    string += openOrClosed(left_door_closed)
    string += "\nRight Door Status: "
    string += openOrClosed(right_door_closed)
    print(string)



def getHour(time): # returns hour in readable format (e.g. 05:00am)
    hour = time // 10
    hour = "0"+str(hour)+":00am"
    return hour
