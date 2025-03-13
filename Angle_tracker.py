"""Angle_tracker.py
Author: Caleb Leonard
Date: 03/02/2025"""
#This program was created to help understand how to keep track of numerical values within set bounds, in this case 0 and 180.
#The Idea is to limit motor rotation to 0 degrees and 180 degrees.

#values to initialize
Angle=0
CurrentAngle=0
ErrAngle=0
Blinds="start"
option=0

#program begins here:
while Blinds!="end":
    #States the current angle and gives options to add or subtract angles
    print()
    print(f"The current angle is {CurrentAngle} ")
    print("Would you like to:\n")
    option=int(input("1. Add to the angle?\n2. Subtract from the angle? "))
    print()
    #option 1 allows user to add numerical values, so long as the values are within 0 and 180.
    if option==1:
        Angle=int(input("What angle would you like to add? "))
        #Checks input from user to see if the value can be fully added or if it will be limited to 180
        if Angle+CurrentAngle>=180:
            ErrAngle=180-CurrentAngle
            CurrentAngle=ErrAngle+CurrentAngle
        else:
            CurrentAngle=CurrentAngle+Angle
    #option 2 allows user to subtract numerical values, so long as the values are within 0 and 180.
    elif option==2:
        Angle=int(input("What angle would you like to subtract? "))
        #Checks input from user to see if the value can be fully added or if it will be limited to 180
        if CurrentAngle-Angle<=0:
            ErrAngle=CurrentAngle-CurrentAngle
            CurrentAngle=ErrAngle
        else:
            CurrentAngle=CurrentAngle-Angle
print()
