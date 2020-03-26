import numpy as np
from scipy import signal

class InputSignal:
    def __init__(self, input_signal_config):
        """

        :param input_signal_config: dict containing signal info
        """
        self.fc = input_signal_config["freq"]
        self.waveform = input_signal_config["waveform"]
        self.amplitude = input_signal_config["amplitude"]
        self.fs = input_signal_config["fs"]
        self.y = []
        self.y_norm = []
        self.t = []
        self.t_norm = []
        self.__compute_signal()

    def __compute_signal(self):
        if self.waveform == "sine":
            period = 1.0 / self.fc
            self.t = np.linspace(0, 2*period, 1000)
            self.t_norm = self.t / self.fs
            self.y = np.sin(2*np.pi*self.fc*self.t)
            self.y_norm = np.sin(2 * np.pi * self.fc * self.t_norm)
        elif self.waveform == "square":
            period = 1.0 / self.fc
            self.t = np.linspace(0, 2*period, 1000)
            self.t_norm = self.t / self.fs
            self.y = signal.square(2*np.pi*self.fc*self.t, 0.5)
            self.y_norm = signal.square(2 * np.pi * self.fc * self.t_norm, 0.5)
    def get_signal_dict(self):
        ret_dict = dict()
        ret_dict["t"] = self.t
        ret_dict["y"] = self.y
        return ret_dict
