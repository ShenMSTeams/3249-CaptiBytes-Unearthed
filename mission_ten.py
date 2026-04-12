from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionTen(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Ten")
    robot.straight(-500)
    robot.turn(15)
    robot.straight(-350)
    robot.turn(-105)
    robot.straight(-50)
    left_attachment_motor.run_time(600,700,Stop.HOLD, False)
    wait(1000)
    robot.straight(150)
