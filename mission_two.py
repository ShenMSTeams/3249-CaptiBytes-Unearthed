from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop

def MissionTwo(robot:DriveBase, left_attachment_motor, right_attachment_motor):
    print("Mission Two")
    robot.settings(straight_speed=300)
    robot.straight(675) #Moving to the surface brush
    robot.straight(-250) #Knock down first brush
    robot.straight(260) #Knock downs second brush
    robot.turn(90)      
    robot.straight(170) 
    robot.turn(-135)
    robot.straight(210)
    #robot.straight(210)
    left_attachment_motor.run_time(80,1000) #Lifts the piece
    #robot.straight(-130)
    robot.straight(-140)
    #robot.turn(140)
    #robot.turn(90)
    #robot.straight(-50)
    #robot.turn(40)
    #robot.straight(200)
    #robot.turn(25)
    #left_attachment_motor.run_time(-70,1000)
    #robot.straight(-50)
    #robot.turn(30)
    #robot.turn(-50)
    #robot.straight(-100)


    robot.turn(45)
    robot.straight(-750)

    """robot.straight(180)
    robot.turn(48)
    left_attachment_motor.run_time(-200,1000)
    robot.straight(-50)
    robot.turn(-45)
    robot.straight(-100)
    robot.turn(-90)
    robot.straight(-780)"""



    #robot.straight(100)
    #robot.straight(30)
    #robot.turn(-54)     #turns and moves the green areas
    #robot.straight(65)  
    #robot.straight(-70) 
    #robot.turn(13.5)
    #robot.straight(140)
    #robot.straight(-100)
    #robot.turn(45)
    #robot.straight(-800)


    #robot.turn(30)
    #robot.turn(15)
    #robot.straight(50)
    #robot.turn(-160)
    #robot.turn(90)
    #robot.turn(-45)
    #robot.straight(50)
