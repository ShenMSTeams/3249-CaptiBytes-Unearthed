from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait

class AndySensor:
    def __init__(self, port: Port):
        self.sensor = UltrasonicSensor(port)
    def wait_for_wall(self, distance: float):
        while self.sensor.distance() > distance:
            wait(12)
    def lights(self, value: bool):
        if value:
            self.sensor.lights.on(100)
        else:
            self.sensor.lights.off()
