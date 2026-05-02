from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionThree(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Three")
    robot.settings(straight_speed=350)
    robot.straight(660)
    robot.turn(90,Stop.HOLD,True)
    robot.straight(483)
    robot.turn(-90,Stop.HOLD,True)
    left_attachment_motor.run(-300)
    right_attachment_motor.run(-300)
    wait(2000)
    robot.straight(75)
    robot.turn(90)
    robot.straight(250)
    robot.turn(130)
    robot.straight(30)
    left_attachment_motor.run(500)
    right_attachment_motor.run(500)
    robot.straight(-20)
