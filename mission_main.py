from mission_common import Mission, MissionControl
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from mission_0 import MissionZero
from mission_1 import MissionOne
from mission_2 import MissionTwo
from mission_3 import MissionThree
from mission_4 import MissionFour
from mission_5 import MissionFive
from mission_6 import MissionSix
from mission_7 import MissionSeven
#from mission_eight import MissionEight
#from mission_nine import MissionNine
#from mission_ten import MissionTen
from distance_sensor import AndySensor

class MyMissions():
    @Mission(0)
    def go_mission_zero(*robot):
        MissionZero(*robot)

    @Mission(1)
    def go_mission_one(*robot):
        MissionOne(*robot)

    @Mission(2)
    def go_mission_two(*robot):
        MissionTwo(*robot)

    @Mission(3)
    def go_mission_three(*robot):
        MissionThree(*robot)


    @Mission(4)
    def go_mission_four(*robot):
        MissionFour(*robot)


    @Mission(5)
    def go_mission_five(*robot):
        MissionFive(*robot)

    @Mission(6)
    def go_mission_six(*robot):
        MissionSix(*robot)


    @Mission(7)
    def go_mission_seven(*robot):
        MissionSeven(*robot)

    #@Mission(8)
    #def go_mission_eight(*robot):
    #    MissionEight(*robot)

    #@Mission(9)
    #def go_mission_nine(*robot):
    #    MissionNine(*robot)

    #@Mission(10)
    #def go_mission_ten(*robot):
    #    MissionTen(*robot)
        


hub = PrimeHub() 

# Display voltage
print("Battery Value:%s%%" % (hub.battery.voltage() / 84))

hub.display.orientation(Side.TOP)
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor,
                  wheel_diameter=62.4, axle_track=85.7)
robot.use_gyro(True)

left_attachment_motor = Motor(Port.B, Direction.CLOCKWISE,  [12, 20])
right_attachment_motor = Motor(Port.D, Direction.CLOCKWISE, [12, 20])
eyes = AndySensor(Port.A)

MissionControl(MyMissions).use_robot(
    robot,
    left_attachment_motor,
    right_attachment_motor,
    eyes
).run_all()