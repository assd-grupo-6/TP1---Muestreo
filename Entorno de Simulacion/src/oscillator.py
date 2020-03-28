import numpy as np
from scipy import signal


class Oscillator:
    def __init__(self, oscillator_config):
        """
        :param oscillator_config: dict containing signal info
        """
        self.fc = oscillator_config["freq"]
        self.waveform = oscillator_config["amplitude"]
        self.duty = oscillator_config["duty"]
        self.y = []
        self.t = []

    def get_signal(self, t):
        # TODO: verificar
        self.y = (signal.square(2 * np.pi * self.fc * t, self.duty) + 1)/2.
        ret_dict = dict()
        ret_dict["t"] = t
        ret_dict["y"] = self.y
        return ret_dict
