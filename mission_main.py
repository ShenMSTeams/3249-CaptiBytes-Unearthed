from mission_common import Mission, MissionControl
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from mission_one import MissionOne
from mission_two import MissionTwo
from mission_three import MissionThree
from mission_four import MissionFour
from mission_five import MissionFive
# Explicitly setup everything
class MyMissions():
    @Mission(1)
    def go_mission_one(robot, left_attachment_motor, right_attachment_motor):
        m = MissionOne()
        m.Run(robot, left_attachment_motor, right_attachment_motor)

    @Mission(2)
    def go_mission_two(robot, left_attachment_motor, right_attachment_motor):
        m = MissionTwo()
        m.Run(robot, left_attachment_motor, right_attachment_motor)

    @Mission(3)
    def go_mission_three(robot, left_attachment_motor, right_attachment_motor):
        m = MissionThree()
        m.Run(robot, left_attachment_motor, right_attachment_motor)


    @Mission(4)
    def go_mission_four(robot, left_attachment_motor, right_attachment_motor):
        m = MissionFour()
        m.Run(robot, left_attachment_motor, right_attachment_motor)


    @Mission(5)
    def go_mission_five(robot, left_attachment_motor, right_attachment_motor):
        m = MissionFive()
        m.Run(robot, left_attachment_motor, right_attachment_motor)


hub = PrimeHub() 
print(hub.battery.voltage())
hub.display.orientation(Side.TOP)
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor,
                  wheel_diameter=62.4, axle_track=88)
robot.use_gyro(True)

left_attachment_motor = Motor(Port.B, Direction.CLOCKWISE,  [12, 20])
right_attachment_motor = Motor(Port.D, Direction.CLOCKWISE, [12, 20])

missions = MissionControl(MyMissions).use_robot(robot).use_left_attachment_motor(left_attachment_motor).use_right_attachment_motor(right_attachment_motor)


missions.run()
#.use_attachment_motors(left_attachment_motor, right_attachment_motor)
#distance sensor is blue 
# Unconditionally run all missions
#for mission in missions:
    #mission()

# Use selector to run all missions


# Don't put code here, MissionControl->run_all never returns



