from  datetime import datetime
from pid_control import PIDTemperature
from sensor import Sensor
from database import DataBaseSensor
from control import ActuatorFan,ActuatorHeat
"""
For run this script on boot:

1.	Create file:           sudo nano /usr/local/bin/chamber.sh        with content:
#! /bin/bash
export DISPLAY=:0
/usr/bin/python3 /home/user/Desktop/luya/main.py

2.	 Give permission to execute the file sudo chmod 777  /usr/local/bin/chamber.sh    
3.	 Create file:        sudo nano /lib/systemd/system/chamber.service     with content: 
[Unit]
Description=Control Temperature application
After=multi-user.target
After=graphical.target 
[Service]
ExecStart=/usr/local/bin/chamber.sh
Restart=always
StartLimitInterval=10
RestartSec=10
Restart=on-failure
User=<your_user> 
[Install]
WantedBy=multi-user.target
WantedBy=graphical.target


4.	Enable the service script to run after boot :  sudo systemctl enable chamber.service
5.	 Start the service :  sudo systemctl start chamber.service
6.	 Check if the service work well:  sudo systemctl status chamber.service

"""



class Main:
    def __init__(self):
        self.sensor=Sensor()
        self.db=DataBaseSensor()
        self.pid_temp=PIDTemperature()
        self.fan=ActuatorFan()
        self.heat=ActuatorHeat()
        self.TARGET_TEMPERATURE = 32  # C
        self.INTERVAL_CONTROL = 1  # seconds
        self.current_temperature=0

    def start_program(self):
        """
        this function just start the main logic
        :return:
        """
        last_time = datetime.now()
        self.heat.start_actuator_for_work()
        self.fan.start_actuator_for_work()
        while True:
            current_time = datetime.now()
            delta_time = (current_time - last_time).total_seconds()
            if delta_time >= self.INTERVAL_CONTROL:
                # read the temperature
                self.current_temperature=self.sensor.reading_temperature()
                # store into db
                self.db.adding__new_data(current_time.strftime('%Y-%m-%d %H:%M:%S'),
                                         self.current_temperature)
                # run pid= more temperature=> more fun, less heat, less temperature more heat, less fan
                output_heat=self.pid_temp.output_heat(self.TARGET_TEMPERATURE, self.current_temperature)
                output_fan=self.pid_temp.output_fan(self.TARGET_TEMPERATURE, self.current_temperature)
                # control actuators
                self.heat.control(output_heat)
                self.fan.control(output_fan)
                # update time
                last_time = datetime.now()
        # if out of the loop= stop PWM signal and clean up
        self.heat.stop_actuator()
        self.fan.stop_actuator()
        self.heat.clean_up_pwm() # or
        self.fan.clean_up_pwm()




if __name__=="__main__":
    m=Main()
    m.start_program()






