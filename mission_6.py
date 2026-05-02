from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionSix(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Six")
    robot.settings(straight_speed=400)
    robot.straight(780)
    robot.turn(65)
    robot.straight(220)
    robot.turn(20)
    robot.straight(100)
    right_attachment_motor.run_time(-600,600,Stop.HOLD, False) # Move arm up
    left_attachment_motor.run_time(600,600)
    wait(400)
    right_attachment_motor.run_time(600,600,Stop.HOLD, False) #Move arm down
    left_attachment_motor.run_time(-600,600)
    robot.straight(-40)
    robot.turn(60)
    robot.straight(280)
    robot.turn(-20)
    right_attachment_motor.run_time(-1000,800,Stop.HOLD, False) #Move arm down
    left_attachment_motor.run_time(1000,800)
    robot.turn(-20)
    robot.straight(-200)
    robot.turn(-70)
    robot.straight(-880)
    
    