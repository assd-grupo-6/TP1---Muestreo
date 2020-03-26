import numpy as np


class AnalogSwitch():
    def __init__(self):
        np.random.seed(12312312)

    def t_output(self, input):
        """
        Given an input signal, the output filtered signal is computed
        :param input: input signal as a dict with fields t and y
        :return: the filtered signal
        :rtype:  dict
        """
        # TODO: dummy just return a random array
        t = input["t"]
        y = np.random.rand(len(t))
        ret = dict()
        ret["y"] = y
        ret["t"] = t
        return ret
