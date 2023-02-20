#!/usr/bin/env python3
from ev3dev2.motor import *
def motor():
    def asdfs():
        #sets speed to the inputted percent of the motor’s max speed
        SpeedPercent(50)
        #sets speed in rotations per second 
        SpeedRPS(.5)
        #sets speed in rotations per minute 
        SpeedRPM(20)
        #sets speed in degrees per second
        SpeedDPS(5)
        #sets speed in degrees per min
        SpeedDPM(500)
        #Addresses for the motor ports on the EV3 Brick 
        OUTPUT_A
        OUTPUT_B
        OUTPUT_C
        OUTPUT_D

    #run a single motor
    def singleMotor():
        m = LargeMotor(OUTPUT_A)
        m.on_for_rotations(SpeedPercent(75), 5)

    #two motors
    def twoMotors():
        tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

        # drive in a turn for 5 rotations of the outer motor
        # the first two parameters can be unit classes or percentages.
        tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(75), 10)

        # drive in a different turn for 3 seconds
        tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(30), 3)
        

from ev3dev2.sound import *
def speek():
    sound = Sound()
    sound.speak('Welcome to the E V 3 dev project!')

