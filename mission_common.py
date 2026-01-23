from pybricks.tools import hub_menu

class Mission:
    __base = 1

    def __init__(self, identifier = None) -> None:
        if identifier is None:
            self.number = Mission.__base
            Mission.__base += 1
        else:
            self.number = identifier

    def __call__(self, method):
        self.__method = method
        return self

    def run(self, robot, left_attachment_motor, right_attachment_motor) -> None:
        self.__method(*robot, *left_attachment_motor, *right_attachment_motor)

    def __lt__(self, other: Mission) -> bool:
        return self.number < other.number

    def method(self, robot, left_attachment_motor, right_attachment_motor):
        return lambda: self.run(robot, left_attachment_motor, right_attachment_motor)

class MissionControl():
    def __init__(self, missions) -> None:
        self.robot = ()
        self.left_attachment_motor = ()
        self.right_attachment_motor = ()
        methods = (getattr(missions, method) for method in dir(missions))
        self.missions = [method for method in methods if type(method) is Mission]
        self.missions.sort()

    def use_robot(self, *robot):
        self.robot = robot
        return self

    def run(self) -> None:
        print([mission.number for mission in self.missions])
        chosen = hub_menu(*(mission.number for mission in self.missions))
        next(
            mission for mission in self.missions if mission.number == chosen
        ).run(self.robot, self.left_attachment_motor, self.right_attachment_motor)
        self.missions = self.missions[1:] + self.missions[:1]

    def run_all(self):
        while ...:
            self.run()