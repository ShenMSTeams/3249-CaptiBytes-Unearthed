from pybricks.tools import wait
from distance_sensor import AndySensor

def MissionZero(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Zero")
    robot.settings(straight_speed=400)
    robot.straight(450)
    robot.straight(-450)
