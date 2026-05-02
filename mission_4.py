from pybricks.tools import wait
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from distance_sensor import AndySensor

def MissionFour(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor):
    print("Mission Four")
    # This missions objective is to complete M11 Angler Artifacts (30 points)
    # This mission also sends the bot over to red base 
    robot.settings(straight_speed=300)
    robot.straight(200)
    robot.turn(-90)
    robot.straight(589)
    robot.turn(-90)
    robot.straight(50)
    #robot.turn(-90)
    #robot.straight(48) # Motor is conneted to the gear
    left_attachment_motor.run_time(8000,2000) # Motor runs and artifacts are rasied
    wait(2000)
    robot.straight(-95)
    robot.turn(90)
    robot.settings(straight_speed=350)
    robot.straight(866) # Goes to red base
    





  
   


   
