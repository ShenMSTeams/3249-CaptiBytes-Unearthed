from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionFour(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Four")
    # This missions main obejective, is M08 Silo (30 points)
    robot.settings(straight_speed=400, turn_rate=90)
    robot.straight(400)
    robot.turn(40)
    robot.straight(20)
    robot.turn(-40) # Realign
    robot.straight(79)
    left_attachment_motor.run_time(400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(400,700) #down
    wait(500)
    left_attachment_motor.run_time(-400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(-400,700) #up
    wait(500)
    left_attachment_motor.run_time(400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(400,700) #down
    wait(500)
    left_attachment_motor.run_time(-400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(-400,700) #up
    wait(500)
    left_attachment_motor.run_time(400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(400,700) #down
    wait(500)
    left_attachment_motor.run_time(-400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(-400,700) #up
    wait(500)
    robot.straight(-500) # Come back to base
    
    
    