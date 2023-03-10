
"""  pip install simple-pid   """
from simple_pid import PID

class PIDTemperature:
    """
    class for correction the heating element with PID
    the value of each P,I,D have to be adjust very well
    """
    def __init__(self):
        self.PID = PID
        # heat
        self.Kp_heat = 1
        self.Ki_heat = 0
        self.Kd_heat = 0
        self.OUTPUT_LIMITS_MIN_HEAT=1 # if temperature is low, have to MORE power the heat
        self.OUTPUT_LIMITS_MAX_HEAT=20000 # Hz
        # fan
        self.Kp_fan = 1
        self.Ki_fan = 0
        self.Kd_fan = 0
        self.OUTPUT_LIMITS_MIN_FAN = 20000 # 20 000 Hz if temperature is low, have to LESS power the fan
        self.OUTPUT_LIMITS_MAX_FAN = 1 # 1 Hz



    def output_heat(self, set_point:float, current_temperature:float):
        """
        control frequency for the heating element
        :param set_point: target temperature
        :param current_temperature: actual temperature
        :return: the output value after calculation
        """

        pid_heat = self.PID(self.Kp_heat, self.Ki_heat, self.Kd_heat, setpoint=set_point)
        pid_heat.output_limits = (self.OUTPUT_LIMITS_MIN_HEAT, self.OUTPUT_LIMITS_MAX_HEAT)
        output_heat = pid_heat(current_temperature)
        return output_heat

    def output_fan(self, set_point:float, current_temperature:float):
        """
        control frequency for the fan
        :param set_point: target temperature
        :param current_temperature: actual temperature
        :return: the output value after calculation
        """

        pid_fan = self.PID(self.Kp_fan, self.Ki_fan, self.Kd_fan, setpoint=set_point)
        pid_fan.output_limits = (self.OUTPUT_LIMITS_MIN_FAN, self.OUTPUT_LIMITS_MAX_FAN)
        output_fan = pid_fan(current_temperature)
        return output_fan





