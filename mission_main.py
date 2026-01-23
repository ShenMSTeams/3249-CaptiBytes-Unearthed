from mission_common import Mission, MissionControl
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from mission_one import MissionOne
from mission_two import MissionTwo
from mission_three import MissionThree
from mission_four import MissionFour
from mission_five import MissionFive
from mission_six import MissionSix
from mission_seven import MissionSeven
from mission_eight import MissionEight

class MyMissions():
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

    @Mission(8)
    def go_mission_eight(*robot):
        MissionEight(*robot)

hub = PrimeHub() 

# Display voltage
print("%s%%" % (hub.battery.voltage() / 73))

hub.display.orientation(Side.TOP)
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor,
                  wheel_diameter=62.4, axle_track=85.7)
robot.use_gyro(True)

left_attachment_motor = Motor(Port.B, Direction.CLOCKWISE,  [12, 20])
right_attachment_motor = Motor(Port.D, Direction.CLOCKWISE, [12, 20])

MissionControl(MyMissions).use_robot(
    robot,
    left_attachment_motor,
    right_attachment_motor
).run_all()