from  datetime import datetime

from pid_control import PIDTemperature
from sensor import Sensor
from database import DataBaseSensor
from control import ActuatorFan,ActuatorHeat



class Main:
    def __init__(self):
        self.sensor=Sensor()
        self.db=DataBaseSensor()
        self.pid_temp=PIDTemperature()
        self.fan=ActuatorFan()
        self.heat=ActuatorHeat()
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
                output_heat=self.pid_temp.output_heat(self.TARGET_TEMPERATUR,self.current_temperature)
                output_fan=self.pid_temp.output_fan(self.TARGET_TEMPERATUR,self.current_temperature)
                # control actuators
                self.heat.start_actuator_for_work()
                self.heat.control(output_heat)

                self.fan.start_actuator_for_work()
                self.fan.control(output_fan)
                # update time
                last_time = datetime.now()
        # if out loop= stop PWM signal
        self.heat.stop_actuator()
        self.fan.stop_actuator()
        self.heat.clean_up_pwm() # or 
        self.fan.clean_up_pwm()






