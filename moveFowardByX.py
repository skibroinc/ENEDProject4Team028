#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sound import *
import time

sound = Sound()
sound.speak('Welcome to team 0 2 8 E V 3 dev project!')

subTask = input("Which subtask (a,b): ")
tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)


if (subTask == "a"):
    n = int(input("Enter the number of iterations: "))
    distance = int(input("Enter the distance in cm: "))
    d = distance / 100 * 5.765

    for i in range(n):
        tank_drive.on_for_rotations(SpeedPercent(-34.95), SpeedPercent(-34.95), d) #foward
        time.sleep(.5)
        tank_drive.on_for_rotations(SpeedPercent(35), SpeedPercent(35), d * 1.01) #reverse
        time.sleep(.5)
elif (subTask == "b"):
    n = int(input("Enter the number of iterations: "))
    distance = int(input("Enter the distance in cm: "))
    d = distance / 100 * 5.765

    for i in range(n * 2):
        tank_drive.on_for_rotations(SpeedPercent(-34.95), SpeedPercent(-34.95), d) #foward
        time.sleep(.5)
        tank_drive.on_for_rotations(SpeedPercent(-17.5), SpeedPercent(17.5), .9) #turn
        time.sleep(.75)
        

