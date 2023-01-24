"""
sudo pip3 install adafruit-circuitpython-sht31d
"""

import board
import busio
import adafruit_sht31d

class Sensor:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_sht31d.SHT31D(self.i2c)
        self.TEMPERATURE=0 # initial value
    def reading_temperature(self):
        """
        reading the temperature from the sensor and return it
        :return: the temperature float type
        """
        try:
            self.TEMPERATURE=self.sensor.temperature
        except:
            print('Error with the sensor.')
            return self.TEMPERATURE
        return self.TEMPERATURE