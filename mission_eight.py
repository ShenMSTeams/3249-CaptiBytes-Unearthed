from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionEight(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Eighth")
    robot.straight(866)
    robot.turn(-90)
    robot.straight(44)
    left_attachment_motor.run_time(1000,4000)
    robot.straight(-44)
    robot.turn(90)
    robot.straight(-866)
    #robot.turn(51)
    #robot.straight(554)
    #robot.turn(6.5)
    #robot.turn(-30) comment no
    #robot.turn(-23)
    #left_attachment_motor.run_time(850,700,Stop.HOLD, False)
    #right_attachment_motor.run_time(900,700)
    #robot.straight(2)
    #robot.straight(-3)
    #robot.straight(2)
    #robot.turn(13)





    #robot.straight(500)
    ##robot.turn(24)
    #robot.straight(350)
    #robot.turn(-50)
    #robot.straight(60)
    #robot.straight(200)
    #robot.turn(6.5)
    #robot.turn(-30)
    #robot.straight(4)
    #robot.turn(-23)
    #left_attachment_motor.run_time(850,700,Stop.HOLD, False) 
    #right_attachment_motor.run_time(900,700)
    #robot.straight(2)
    #robot.straight(-3)
    #robot.straight(2)
    #robot.turn(13)
    #left_attachment_motor.run_time(-500,1000,Stop.HOLD,False)


    #wait(1000)
    #robot.turn(-45)
    #left_attachment_motor.run_time(-400,700,Stop.HOLD, False) 
    #right_attachment_motor.run_time(-400,700)
    #wait(500)
   
