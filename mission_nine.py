from pybricks.tools import wait
from distance_sensor import AndySensor

def MissionNine(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Nine")
    #This mission completes mission 
    robot.straight(325)
    robot.turn(-45)
    robot.straight(140)
    robot.turn(-60)# Hits the bar for lifting the marketware
    robot.turn(60)  
    right_attachment_motor.run_time(-1000,800)
    wait(1000)
    robot.straight(-200)
    #robot.straight(20)
    right_attachment_motor.run_time(1000,800)
    robot.straight(-30)
    robot.turn(-45)
    robot.straight(350)
    robot.turn(90)
    robot.straight(40)
    robot.straight(-150)
    robot.turn(-90) 
    robot.settings(straight_speed=400)
    robot.straight(-630) # coming back to base

    #robot.turn(60) 
    #wait(1000)
    #robot.straight(-200)
   
    