import numpy as np
from scipy import signal

class AAF:
    """
    Implements the low-pass filter that acts as the Anti Aliasing Filter of the system
    :param aaf_config: parameter containing AAF settings
    :type aaf_config: dict
    """
    def __init__(self, aaf_config):
        # pass band frequency
        self.fp = aaf_config["fp"]
        # pass band attenuation
        self.ap = aaf_config["ap"]
        # attenuated band frequency
        self.fa = aaf_config["fa"]
        # attenuated band attenuation
        self.aa = aaf_config["aa"]
        # sampling freq
        self.fs = aaf_config["fs"]
        self.sos = self.second_order_stages()

    def second_order_stages(self):
        n, wn = signal.ellipord(2*np.pi*self.fp, 2*np.pi*self.fa, self.ap, self.aa, analog=True)
        sos = signal.ellip(n, self.ap, self.aa, wn, 'low', analog=True, output='sos')
        return sos

    def transfer_function(self):
        w = self.fp/(self.fs/2)
        b, a = signal.butter(5, w, 'low')

        return b, a

    def get_numeric_output(self, t, s_in):
        """
        Given an input signal, the output filtered signal is computed
        :param t: time vector
        :param s_in: input signal vector
        :return: the filtered signal
        :rtype: list of complex
        """
        filtered = signal.sosfilt(self.sos, s_in)
        return filtered
