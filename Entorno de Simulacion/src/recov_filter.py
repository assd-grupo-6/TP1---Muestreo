from scipy import signal
import numpy as np


class RecoveryFilter:
    def __init__(self, filter_settings):
        self.fp = filter_settings["fp"]
        self.ap = filter_settings["ap"]
        self.fa = filter_settings["fa"]
        self.aa = filter_settings["aa"]
        self.num = []
        self.den = []
        self.compute_filter()

    def compute_filter(self):
        wp = 2 * np.pi * self.fp
        wa = 2 * np.pi * self.fa
        order, wn = signal.cheb2ord(wp, wa, 1, 50, analog=True)
        self.num, self.den = signal.cheby2(order, 50, wn, 'lowpass', analog=True, output='ba')

    def output(self, input_signal):
        t = input_signal["t"]
        x = input_signal["y"]
        dt = t[1] - t[0]

        # self.system_discrete = signal.cont2discrete((self.num, self.den), dt)
        # [tout, yout] = signal.dlsim(self.system_discrete, x, t)
        (num, den, dt) = signal.cont2discrete((self.num, self.den), dt)
        yout = signal.filtfilt(num.squeeze(), den.squeeze(), x)

        ret = dict()
        ret["t"] = t
        ret["y"] = yout

        return ret
