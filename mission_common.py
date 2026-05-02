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

    def run(self, robot, left_attachment_motor, right_attachment_motor, eyes) -> None:
        self.__method(robot, left_attachment_motor, right_attachment_motor, eyes)

    def __lt__(self, other: Mission) -> bool:
        return self.number < other.number

    def method(self, robot, left_attachment_motor, right_attachment_motor, eyes):
        return lambda: self.run(robot, left_attachment_motor, right_attachment_motor, eyes)

class MissionControl():
    def __init__(self, missions) -> None:
        self.robot = ()
        self.left_attachment_motor = ()
        self.right_attachment_motor = ()
        self.eyes = ()
        # Get all Mission objects defined in the missions class
        methods = (getattr(missions, method) for method in dir(missions))
        self.missions = [method for method in methods if type(method) is Mission]
        # Sort missions by their assigned number
        self.missions.sort()

    def use_robot(self, robot, left_attachment_motor, right_attachment_motor, eyes):
        self.robot = robot
        self.left_attachment_motor = left_attachment_motor
        self.right_attachment_motor = right_attachment_motor
        self.eyes = eyes
        return self

    def run(self) -> None:
        # Display the current order of missions in the console for debugging
        print([mission.number for mission in self.missions])
        
        # hub_menu shows the first item in the list by default on the Hub screen
        chosen = hub_menu(*(mission.number for mission in self.missions))
        
        # Find the mission object that matches the number chosen on the menu
        mission_to_run = None
        chosen_index = 0
        for i, m in enumerate(self.missions):
            if m.number == chosen:
                mission_to_run = m
                chosen_index = i
                break
        
        # Run the selected mission
        mission_to_run.run(self.robot, self.left_attachment_motor, self.right_attachment_motor, self.eyes)
        
        # FIX: Rotate the list based on the CHOSEN mission index.
        # This moves the mission we just finished (and everything before it) 
        # to the end of the list. The NEXT mission in sequence will now be at index 0.
        self.missions = self.missions[chosen_index + 1:] + self.missions[:chosen_index + 1]

    def run_all(self):
        # Loop forever so the menu reappears after every mission
        while True:
            self.run()