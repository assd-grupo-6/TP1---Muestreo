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

from src.analog_switch import AnalogSwitch
from src.input_signal import InputSignal
from src.recov_filter import RecoveryFilter
from src.sample_hold import SampleAndHold


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
        # Create input signal
        self.input_signal = InputSignal(self.input_signal_settings)
        # Create Sample & Hold
        self.sample_and_hold = SampleAndHold()
        # Create Analog Switch
        self.analog_switch = AnalogSwitch()
        # Create recovery filter
        self.recovery_filter = RecoveryFilter()

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

        # nodes signals represented by a dict containing "t", "y"
        # "t" is the time vector
        # "y" is the time signal
        self.in_node = self.input_signal.get_signal_dict()
        self.aaf_node = dict()
        self.sample_hold_node = dict()
        self.analog_switch_node = dict()
        self.recov_filt_node = dict()


        # Connect widget signals
        self.sinWave_radioButton.toggled.connect(self.update_input_signal)
        self.altSinWaveform_RadioButton.toggled.connect(self.update_input_signal)
        self.squareWaveform_radioButton.toggled.connect(self.update_input_signal)
        self.inputSignalFreq_spinBox.valueChanged.connect(self.update_input_signal)

        self.inputSignalOut_checkBox.toggled.connect(self.update_plot)
        self.antiAliasOut_checkBox.toggled.connect(self.update_plot)
        self.sampleHoldOut_checkBox.toggled.connect(self.update_plot)
        self.analogSwitchOut_checkBox.toggled.connect(self.update_plot)
        self.recovFilterOut_checkBox.toggled.connect(self.update_plot)

        self.antiAliasStage_checkBox.toggled.connect(self.stages_changed)
        self.sampleHoldStage_checkBox.toggled.connect(self.stages_changed)
        self.analogSwitchStage_checkBox.toggled.connect(self.stages_changed)
        self.recovFilterStage_checkBox.toggled.connect(self.stages_changed)

        self.update_input_signal()

        # TODO: remove this
        np.random.seed(19680801)

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
        # get waveform
        for radioButton in self.input_signal_waveform_radioButtons:
            if radioButton.isChecked():
                waveform = radioButton.waveform
        # get frequency
        freq = self.inputSignalFreq_spinBox.value()

        #get amplitude
        amplitude = self.inputSignalAmp_spinBox.value()

        self.input_signal_settings["waveform"] = waveform
        self.input_signal_settings["freq"] = freq
        self.input_signal_settings["amplitude"] = amplitude

        self.input_signal = InputSignal(self.input_signal_settings)
        self.update_node_signals()

    def update_plot(self):
        # get output nodes settings
        self.output_settings["input-signal"] = self.inputSignalOut_checkBox.isChecked()
        self.output_settings["aaf"] = self.antiAliasOut_checkBox.isChecked()
        self.output_settings["sample-and-hold"] = self.sampleHoldOut_checkBox.isChecked()
        self.output_settings["analog-switch"] = self.analogSwitchOut_checkBox.isChecked()
        self.output_settings["recovery-filter"] = self.recovFilterOut_checkBox.isChecked()

        # TODO: implementar
        # Dummy plot to test
        self.figure.clf()
        self.figure_canvas.draw()
        self.axes = self.figure.add_subplot(111)

        if self.output_settings["input-signal"] is True:
            self.axes.plot(self.in_node["y"], label='random plot - input')
        if self.output_settings["aaf"] is True:
            self.axes.plot(self.aaf_node["y"], label='random plot - aaf')
        if self.output_settings["sample-and-hold"] is True:
            self.axes.plot(self.sample_hold_node["y"], label='random plot - s\&h')
        if self.output_settings["analog-switch"] is True:
            self.axes.plot(self.analog_switch_node["y"], label='random plot - analog switch')
        if self.output_settings["recovery-filter"] is True:
            self.axes.plot(self.recov_filt_node["y"], label='random plot - recovery filter')

        self.axes.legend()
        self.figure_canvas.draw()

    def stages_changed(self):
        self.stages_settings["aaf"] = self.antiAliasStage_checkBox.isChecked()
        self.stages_settings["sample-and-hold"] = self.sampleHoldStage_checkBox.isChecked()
        self.stages_settings["analog-switch"] = self.analogSwitchStage_checkBox.isChecked()
        self.stages_settings["recovery-filter"] = self.recovFilterStage_checkBox.isChecked()

        self.update_node_signals()

    def update_node_signals(self):
        # t_output method structure to implement.
        # for now may throw random
        if self.stages_settings["aaf"] is True:
            self.aaf_node = self.aaf.t_output(self.in_node)
        else:
            self.aaf_node = self.in_node

        if self.stages_settings["sample-and-hold"] is True:
            self.sample_hold_node = self.sample_and_hold.t_output(self.aaf_node)
        else:
            self.sample_hold_node = self.aaf_node

        if self.stages_settings["analog-switch"] is True:
            self.analog_switch_node = self.analog_switch.t_output(self.sample_hold_node)
        else:
            self.analog_switch_node = self.sample_hold_node

        if self.stages_settings["recovery-filter"] is True:
            self.recov_filt_node = self.recovery_filter.t_output(self.analog_switch_node)
        else:
            self.recov_filt_node = self.analog_switch_node

        self.update_plot()
