from scipy import signal
import numpy as np


class AntiAlias:
    def __init__(self, filter_settings):
        self.fp = filter_settings["fp"]
        self.ap = filter_settings["ap"]
        self.fa = filter_settings["fa"]
        self.aa = filter_settings["aa"]

        self.system = []
        self.lti = []
        self.compute_filter()

    def compute_filter(self):
        # num, den = signal.butter(5, 2*np.pi * self.fp, 'low', analog=True, output='ba')
        num, den = signal.ellip(5, 1, 41, 2*np.pi * self.fp, 'low', analog=True, output='ba')
        self.system = signal.lti(num, den)

    def output(self, input):
        t = input["t"]
        x = input["y"]

        tout, y, x = signal.lsim(self.system, x, t)

        ret = dict()
        ret["t"] = tout
        ret["y"] = y

        return ret

