from PyQt5.QtWidgets import QFileDialog

from src import design
import json
from PyQt5 import QtWidgets, QtGui
import numpy as np
from scipy.fftpack import fft, fftfreq
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from distutils.spawn import find_executable
import matplotlib.pyplot as mpl

from src.aaf2 import AntiAlias
from src.analog_sw_ctrl_signal import AnalogSwitchCtrlSignal
from src.analog_switch import AnalogSwitch
from src.input_signal import InputSignal
from src.recov_filter import RecoveryFilter
from src.sample_hold import SampleAndHold
from src.oscillator import Oscillator


class Application(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.setupUi(self)
        # Parse configuration file
        self.config_path = "../config/config.json"
        self.configs = self.get_config()
        self.aaf_settings = self.configs["aaf-settings"]
        self.recovery_filter_settings = self.configs["recovery-filter-settings"]
        self.output_settings = self.configs["output-settings"]
        self.oscillator_settings = self.configs["oscillator"]
        self.stages_settings = self.configs["stages-settings"]
        self.input_signal_settings = self.configs["input-signal"]
        self.widgets_settings = self.configs["widgets-parameters"]
        self.system_settings = self.configs["system-settings"]
        # Create AAF
        self.aaf = AntiAlias(self.aaf_settings)
        # Create input signal
        self.input_signal = InputSignal(self.input_signal_settings)
        # Create Sample & Hold
        self.sample_and_hold = SampleAndHold()
        # Create Analog Switch
        self.analog_switch = AnalogSwitch()
        # Create recovery filter
        self.recovery_filter = RecoveryFilter(self.recovery_filter_settings)
        # Create Oscillator
        self.oscillator = Oscillator(self.oscillator_settings)
        # Create Analog Switch Control Signal
        # Same frequency as the oscillator, lower duty cycle
        self.as_ctrl_signal_settings = dict()
        self.as_ctrl_signal_settings["freq"] = self.oscillator_settings["freq"]
        self.as_ctrl_signal_settings["duty"] = self.oscillator_settings["duty"] * self.system_settings["as-ctrl-duty"]
        self.analog_switch_ctrl_signal = AnalogSwitchCtrlSignal(self.as_ctrl_signal_settings)

        # Setup Matplotlib
        if find_executable('latex'):
            mpl.rc('font', **{'family': 'serif', 'serif': ['Palatino']})
            mpl.rc('text', usetex=True)
        # Create Figure
        self.figure = Figure()
        self.figure_canvas = FigureCanvas(self.figure)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.figure_canvas.setSizePolicy(size_policy)
        self.figureLayout.addWidget(self.figure_canvas)
        self.time_axes = self.figure.add_subplot(211)
        self.freq_axes = self.figure.add_subplot(212)

        # transfer settings to GUI
        self.transfer_settings_to_GUI()
        # Add 'waveform' field to input signal radio buttons
        self.sinWave_radioButton.waveform = "sine"
        self.altSinWaveform_RadioButton.waveform = "altsine"
        self.squareWaveform_radioButton.waveform = "square"
        # Define input signal radio buttons 'group'
        self.input_signal_waveform_radioButtons = [self.sinWave_radioButton,
                                                   self.altSinWaveform_RadioButton,
                                                   self.squareWaveform_radioButton]

        # nodes signals represented by a dict containing "t", "y"
        # "t" is the time vector
        # "y" is the time signal
        self.in_node = self.input_signal.get_signal_dict()
        self.aaf_node = dict()
        self.sample_hold_node = dict()
        self.analog_switch_node = dict()
        self.recov_filt_node = dict()

        # TODO: Deberia tener un vector de tiempo global? o lo saco de la input signal?

        # Connect widget signals
        self.sinWave_radioButton.toggled.connect(self.update_input_signal)
        self.altSinWaveform_RadioButton.toggled.connect(self.update_input_signal)
        self.squareWaveform_radioButton.toggled.connect(self.update_input_signal)
        self.updateInput_pushButton.clicked.connect(self.update_input_signal)

        self.updateSampe_pushButton.clicked.connect(self.update_oscillator)

        self.inputSignalOut_checkBox.toggled.connect(self.update_plots)
        self.antiAliasOut_checkBox.toggled.connect(self.update_plots)
        self.sampleHoldOut_checkBox.toggled.connect(self.update_plots)
        self.analogSwitchOut_checkBox.toggled.connect(self.update_plots)
        self.recovFilterOut_checkBox.toggled.connect(self.update_plots)

        self.antiAliasStage_checkBox.toggled.connect(self.stages_changed)
        self.sampleHoldStage_checkBox.toggled.connect(self.stages_changed)
        self.analogSwitchStage_checkBox.toggled.connect(self.stages_changed)
        self.recovFilterStage_checkBox.toggled.connect(self.stages_changed)

        self.exportPlots_pushButton.clicked.connect(self.export_plots)

        self.update_input_signal()

    def transfer_settings_to_GUI(self):
        # Widgets Parameters
        self.inputSignalFreq_spinBox.setMinimum(self.widgets_settings["input-freq-low"])
        self.inputSignalFreq_spinBox.setMaximum(self.widgets_settings["input-freq-high"])
        self.sampleRat_spinBox.setMaximum(self.widgets_settings["sample-rate-high"])
        self.sampleRat_spinBox.setMinimum(self.widgets_settings["sample-rate-low"])

        # input Signal
        waveform = self.input_signal_settings["waveform"]
        if waveform == "sine":
            self.sinWave_radioButton.setChecked(True)
        elif waveform == "alt-sin":
            self.altSinWaveform_RadioButton.setChecked(True)
        elif waveform == "square":
            self.squareWaveform_radioButton.setChecked(True)
        self.inputSignalFreq_spinBox.setValue(self.input_signal_settings["freq"])
        self.inputSignalAmp_spinBox.setValue(self.input_signal_settings["amplitude"])

        # Sampling
        self.sampleRat_spinBox.setValue(self.oscillator_settings["freq"])
        self.sampleCycle_spinBox.setValue(self.oscillator_settings["duty"])

        # Stages
        self.antiAliasStage_checkBox.setChecked(self.stages_settings["aaf"])
        self.sampleHoldStage_checkBox.setChecked(self.stages_settings["sample-and-hold"])
        self.analogSwitchStage_checkBox.setChecked(self.stages_settings["analog-switch"])
        self.recovFilterStage_checkBox.setChecked(self.stages_settings["recovery-filter"])

        # Outputs
        self.inputSignalOut_checkBox.setChecked(self.output_settings["input-signal"])
        self.antiAliasOut_checkBox.setChecked(self.output_settings["aaf"])
        self.sampleHoldOut_checkBox.setChecked(self.output_settings["sample-and-hold"])
        self.analogSwitchOut_checkBox.setChecked(self.output_settings["analog-switch"])
        self.recovFilterOut_checkBox.setChecked(self.output_settings["recovery-filter"])

    def get_config(self):
        """
        :return: Nested dictionary with configurations
        :rtype: dict
        """
        with(open(self.config_path)) as config_file:
            data = json.load(config_file)
            return data

    def update_oscillator(self):
        self.oscillator_settings["freq"] = self.sampleRat_spinBox.value()
        self.oscillator_settings["duty"] = self.sampleCycle_spinBox.value()
        self.oscillator = Oscillator(self.oscillator_settings)
        # Update AS Ctrl Signal
        self.as_ctrl_signal_settings["freq"] = self.oscillator_settings["freq"]
        self.as_ctrl_signal_settings["duty"] = self.oscillator_settings["duty"] * self.system_settings["as-ctrl-duty"]
        self.analog_switch_ctrl_signal = AnalogSwitchCtrlSignal(self.as_ctrl_signal_settings)

        self.update_node_signals()

    def update_input_signal(self):
        # get waveform
        for radioButton in self.input_signal_waveform_radioButtons:
            if radioButton.isChecked():
                self.input_signal_settings["waveform"] = radioButton.waveform
        # get frequency
        freq = self.inputSignalFreq_spinBox.value()
        self.input_signal_settings["freq"] = freq

        # get amplitude
        amplitude = self.inputSignalAmp_spinBox.value()
        self.input_signal_settings["amplitude"] = amplitude

        self.input_signal = InputSignal(self.input_signal_settings)

        # must update oscillator. this method updates AS Ctrl Signal and then calls to update nodes
        self.update_oscillator()

    def update_f_plots(self):
        if self.output_settings["input-signal"] is True:
            spectrum = self.get_spectrum(self.in_node)
            self.freq_axes.semilogx(spectrum["f"], spectrum["psd"], label='Input Signal')
        if self.output_settings["aaf"] is True:
            spectrum = self.get_spectrum(self.aaf_node)
            self.freq_axes.semilogx(spectrum["f"], spectrum["psd"], label='Anti Alias Filter')
        if self.output_settings["sample-and-hold"] is True:
            spectrum = self.get_spectrum(self.sample_hold_node)
            self.freq_axes.semilogx(spectrum["f"], spectrum["psd"], label='Sample \& Hold Signal')
        if self.output_settings["analog-switch"] is True:
            spectrum = self.get_spectrum(self.analog_switch_node)
            self.freq_axes.semilogx(spectrum["f"], spectrum["psd"], label='Analog Switch Signal')
        if self.output_settings["recovery-filter"] is True:
            spectrum = self.get_spectrum(self.recov_filt_node)
            self.freq_axes.semilogx(spectrum["f"], spectrum["psd"], label='Recovery Filter Signal')

        self.freq_axes.legend(loc='upper right')

    def update_t_plot(self):
        t = self.in_node["t"]

        if self.output_settings["input-signal"] is True:
            self.time_axes.plot(t, self.in_node["y"], label='Input Signal')
        if self.output_settings["aaf"] is True:
            self.time_axes.plot(t, self.aaf_node["y"], label='Anti Alias Filter Signal')
        if self.output_settings["sample-and-hold"] is True:
            self.time_axes.plot(t, self.sample_hold_node["y"], label='Sample \& Hold Signal')
        if self.output_settings["analog-switch"] is True:
            self.time_axes.plot(t, self.analog_switch_node["y"], label='Analog Switch Signal')
        if self.output_settings["recovery-filter"] is True:
            self.time_axes.plot(t, self.recov_filt_node["y"], label='Recovery Filter Signal')

        self.time_axes.legend(loc='upper right')

    def update_plots(self):
        # get output nodes settings
        self.output_settings["input-signal"] = self.inputSignalOut_checkBox.isChecked()
        self.output_settings["aaf"] = self.antiAliasOut_checkBox.isChecked()
        self.output_settings["sample-and-hold"] = self.sampleHoldOut_checkBox.isChecked()
        self.output_settings["analog-switch"] = self.analogSwitchOut_checkBox.isChecked()
        self.output_settings["recovery-filter"] = self.recovFilterOut_checkBox.isChecked()

        self.figure.clf()
        self.figure_canvas.draw()
        self.time_axes = self.figure.add_subplot(211)
        self.freq_axes = self.figure.add_subplot(212)
        self.update_t_plot()
        self.update_f_plots()

        self.time_axes.grid('minor')
        self.time_axes.set_title("Time Domain")
        self.time_axes.set_xlabel("Time [sec]")
        self.time_axes.set_ylabel("Amplitude [V]")

        self.freq_axes.grid('minor')
        self.freq_axes.set_title("Frequency Domain")
        self.freq_axes.set_xlabel("Frequency [Hz]")
        self.freq_axes.set_ylabel("Mag")
        self.figure_canvas.draw()

    def get_spectrum(self, input_signal, bilateral=False):
        y = input_signal["y"]
        t = input_signal["t"]
        signal_fft = fft(y, n=10000)
        # signal power spectral density
        signal_psd = np.abs(signal_fft)
        # get frequencies corresponding to psd
        dt = t[1] - t[0]
        f = fftfreq(len(signal_psd), dt)
        # get positive half of frequencies
        i = f > 0

        ret = dict()
        if bilateral:
            ret["psd"] = signal_psd
            ret["f"] = f
        else:
            ret["psd"] = signal_psd[i] / 10000
            ret["f"] = f[i]
        return ret

    def stages_changed(self):
        self.stages_settings["aaf"] = self.antiAliasStage_checkBox.isChecked()
        self.stages_settings["sample-and-hold"] = self.sampleHoldStage_checkBox.isChecked()
        self.stages_settings["analog-switch"] = self.analogSwitchStage_checkBox.isChecked()
        self.stages_settings["recovery-filter"] = self.recovFilterStage_checkBox.isChecked()

        self.update_node_signals()

    def update_node_signals(self):
        self.in_node = self.input_signal.get_signal_dict()

        if self.stages_settings["aaf"] is True:
            self.aaf_node = self.aaf.output(self.in_node)
        else:
            self.aaf_node = self.in_node

        t = self.in_node["t"]

        if self.stages_settings["sample-and-hold"] is True:
            self.sample_hold_node = self.sample_and_hold.output(self.aaf_node,
                                                                self.analog_switch_ctrl_signal.get_signal(t))
        else:
            self.sample_hold_node = self.aaf_node

        if self.stages_settings["analog-switch"] is True:
            self.analog_switch_node = self.analog_switch.output(self.sample_hold_node, self.oscillator.get_signal(t))
        else:
            self.analog_switch_node = self.sample_hold_node

        if self.stages_settings["recovery-filter"] is True:
            self.recov_filt_node = self.aaf.output(self.analog_switch_node)
        else:
            self.recov_filt_node = self.analog_switch_node

        self.update_plots()

    def export_plots(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()",
                                                   "", "PDF (*.pdf);;All Files (*)", options=options)
        if file_name:
            self.figure.savefig(file_name + '.pdf', bbox_inches='tight')
