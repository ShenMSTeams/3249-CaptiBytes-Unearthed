from pybricks.tools import wait
from distance_sensor import AndySensor

def MissionNine(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Nine")
    robot.straight(325)
    robot.turn(-45)
    robot.straight(140)
    robot.turn(-60)
    robot.turn(60)  #Turn Back from getting the market wares
    right_attachment_motor.run_time(-1000,800)
    wait(1000)
    robot.straight(-200)
    robot.straight(20)
    right_attachment_motor.run_time(1000,800)
    robot.turn(-45)
    robot.straight(365)
    robot.turn(90)
    robot.straight(40)
    robot.straight(-150)
    robot.turn(-90)
    robot.straight(-630)
    