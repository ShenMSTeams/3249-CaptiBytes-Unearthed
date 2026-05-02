from pybricks.tools import wait
from distance_sensor import AndySensor

def MissionOne(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission One")
    # This missions objective is M12 Salvage Operations,(30 points)
    # and dropping one flag from M15 (10 points)

    robot.settings(straight_speed=400)
    robot.straight(500) # Uncovers the sand 
    robot.straight(-500) # Comes back to base
    wait(2000)
    robot.straight(650) # Lifts the ship
    # You need a wait before making the motors moving or the code runs and then before it starts it stops 
    right_attachment_motor.run_time(400,1000) # Drops the flag 
    wait(500)
    robot.straight(-680) # Comes back to base
