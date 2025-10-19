from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

class MissionTwo:
    def Run(self, robot:DriveBase, left_attachment_motor, right_attachment_motor):
        print("Mission Two")
        robot.straight(675)
        robot.straight(-200)
        robot.straight(200)
        robot.turn(90)
        robot.straight(495)
        robot.turn(-50)
        right_attachment_motor.run(-1000)
        left_attachment_motor.run(4000)
        wait(300)