from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionThree(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Three")
    robot.settings(straight_speed=350)
    robot.straight(680)
    #robot.turn(-80)
    #robot.turn(-22)
    #robot.straight(-50)
    #robot.straight(-100)
    robot.turn(90,Stop.HOLD,True)
    robot.straight(483)
    robot.turn(-90,Stop.HOLD,True)
    left_attachment_motor.run(-300)
    right_attachment_motor.run(-300)
    wait(2000)
    robot.straight(70)  # realinment
    robot.straight(-30)
    robot.turn(82,Stop.HOLD,True)
    robot.straight(90)
    robot.straight(320)
    robot.turn(75,Stop.HOLD,True)
    robot.straight(25)
    left_attachment_motor.run(300)
    right_attachment_motor.run(300) # dropping of basket
    wait(2000)
    left_attachment_motor.run(-300)
    right_attachment_motor.run(-300)
    wait(2000)
    robot.straight(-20)
    robot.turn(-72,Stop.HOLD,True)
    robot.arc(400,angle=52,then=Stop.HOLD,wait=True)
    robot.straight(-112)
    robot.turn(-45,Stop.HOLD,True) # turning to get back to base
    robot.straight(50)
    robot.turn(35,Stop.HOLD,True)
    robot.straight(180)
    robot.turn(45,Stop.HOLD,True)
    robot.straight(600)


    #robot.arc(400,angle=53,then=Stop.HOLD,wait=True)
    #robot.straight(215)
    #robot.arc(-405,angle=30,then=Stop.HOLD,wait=True)
    #robot.turn(10,Stop.HOLD,True)
    #robot.straight(150)
    #robot.turn(-45,Stop.HOLD,True) # turning to get back to base
    #obot.turn(35,Stop.HOLD,True)
    #robot.straight(180)
    #robot.turn(45,Stop.HOLD,True)
    #robot.straight(600)