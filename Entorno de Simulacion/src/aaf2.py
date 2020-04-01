from scipy import signal
import numpy as np


class AntiAlias:
    def __init__(self, filter_settings):
        self.fp = filter_settings["fp"]
        self.ap = filter_settings["ap"]
        self.fa = filter_settings["fa"]
        self.aa = filter_settings["aa"]
        self.num = []
        self.den = []
        self.compute_filter()
        self.system_discrete = []

    def compute_filter(self):
        self.num = [1]
        self.den = [7.06158917e-42, 3.04832881e-36, 1.08833832e-30, 2.47766922e-25, 4.41255356e-20, 5.70986892e-15,
               5.36562867e-10, 3.27584724e-05, 1.]

    def output(self, input_signal):
        t = input_signal["t"]
        x = input_signal["y"]
        dt = t[1] - t[0]
        self.system_discrete = signal.cont2discrete((self.num, self.den), dt)
        [tout, yout] = signal.dlsim(self.system_discrete, x, t)

        ret = dict()
        ret["t"] = tout
        ret["y"] = yout.squeeze()

        return ret

