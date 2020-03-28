
class SampleAndHold:
    def __init__(self, prevValue = 0): #En caso de que el valor previo del sample and hold sea distinto de 0, indicar.
        self.preValue = prevValue
        return

    def output(self, analogInput, digitalClockInput): #Recibe 2 señales como diccionarios, la señal del oscilador digital, y la señal analógica
                                                        #Ambas señales deben tener los mismos vectores de tiempo.
            """                                         
            Given an input signal, the output filtered signal is computed
            :param input: input signal as a dict with fields t and y
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


def test():
    SH = SampleAndHold()
    y = [0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0]
    z = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1]
    t = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
    ret = dict()
    ret2 = dict()
    ret["y"] = y
    ret["t"] = t
    ret2["y"] = z
    ret2["t"] = t

    x = SH.output(ret,ret2)
    print(x["y"])

#test()