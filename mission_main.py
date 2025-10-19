from mission_common import Mission, MissionControl
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.tools import hub_menu
from mission_one import MissionOne
from mission_two import MissionTwo

# Explicitly setup everything
class MyMissions():
    @Mission(1)
    def go_forward(robot, left_attachment_motor, right_attachment_motor):
        m = MissionOne()
        m.Run(robot, left_attachment_motor, right_attachment_motor)

    @Mission(2)
    def go_reverse(robot, left_attachment_motor, right_attachment_motor):
        m = MissionTwo()
        m.Run(robot, left_attachment_motor, right_attachment_motor)

hub = PrimeHub()
hub.display.orientation(Side.TOP)
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor,
                  wheel_diameter=62.4, axle_track=20)
robot.use_gyro(True)

left_attachment_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_attachment_motor = Motor(Port.D, Direction.CLOCKWISE)

missions = MissionControl(MyMissions).use_robot(robot).use_left_attachment_motor(left_attachment_motor).use_right_attachment_motor(right_attachment_motor)

# Unconditionally run all missions
#for mission in missions:
#    mission()

# Use selector to run all missions
missions.run()

# Don't put code here, MissionControl->run_all never returns

