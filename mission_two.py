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
        robot.straight(90)
        robot.straight(300)
        robot.turn(75,Stop.HOLD,True)
        left_attachment_motor.run(300)
        right_attachment_motor.run(300) # dropping of basket
        wait(2000)
        left_attachment_motor.run(-300)
        right_attachment_motor.run(-300)
        wait(2000)
        robot.turn(-72,Stop.HOLD,True)
        #robot.arc(400,angle=53,then=Stop.HOLD,wait=True)
        robot.arc(400,angle=47,then=Stop.HOLD,wait=True)
        #robot.straight(215)
        #robot.arc(-405,angle=30,then=Stop.HOLD,wait=True)
        #robot.turn(10,Stop.HOLD,True)
        #robot.straight(150)
        robot.straight(-109)
        #robot.turn(-45,Stop.HOLD,True) # turning to get back to base
        #obot.turn(35,Stop.HOLD,True)
        #robot.straight(180)
        #robot.turn(45,Stop.HOLD,True)
        #robot.straight(600)