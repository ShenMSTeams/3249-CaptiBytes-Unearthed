from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#turn the bot around 
class MissionFour:
    def Run(self, robot:DriveBase, left_attachment_motor, right_attachment_motor):
        print("Mission Four ")
        robot.straight(-730)
        robot.turn(-120)
        robot.turn(150)
        robot.turn(-20)
        robot.straight(255)
        robot.turn(40)
        robot.straight(100)
        robot.straight(-50)
        robot.turn(-90)
        robot.straight(400)
        