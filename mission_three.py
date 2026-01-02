from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop

def MissionThree(robot:DriveBase, left_attachment_motor, right_attachment_motor):
    print("Mission Three")

    #robot.straight(350)
    # False means don't wait for the motor to finish running before going to the next step    
    # Move Down
    robot.straight(475)
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
    robot.straight(-60)
    robot.turn(-35)
    robot.straight(-400)
    