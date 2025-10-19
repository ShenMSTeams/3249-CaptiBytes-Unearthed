from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

class MissionOne:
    def Run(self, robot:DriveBase, left_attachment_motor, right_attachment_motor):
        print("Mission One")
        robot.straight(500)
        robot.straight(-500)
        wait(2000)
        robot.straight(800)
        # You need a wait before making the motors moving or the code runs and then before ti stars it stops 
        right_attachment_motor.run(-1000)
        left_attachment_motor.run(4000)
        wait(3000)

        