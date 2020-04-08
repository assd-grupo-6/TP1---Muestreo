import matplotlib.pyplot as plt
from distutils.spawn import find_executable
import re
import numpy as np

freq_path = 'b/35200_s&h.txt'
time_path = 'b/35200_s&h_t.txt'

f= []
spectrum = []
t = []
y1 = []
y2 = []

with open(freq_path) as freq_file:
    freq_data_lines = freq_file.readlines()
    pattern = '\((.*)d'
    for line in freq_data_lines:
        f.append(float(line.split('\t')[0]))
        spectrum.append(float(re.search(pattern, line).group(1)))

with open(time_path) as time_file:
    time_data_lines = time_file.readlines()
    for line in time_data_lines:
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
t_axes.plot(t, y2, label='Analog Switch Signal')
t_axes.legend(loc='upper right')
t_axes.grid('minor')

f_axes.plot(f, spectrum, label='Analog Switch')
f_axes.set_xlabel('Frequency [Hz]')
f_axes.set_ylabel('Mag')
f_axes.set_xlim([0, 70e3])
f_axes.set_ylim([-80, -15])
f_axes.grid('minor')
# Pintar regiones
B = 9.6e3
fs = 35200
fc = 48e3
lims = f_axes.get_ylim()
# primera rep
fc1 = fs/2 - B/2   
fc2 = fs/2 + B/2
f_axes.fill_betweenx(lims, fc1 - 1.5*B/2, fc1 + B/2,
                    color='green', alpha=0.3, label='$1^{st}$ Repetition')
# segunda rep
f_axes.fill_betweenx(lims, fc2 - B/2, fc2 + B/2,
                    color='yellow', alpha=0.3, label='$2^{nd}$ Repetition')
# espectro principal
f_axes.fill_betweenx(lims, fc - 1.5*B/2, fc + 1.5*B/2,
                    color='blue', alpha=0.3, label='Original Spectrum')
f_axes.legend(loc='upper right')

mng = plt.get_current_fig_manager()
### works on Ubuntu??? >> did NOT working on windows
# mng.resize(*mng.window.maxsize())
mng.window.state('zoomed') #works fine on Windows!
filename = 'b/' + str(fs) + '_s&h.pdf'
fig.savefig(filename)
plt.show() #close the figure to run the next section
