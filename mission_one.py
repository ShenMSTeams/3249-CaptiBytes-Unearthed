from pybricks.tools import wait

def MissionOne(robot:DriveBase, left_attachment_motor, right_attachment_motor, *):
    print("Mission One")
    robot.settings(straight_speed=400)
    robot.straight(500)
    robot.straight(-500)
    wait(3000)
    robot.straight(650) #750
    # You need a wait before making the motors moving or the code runs and then before ti stars it stops 
    right_attachment_motor.run_time(400,1000)
    wait(500)
    robot.straight(-680)