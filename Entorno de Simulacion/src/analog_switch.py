import numpy as np


class AnalogSwitch():
    def __init__(self):
        self.controlSignal = dict()



    def output(self, input, control):
        """
        Given an input signal, the output filtered signal is computed
        :param input: input signal as a dict with fields t and y
        :param control: control signal as a dict with fields t and y
        :return: the filtered signal
        :rtype:  dict
        """
        ti = input["t"]
        tc = control["t"]
        if ti.any() == tc.any():
            ret = dict()
            if control["y"].any() == 0:
                ret["y"] = 0
            else:
                ret["y"] = input["y"]
            ret["t"] = ti
            return ret
        else:
            raise ValueError("Analog switch error: signal and control inputs out of sync")
