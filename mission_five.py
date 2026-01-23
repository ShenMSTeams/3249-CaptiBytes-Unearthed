from pybricks.tools import wait

#turn the bot around 
def MissionFive(robot:DriveBase, left_attachment_motor, right_attachment_motor):
    print("Mission Five ")
    robot.straight(-730)
    robot.turn(-120)
    robot.straight(20)
    robot.turn(45)
    robot.straight(50)
    right_attachment_motor.run_time(110)
    #robot.turn(150)
    #robot.turn(-20)
    #robot.straight(255)
    #robot.turn(40)
    #robot.straight(100)
    #robot.straight(-50)
   # robot.turn(-90)
    #robot.straight(400) 

        