"""
pip install pigpio
"""

import RPi.GPIO as GPIO


class Actuator:
    def __init__(self):
        self.GPIO_PWM_NUMBER=0
        self.INITIAL_START_VALUE_PWM=0
        self.INITIAL_DUTY_CYCLE_PWM=1
        self.gpio=GPIO.setmode(GPIO.BOARD)
        self.gpio.setup(self.GPIO_PWM_NUMBER, GPIO.OUT)

        self.actuator= GPIO.PWM(self.GPIO_PWM_NUMBER, self.INITIAL_START_VALUE_PWM)
        # self.heat = GPIO.PWM(self.PWM_HEAT, self.INITIAL_START_VALUE_PWM)



    def control_fan(self,frequency:int):
        """
        controling the pwm for the cooling element
        :param frequency: int 0-40kHz
        :return:
        """

        self.fan.start(self.INITIAL_DUTY_CYCLE_PWM)
        self.fan.ChangeFrequency(frequency)
        self.fan.stop()
        return


    def control_heat(self,frequency:int):
        """
        controling the pwm for the heating element
         :param frequency: int 0-40kHz
        :return:
                """
        self.heat.start(self.INITIAL_DUTY_CYCLE_PWM)
        self.heat.ChangeFrequency(frequency)
        self.heat.stop()
        return


class ActuatorFan(Actuator):
    def __init__(self):
        super().__init__()
        self.GPIO_PWM_NUMBER=12


class ActuatorHeat(Actuator):
    def __init__(self):
        super().__init__()
        self.GPIO_PWM_NUMBER=13

