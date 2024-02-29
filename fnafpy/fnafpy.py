# fnaf inspired game, going onto arduino hopefully
# import
import os
# define initial conditions
power = 100
time = 0
running = [True,True]
left_door_closed = False
right_door_closed = False
# in the works
power_const = 0.5
time_const = 1
# ■ □
class robot(): # robot class
    def __init__(self,route,speed,name): # initialization
        # functional
        self.route = route # list
        self.speed = speed # value from 1 to 20
        # cosmetic
        self.name = name


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



def end(running): # end code
    if running[1]: # if win
        print("You Win! Yay!")
    else: # if lose
        print("You Died! Better Luck Next Time!")

while running[0]: # main loop
    # define current iteration power drain
    power_usage = power_const
    if left_door_closed:
        power_usage += power_const
    if right_door_closed:
        power_usage += power_const
    power -= power_usage
    # travel through time
    time += time_const
    # show time and power
    print(getHour(time),powerBar(power))
    # show door status
    doorStatus(left_door_closed,right_door_closed)
    # find out if game is over (won or lost)
    if power <= 0: # if out of power
        running = [False,False]
    if time >= 60: # if made to 6am
        running = [False,True]
    if running[0]: # open or close doors with 'a' and 'd'
        action = input()
    else:
        action = ""
    if "a" in action:
        left_door_closed = not(left_door_closed)
    if "d" in action:
        right_door_closed = not(right_door_closed)
    os.system('cls')
end(running)
input()