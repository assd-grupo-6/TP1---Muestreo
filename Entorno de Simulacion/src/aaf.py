import numpy as np
from scipy import signal


class AntiAlias:
    def __init__(self, type=None, fc=0.01, n=2048):
        self.n = n
        self.fc = fc
        self.type = type
        if (type == 'real'):
            self.assignedFilter()

    def update(self):
        if (self.type == 'real'):
            filt = self.system.to_tf()
            self.system = signal.TransferFunction(*signal.lp2lp(filt.num, filt.den, wo=2 * np.pi * self.fc))

    def setCutFreq(self, f):
        if f >= 0.01:
            self.fc = f
        else:
            self.fc = 0.01

    def setType(self, type):
        switcher = {
            None: None,
            'real': 'real',
            'ideal': 'ideal',
        }
        self.type = switcher.get(type, lambda: None)

    def output(self, v):
        self.update()
        out = dict()
        Vin_f = np.fft.fftfreq(self.n, d=v['t'][-1] / (self.n))
        Vin_out = np.fft.fft(v['y'])
        if self.type == 'ideal':
            h = np.zeros(len(Vin_out))
            for idx in np.arange(0, len(Vin_out)):
                if (np.abs(Vin_f[idx]) <= self.fc):
                    h[idx] = 1
        elif self.type == None:
            h = np.ones(len(Vin_f))
        else:
            w, h = signal.freqresp(self.system, 2 * np.pi * Vin_f)
        self.Vout_out = h * Vin_out
        self.Vout_f = Vin_f

        out['y'] = (np.fft.ifft(self.Vout_out, n=self.n)).real
        out['t'] = v['t']

        return out

    def assignedFilter(self):
        p = np.array([-0.08446 + 1.018j, -0.2415 + 0.854j, -0.3706 + 0.5628j, -0.4485 + 0.1922j, -0.08446 - 1.018j,
                      -0.2415 - 0.854j, -0.3706 - 0.5628j, -0.4485 - 0.1922j])
        self.system = signal.TransferFunction(*signal.zpk2tf([], p, 1.))
        self.system.num = self.system.den[-1]

    def idealFilter(self):
        num, den = signal.butter(N=40, btype='low', Wn=1, analog=True, output='ba')
        self.system = signal.TransferFunction(num, den)

    def dataBodePlot(self):
        data = dict()
        mask = self.Vout_f >= 0
        y_f = 2 * np.abs(self.Vout_out / self.n)
        data['f'] = self.Vout_f[mask]
        data['out'] = y_f[mask]
        return data
