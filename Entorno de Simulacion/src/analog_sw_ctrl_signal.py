import numpy as np
from scipy import signal


class AnalogSwitchCtrlSignal:
    def __init__(self, analog_sw_settings):
        self.fc = analog_sw_settings["freq"]
        self.duty = analog_sw_settings["duty"]
        self.y = []
        self.t = []

    def get_signal(self, t):
        self.y = (signal.square(2*np.pi*self.fc * t, self.duty) + 1) / 2
        ret_dict = dict()
        ret_dict["t"] = t
        ret_dict["y"] = self.y
        return ret_dict
