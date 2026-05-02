from pybricks.tools import wait
from distance_sensor import AndySensor

def MissionFive(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission One")
    # This missions objective is M12 Salvage Operations,(30 points)
    # and dropping one flag from M15 (10 points)

    robot.settings(straight_speed=400)#so the mission is faster
    robot.straight(500) # Uncovers the sand 
    robot.straight(-500) # Comes back to base
    wait(2000)#waits to change alignment and put flag in
    robot.straight(650) # Lifts the ship
    right_attachment_motor.run_time(400,1000) # Drops the flag 
    wait(500)#waits to push the ship up
    robot.straight(-680) # Comes back to base