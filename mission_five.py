from pybricks.tools import wait
from distance_sensor import AndySensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop

#turn the bot around 
def MissionFive(robot:DriveBase, left_attachment_motor, right_attachment_motor, eyes: AndySensor ):
    print("Mission Five ")
    robot.straight(-730)
    robot.turn(-100)
    robot.straight(-100)
    robot.straight(150)
    robot.turn(-25)
    left_attachment_motor.run_time(1000,400,Stop.HOLD, False)
    right_attachment_motor.run_time(1000,400)
    #wait(500)
    #left_attachment_motor.run_time(1000,400,Stop.HOLD, False)
    #right_attachment_motor.run_time(-1000,400)
    #robot.turn(100)
    #robot.straight(700)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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

        