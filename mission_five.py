from pybricks.tools import wait
from distance_sensor import AndySensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
def MissionFive(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor ):
    print("Mission Five ")
   # This mission main objective is to get M06 Forge (30 points)
   # it gets M05 Who Lived Here (30 points)
   # it also gets M07 Heavy Lifting(30 points)
    robot.straight(-735) 
    robot.turn(-95)#turns and hits forge
    robot.straight(-120)#Turns and hits who lives here
    robot.turn(45)
    robot.straight(210)
    robot.turn(-81)
    robot.straight(100)
    left_attachment_motor.run_time(70,2050,Stop.HOLD, False)
    wait(2000) # Drops arm down for the mill stone
    robot.straight(60)
    left_attachment_motor.run_time(-100,4000,Stop.HOLD, False) # lift mill stone
    wait(1000)
    robot.straight(-120)
    robot.turn(-50)
    robot.straight(-400) # Coming back to base
    robot.turn(-50)
    robot.straight(-400)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #wait(1000)
    #robot.turn(-10)
    #robot.turn(25)
    #left_attachment_motor.run_time(-1000,400,Stop.HOLD, False)
    #right_attachment_motor.run_time(1000,400)

    #robot.straight(59)
    #robot.turn(-20)
    #left_attachment_motor.run_time(-1000,400,Stop.HOLD, False)
    #right_attachment_motor.run_time(1000,400)
    #wait(1000)
    #robot.straight(-15)
    #robot.turn(75)
    #left_attachment_motor.run_time(900,400,Stop.HOLD, False)
    #right_attachment_motor.run_time(-900,400)
    #robot.straight(-150)
    #robot.turn(90)
    #robot.straight(700)
    #robot.turn(-300)
    #robot.straight(-90)
    #robot.turn(90)
    #robot.straight(-20)


    #robot.straight(-450)
    #robot.turn(45)
    #robot.straight(-100)
    #robot.turn(75)
    #robot.straight(20)
   # robot.straight(-25)
   # robot.turn(-25)
    #robot.straight(-50)
    #robot.straight(50)
   # robot.turn(45)
   # robot.straight(50)
   # robot.turn(50)
   # right_attachment_motor.run_time(110)
  #  robot.turn(150)
   # robot.turn(-20)
   # robot.straight(255)
   # robot.turn(40)
  #  robot.straight(100)
   # robot.straight(-50)
   # robot.turn(-90)
   # robot.straight(-400) 

        