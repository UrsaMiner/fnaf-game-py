# gameplay core functions
#import
import os
from visuals import *
from animatronics import *
def end(running): # end code
  if running[1]: # if win
    print("You Win! Yay!")
  else: # if lose
    print("You Died! Better Luck Next Time!")

def mainLoop(): # main program loop
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
