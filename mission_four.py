from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionFour(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Four")

    #robot.straight(350)
    # False means don't wait for the motor to finish running before going to the next step    
    # Move Down
    robot.settings(straight_speed=200)
    robot.straight(499)
    left_attachment_motor.run_time(400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(400,700)
    wait(1000)
    # Move up
    left_attachment_motor.run_time(-400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(-400,700)
    wait(500)
    left_attachment_motor.run_time(400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(400,700)
    wait(500)
    left_attachment_motor.run_time(-400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(-400,700)
    wait(500)
    left_attachment_motor.run_time(400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(400,700)
    wait(500)
    left_attachment_motor.run_time(-400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(-400,700)
    wait(500)
    left_attachment_motor.run_time(400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(400,700)
    wait(500)
    left_attachment_motor.run_time(-400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(-400,700)
    robot.straight(-100)
    robot.turn(-360)
    robot.straight(-180)
    robot.turn(-90)
    robot.straight(365)
    robot.turn(90)
    robot.straight(80)
    robot.straight(-150)
    robot.turn(-90)
    robot.straight(-700)
    
    
    