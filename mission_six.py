from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop

def MissionSix(robot:DriveBase, left_attachment_motor, right_attachment_motor):
    print("Mission Six")
    robot.straight(675) #Moving to the surface brush
    robot.straight(-250) #Knock down first brush
    robot.straight(260) #Knock downs second brush
    robot.turn(90)      
    robot.straight(100) 
    robot.turn(-90)     
    robot.straight(30)
    robot.turn(-54)     #turns and moves the green areas
    robot.straight(65)  
    robot.straight(-70) 
    robot.turn(13)
    robot.straight(140)
    left_attachment_motor.run_time(300,1000) #Lifts the piece

    #robot.turn(30)
    #robot.turn(15)
    #robot.straight(50)
    #robot.turn(-160)
    #robot.turn(90)
    #robot.turn(-45)
    #robot.straight(50)
