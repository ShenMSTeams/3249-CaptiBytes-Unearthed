from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionSeven(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Seven")
    robot.settings(straight_speed=400)
    robot.straight(680)
    robot.straight(-380)
    robot.turn(45)
    #robot.drive(200,0)
    #eyes.wait_for_wall(285)   
    robot.straight(100)
    robot.turn(-45)
    robot.drive(200,0)
    eyes.wait_for_wall(245)   
    robot.turn(-45)
    robot.straight(175)
    right_attachment_motor.run_time(1600,800)# Lifiting the green piece
    robot.straight(-175)
    robot.turn(50)
    robot.straight(-700)
    
    #right_attachment_motor.run_time(1600,800)# Lifiting the green piece






    #robot.straight(650)
    #robot.straight(-300)
    #robot.turn(90)
    #robot.straight(300)
    #robot.straight(15)
    #robot.turn(-90)
    #robot.straight(100)

    # This missions main objective is M01 completing surface brusher (20 points)
    # and M02 Map reveal uncovering the top soil (30 points)
    #robot.settings(straight_speed=400)#makes the bot move faster
    #robot.straight(650)#Kocking down the first surface brush
    #robot.straight(-80) # Knocking down the second brush
    #robot.straight(50)
    #robot.straight(-370)
    #robot.straight(200)
    #robot.straight(200)#pases surface brush
    #robot.turn(90)#turns towards forum readjust
    #robot.straight(20) #moves to forum readjust
    #robot.turn(-90)  #turns back to 
    #robot.drive(200,0)
    #eyes.wait_for_wall(295) # Distance sensor alignment   
    #robot.turn(-40)
    #robot.straight(240)# Push the green piece to the side and push the other piece back
    #right_attachment_motor.run_time(1600,800)# Lifiting the green piece
    #robot.straight(-280)
    #robot.turn(70)
    #robot.straight(-650) # Coming back to base
 
