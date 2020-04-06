import numpy as np


class AnalogSwitch:
    def __init__(self):
        self.controlSignal = dict()

    def output(self, input_signal, control):
        """
        Computes the Analog Switch output given an input signal and the control signal
        :param input_signal: data to be switched
        :param control: control signal. Square signal
        :return: returns the output signal in a dictionary format
        :rtype: dict
        """
        # Assumes input_signal and control have the same length
        t = input_signal["t"]
        sc = control["y"]
        x = input_signal["y"]
        y = []
        for i in range(0, len(t)):
            if sc[i] == 0:
                y.append(x[i])
            else:
                y.append(0)

        ret = dict()
        ret["t"] = t
        ret["y"] = y
        return ret

