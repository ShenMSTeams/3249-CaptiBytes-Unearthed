from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

class MissionFive:
    def Run(self, robot:DriveBase, left_attachment_motor, right_attachment_motor):
        print("Mission Five")
        robot.straight(670)
        robot.turn(90)
        robot.straight(160)
        robot.straight(-135)
        robot.turn(-90,Stop.HOLD, True)
        robot.straight(-670)
