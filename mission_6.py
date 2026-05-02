from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionSix(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Six")
    robot.straight(690)
    robot.turn(90)
    robot.straight(120)
    robot.straight(-135)
    robot.turn(-90,Stop.HOLD, True)
    robot.straight(-690)
