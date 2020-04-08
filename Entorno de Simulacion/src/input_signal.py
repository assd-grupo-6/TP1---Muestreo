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
        self.y = []
        self.t = []
        self.__compute_signal()

    def __compute_signal(self):
        if self.waveform == "sine":
            period = 1.0 / self.fc
            self.t = np.linspace(0, 4*period, 1000)
            self.y = self.amplitude * np.sin(2*np.pi*self.fc*self.t)
        elif self.waveform == "square":
            period = 1.0 / self.fc
            self.t = np.linspace(0, 4*period, 1000)
            self.y = self.amplitude * signal.square(2*np.pi*self.fc*self.t, 0.5)
        elif self.waveform == "altsine":
            period = 1.5 / self.fc
            self.t = np.linspace(0, 4*period, 1000)
            t_i = self.amplitude * np.linspace(0, period, 100)
            y_i = self.amplitude * np.sin(2*np.pi*self.fc*t_i)
            for i in range(0, 10):
                for element in y_i:
                    self.y.append(element)
        elif self.waveform == "Xc":
            fm = 0.2 * self.fc
            fp = 2 * self.fc
            m = 0.5
            period = 1/fm
            self.t = np.linspace(0, period, 1000)
            ym = np.cos(2*np.pi*fm*self.t)
            yp = np.cos(2*np.pi*fp*self.t)
            self.y = np.cos(2*np.pi*1.8*fp*self.t) + 2*np.cos(2*np.pi*2*fp*self.t) + np.cos(2*np.pi*2.2*fp*self.t)
            # self.y = self.amplitude * (m * ym + 1)*yp

    def get_signal_dict(self):
        ret_dict = dict()
        ret_dict["t"] = self.t
        ret_dict["y"] = self.y
        return ret_dict
