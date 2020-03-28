import numpy as np


class RecoveryFilter():
    def __init__(self):
        np.random.seed(12312312)

    def output(self, input_signal):
        """
        Given an input signal, the output filtered signal is computed
        :param input_signal: input signal as a dict with fields t and y
        :return: the filtered signal
        :rtype:  dict
        """
        # TODO: dummy just return a random array
        t = input_signal["t"]
        y = np.random.rand(len(t))
        ret = dict()
        ret["y"] = y
        ret["t"] = t
        return ret
