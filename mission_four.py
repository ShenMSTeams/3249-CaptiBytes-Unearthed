from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionFour(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Four")

    #robot.straight(350)
    # False means don't wait for the motor to finish running before going to the next step    
    # Move Down
    robot.settings(straight_speed=200)
    robot.straight(400)
    robot.turn(40)
    robot.straight(20)
    robot.turn(-40)
    robot.straight(79)
    left_attachment_motor.run_time(400,700,Stop.HOLD, False) 
    right_attachment_motor.run_time(400,700) #down
    wait(1000)
    # Move up
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
    #left_attachment_motor.run_time(400,700,Stop.HOLD, False) 
    #right_attachment_motor.run_time(400,700)
    #wait(500)
    #left_attachment_motor.run_time(-400,700,Stop.HOLD, False) 
    #right_attachment_motor.run_time(-400,700)
    robot.straight(-100)
    robot.turn(-360)
    robot.straight(-200)
    robot.turn(-90)
    robot.straight(400)
    robot.turn(95)
    robot.straight(90)
    robot.straight(-150)
    robot.turn(-90)
    robot.straight(-700)
    
    
    