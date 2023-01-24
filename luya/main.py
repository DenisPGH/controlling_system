from  datetime import datetime
from sensor import Sensor
from database import DataBaseSensor
from control import ActuatorFan,ActuatorHeat



class Main:
    def __init__(self):
        self.sensor=Sensor()
        self.db=DataBaseSensor()
        self.TARGET_TEMPERATUR = 32  # C
        self.INTERVAL_CONTROL = 1  # seconds
        self.current_temperature=0

    def start_program(self):
        last_time = datetime.now()
        while True:
            current_time = datetime.now()
            delta_time = (current_time - last_time).total_seconds()
            if delta_time >= self.INTERVAL_CONTROL:
                # read the temperature
                self.current_temperature=self.sensor.reading_temperature()
                # store into db
                self.db.adding__new_date(current_time.strftime('%Y-%m-%d %H:%M:%S'),self.current_temperature)
                # run pid

                # control actuators

                last_time = datetime.now()






