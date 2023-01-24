"""
pip install pigpio
"""

import RPi.GPIO as GPIO


class Actuator:
    DEFAULT_DUTY_CYCLE=1 # %
    def __init__(self):
        self.MAX_FREQUENCY=20000 # Hz limit from the AOD4184
        self.MIN_FREQUENCY=0 # Hz limit from the AOD4184

        self.MAX_DUTY_CYCLE = 100  # %
        self.MIN_DUTY_CYCLE = 0  # %
        self.STRING_ERROR_FREQUENCY=f"The frequency must be between {self.MIN_FREQUENCY} and {self.MAX_FREQUENCY}"
        self.STRING_ERROR_DUTY_CYCLE=f"The duty cycle must be between {self.MIN_DUTY_CYCLE} and {self.MAX_DUTY_CYCLE}"

        self.GPIO_PWM_NUMBER=0
        self.INITIAL_START_VALUE_PWM=0 # Hz
        self.INITIAL_DUTY_CYCLE_PWM=1 # 0-100 %
        self.gpio=GPIO.setmode(GPIO.BOARD)




    def start_actuator_for_work(self):
        """
        this function initial and get ready the actuator for work
        :return: nothing
        """
        self.gpio.setup(self.GPIO_PWM_NUMBER, GPIO.OUT)
        self.actuator = GPIO.PWM(self.GPIO_PWM_NUMBER, self.INITIAL_START_VALUE_PWM)
        self.actuator.start(self.INITIAL_DUTY_CYCLE_PWM)
        return


    def control(self,frequency:float,duty_cycle=DEFAULT_DUTY_CYCLE):
        """
        change the working frequency of the actuator
        :param frequency: set the actuator of the new value
        :param duty_cycle: working percent
        :return: nothing
        """
        if not self.MIN_FREQUENCY<=frequency <=self.MAX_FREQUENCY:
            raise ValueError(self.STRING_ERROR_FREQUENCY)
        if not self.MIN_DUTY_CYCLE<=duty_cycle <=self.MAX_DUTY_CYCLE:
            raise ValueError(self.STRING_ERROR_DUTY_CYCLE)

        self.actuator.ChangeDutyCycle(duty_cycle)
        self.actuator.ChangeFrequency(frequency)
        return

    def stop_actuator(self):
        """
        when stop working, just stop the pwm
        :return:
        """
        self.actuator.stop()
        return

    def clean_up_pwm(self):
        """ Clean up the system"""
        self.gpio.cleanup()







class ActuatorFan(Actuator):
    def __init__(self):
        super().__init__()
        self.GPIO_PWM_NUMBER=12 # setup the GPIO of the Fan


class ActuatorHeat(Actuator):
    def __init__(self):
        super().__init__()
        self.GPIO_PWM_NUMBER=13 # setup the GPIO of the Heating element

