class SampleAndHold:
    def __init__(self, prevValue=0):  # En caso de que el valor previo del sample and hold sea distinto de 0, indicar.
        self.preValue = prevValue
        return

    def output(self, analogInput,
               digitalClockInput):  # Recibe 2 señales como diccionarios, la señal del oscilador digital, y la señal analógica
        # Ambas señales deben tener los mismos vectores de tiempo.
        """
        Given an input signal, the output filtered signal is computed
        :param analogInput: input signal as a dict with fields t and y
        :param digitalClockInput: oscillator signal
        :return: the filtered signal
        :rtype:  dict
        """
        out = []
        if len(analogInput["t"]) == len(digitalClockInput["t"]):
            a = digitalClockInput["y"]
            b = analogInput["y"]
            for i in range(len(a)):
                if a[i] != 0:
                    out.append(b[i])
                    self.preValue = b[i]
                else:
                    out.append(self.preValue)

        t = analogInput["t"]
        ret = dict()
        ret["y"] = out
        ret["t"] = t
        return ret
