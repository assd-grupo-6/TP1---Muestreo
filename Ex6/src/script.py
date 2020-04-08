import matplotlib.pyplot as plt
from distutils.spawn import find_executable
import re
import numpy as np
import json


items = ['a', 'b1', 'b2', 'c', 'd']
signals = ['xa', 'xb', 'xc']

for item in items:
    for signal in signals:
        path = item + '/' + signal + '/'
        time_path = path + 'spice'
        freq_path = path + 'spice_freq'

        try:
            f= []
            spectrum1 = []
            spectrum2 = []
            t = []
            y1 = []
            y2 = []

            config_path = path + 'settings.json'
            data = dict()
            with(open(config_path)) as config_file:
                data = json.load(config_file)
            fs = data["fs"]
            dc = data["dc"]
            fin = data["fin"]

            with open(freq_path) as freq_file:
                freq_data_lines = freq_file.readlines()
                pattern = '\((.*)d'
                for line in freq_data_lines[1:]:
                    f.append(float(line.split('\t')[0]))
                    spectrum1.append(float(re.search(pattern, line.split('\t')[1]).group(1)))
                    spectrum2.append(float(re.search(pattern, line.split('\t')[2]).group(1)))

            with open(time_path) as time_file:
                time_data_lines = time_file.readlines()
                for line in time_data_lines[1:]:
                    t.append(float(line.split('\t')[0]))
                    y1.append(float(line.split('\t')[1]))
                    y2.append(float(line.split('\t')[2]))

            if find_executable('latex'):
                plt.rc('font', **{'family': 'serif', 'serif': ['Palatino']})
                plt.rc('text', usetex=True)

            fig = plt.figure(figsize=(16,9))
            axes = fig.subplots(2,1)
            t_axes = axes[0]
            f_axes = axes[1]


            t_axes.set_title('Time Domain')
            t_axes.set_xlabel('Time [seg]')
            t_axes.set_ylabel('Amplitde [V]')
            t_axes.plot(t, y1, label='Input Signal')
            t_axes.plot(t, y2, label='Recovery Filter')
            t_axes.legend(loc='upper right')
            t_axes.grid('minor')

            f_axes.semilogx(f, spectrum1, label='Input Signal')
            f_axes.semilogx(f, spectrum2, label='Recovery Filter')
            f_axes.set_xlabel('Frequency [Hz]')
            f_axes.set_ylabel('Mag')
            f_axes.grid('minor')
            f_axes.legend(loc='upper right')


            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed') #works fine on Windows!
            plt.show()
            filename = path + 'fs_' + str(fs) + '_fin_' + str(fin) + '_dc_' + str(dc) + '.pdf'
            fig.savefig(filename)
            fig.clf()
        except:
            pass
        finally:
            pass