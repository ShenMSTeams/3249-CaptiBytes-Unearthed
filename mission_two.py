from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionTwo(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Two")

    # This missions main objective is M01 completing surface brusher (20 points)
    # and M02 Map reveal uncovering the top soil (30 points)
    
    robot.settings(straight_speed=400)
    robot.straight(650)#Kocking down the first surface brush
    robot.straight(-450) # Knocking down the second brush
    robot.straight(200)
    robot.turn(90)
    robot.straight(100) 
    robot.turn(-90)  
    robot.drive(200,0)
    eyes.wait_for_wall(295) # Distance sensor alignment   
    robot.turn(-40)
    robot.straight(280)# Push the green piece to the side and push the other piece back
    right_attachment_motor.run_time(800,800)# Lifiting the green piece
    robot.straight(-280)
    robot.turn(45)
    robot.straight(-650) # Coming back to base
 
