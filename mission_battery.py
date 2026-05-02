from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from distance_sensor import AndySensor

def MissionBattery(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor ):
    print("Mission Battery ")
    hub.display.text("Battery Value:%s%%" % (hub.battery.voltage() / 84))

