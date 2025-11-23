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
        robot.straight(-250)
        robot.straight(250)
        robot.turn(90,Stop.HOLD,True)
        robot.straight(490)
        robot.turn(-90,Stop.HOLD,True)
        left_attachment_motor.run(-300)
        right_attachment_motor.run(-300)
        wait(2000)
        robot.straight(70)  # realinment
        robot.straight(-30)
        robot.turn(82,Stop.HOLD,True)
        robot.straight(70)
        robot.straight(370)
        robot.turn(75,Stop.HOLD,True)
        left_attachment_motor.run(300)
        right_attachment_motor.run(300) # dropping of basket
        wait(2000)
        left_attachment_motor.run(-300)
        right_attachment_motor.run(-300)
        wait(2000)
        robot.turn(-45,Stop.HOLD,True)
        robot.straight(215)
        robot.turn(10,Stop.HOLD,True)
        robot.straight(150)
        robot.straight(-100)
        robot.turn(-45,Stop.HOLD,True) # turning to get back to base
        robot.turn(35,Stop.HOLD,True)
        robot.straight(180)
        robot.turn(45,Stop.HOLD,True)
        robot.straight(600)