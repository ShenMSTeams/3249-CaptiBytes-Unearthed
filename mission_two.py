from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionTwo(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Two")
    robot.settings(straight_speed=400)
    robot.straight(650)#Moving to the surface brush
    robot.straight(-450)
    robot.straight(200)
    #left_attachment_motor.run_time(-130,10000) #Knock down first brush
    #robot.turn(-20)
    #left_attachment_motor.run_time(-100,3000)
    #obot.turn(20)
    robot.turn(90)
    robot.straight(100) #Knock downs second brush
    robot.turn(-90)  
    robot.drive(200,0)
    eyes.wait_for_wall(300)    
    robot.turn(-40)
    robot.straight(280)
    #robot.straight(210) #Lifts the piece
    #robot.straight(-130)
    robot.straight(-280)
    robot.turn(45)
    robot.straight(-650)
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

    #robot.turn(-75)
    #robot.straight(-100)
    #robot.turn(-55)
    #robot.straight(-330)
    #left_attachment_motor.run_time(-10,4000)

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
