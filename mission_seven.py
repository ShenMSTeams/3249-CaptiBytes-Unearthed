from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop

def MissionSeven(robot:DriveBase, left_attachment_motor, right_attachment_motor):
    print("Mission Seven")
    robot.straight(718)
    robot.turn(90)
    robot.straight(300)
    robot.turn(-45)
    robot.straight(150)
    robot.turn(-60)
    robot.straight(90)
    robot.turn(100)
    robot.straight(23.5)
