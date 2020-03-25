from src import design, aaf
import json
from PyQt5 import QtWidgets, QtGui
import numpy as np
from scipy import signal
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from distutils.spawn import find_executable
import matplotlib.pyplot as mpl


class Application(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.setupUi(self)
        # Parse configuration file
        self.config_path = "../config/config.json"
        self.configs = self.get_config()
        self.aaf_settings = self.configs["aaf-settings"]
        self.recovery_filter_settings = self.configs["recovery-filter-settings"]
        self.sampling_settings = self.configs["sampling-settings"]
        self.output_settings = self.configs["output-settings"]
        self.stages_settings = self.configs["stages-settings"]
        self.input_signal_settings = self.configs["input-signal"]
        self.widgets_settings = self.configs["widgets-parameters"]
        # Create AAF
        self.aaf = aaf.AAF(self.aaf_settings)

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
        self.axes = self.figure.add_subplot(111)

        # transfer settings to GUI
        self.transfer_settings_to_GUI()
        # Add 'waveform' field to input signal radio buttons
        self.sinWave_radioButton.waveform = "sine"
        self.altSinWaveform_RadioButton.waveform = "altsine"
        self.squareWaveform_radioButton.waveform = "square"
        # Define input signal radio buttons 'group'
        self.input_signal_waveform_radioButtons = [self.sinWave_radioButton, self.altSinWaveform_RadioButton, self.squareWaveform_radioButton]

        self.update_input_signal()

        # Connect widget signals
        self.sinWave_radioButton.toggled.connect(self.update_input_signal)
        self.altSinWaveform_RadioButton.toggled.connect(self.update_input_signal)
        self.squareWaveform_radioButton.toggled.connect(self.update_input_signal)
        self.inputSignalFreq_spinBox.valueChanged.connect(self.update_input_signal)


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
        samp_mode = self.sampling_settings["mode"]
        if samp_mode == "natural":
            self.naturalSampling_radioButton.setChecked(True)
        elif samp_mode == "instantaneous":
            self.instSampling_radioButton.setChecked(True)

        self.sampleRat_spinBox.setValue(self.sampling_settings["sample-rate"])
        self.sampleCycle_spinBox.setValue(self.sampling_settings["duty-cycle"])

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

    def update_input_signal(self):
        for radioButton in self.input_signal_waveform_radioButtons:
            if radioButton.isChecked():
                waveform = radioButton.waveform
        freq = self.inputSignalFreq_spinBox.value()
        amp = self.inputSignalAmp_spinBox.value()
        fs = self.input_signal_settings["fs"]

        if waveform == "sine":
            period = 1.0 / freq
            t = np.arange(1000) / fs
            self.time_vect = t
            self.input_signal = np.sin(2*np.pi*freq*t)
        elif waveform == "square":
            period = 1.0 / freq
            t = np.arange(freq) / fs
            self.time_vect = t
            self.input_signal = signal.square(2*np.pi*freq*t, 0.5)
        elif waveform == "3/2sin":
            period = 1.5 / freq
            t = np.linspace(0, period, 1000) /fs
            self.time_vect = t
            wave = np.sin(2*np.pi*freq*t)
            wave= wave + wave
            self.input_signal = []
            for item in np.nditer(wave):
                self.input_signal.append(amp * item)

        # Dummy plot to test
        self.figure.clf()
        self.figure_canvas.draw()
        self.axes = self.figure.add_subplot(111)
        b, a = self.aaf.transfer_function()
        y_out = signal.filtfilt(b, a, self.input_signal)
        self.axes.plot(self.time_vect, self.input_signal, label='in')
        self.axes.plot(self.time_vect, y_out, label='out')
        self.axes.legend()
        self.figure_canvas.draw()

