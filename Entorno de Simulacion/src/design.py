# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1044, 909)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mainGridLayout = QtWidgets.QGridLayout()
        self.mainGridLayout.setObjectName("mainGridLayout")
        self.conf_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conf_groupBox.sizePolicy().hasHeightForWidth())
        self.conf_groupBox.setSizePolicy(sizePolicy)
        self.conf_groupBox.setObjectName("conf_groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.conf_groupBox)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.conf_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.antiAliasStage_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.antiAliasStage_checkBox.sizePolicy().hasHeightForWidth())
        self.antiAliasStage_checkBox.setSizePolicy(sizePolicy)
        self.antiAliasStage_checkBox.setObjectName("antiAliasStage_checkBox")
        self.gridLayout_3.addWidget(self.antiAliasStage_checkBox, 1, 0, 1, 1)
        self.sampleHoldStage_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sampleHoldStage_checkBox.sizePolicy().hasHeightForWidth())
        self.sampleHoldStage_checkBox.setSizePolicy(sizePolicy)
        self.sampleHoldStage_checkBox.setObjectName("sampleHoldStage_checkBox")
        self.gridLayout_3.addWidget(self.sampleHoldStage_checkBox, 2, 0, 1, 1)
        self.recovFilterStage_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recovFilterStage_checkBox.sizePolicy().hasHeightForWidth())
        self.recovFilterStage_checkBox.setSizePolicy(sizePolicy)
        self.recovFilterStage_checkBox.setObjectName("recovFilterStage_checkBox")
        self.gridLayout_3.addWidget(self.recovFilterStage_checkBox, 4, 0, 1, 1)
        self.analogSwitchStage_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analogSwitchStage_checkBox.sizePolicy().hasHeightForWidth())
        self.analogSwitchStage_checkBox.setSizePolicy(sizePolicy)
        self.analogSwitchStage_checkBox.setObjectName("analogSwitchStage_checkBox")
        self.gridLayout_3.addWidget(self.analogSwitchStage_checkBox, 3, 0, 1, 1)
        self.inputSignalOut_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputSignalOut_checkBox.sizePolicy().hasHeightForWidth())
        self.inputSignalOut_checkBox.setSizePolicy(sizePolicy)
        self.inputSignalOut_checkBox.setObjectName("inputSignalOut_checkBox")
        self.gridLayout_3.addWidget(self.inputSignalOut_checkBox, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.conf_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.antiAliasOut_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.antiAliasOut_checkBox.sizePolicy().hasHeightForWidth())
        self.antiAliasOut_checkBox.setSizePolicy(sizePolicy)
        self.antiAliasOut_checkBox.setObjectName("antiAliasOut_checkBox")
        self.gridLayout_9.addWidget(self.antiAliasOut_checkBox, 0, 0, 1, 1)
        self.analogSwitchOut_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analogSwitchOut_checkBox.sizePolicy().hasHeightForWidth())
        self.analogSwitchOut_checkBox.setSizePolicy(sizePolicy)
        self.analogSwitchOut_checkBox.setObjectName("analogSwitchOut_checkBox")
        self.gridLayout_9.addWidget(self.analogSwitchOut_checkBox, 2, 0, 1, 1)
        self.sampleHoldOut_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sampleHoldOut_checkBox.sizePolicy().hasHeightForWidth())
        self.sampleHoldOut_checkBox.setSizePolicy(sizePolicy)
        self.sampleHoldOut_checkBox.setObjectName("sampleHoldOut_checkBox")
        self.gridLayout_9.addWidget(self.sampleHoldOut_checkBox, 1, 0, 1, 1)
        self.recovFilterOut_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recovFilterOut_checkBox.sizePolicy().hasHeightForWidth())
        self.recovFilterOut_checkBox.setSizePolicy(sizePolicy)
        self.recovFilterOut_checkBox.setObjectName("recovFilterOut_checkBox")
        self.gridLayout_9.addWidget(self.recovFilterOut_checkBox, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.conf_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.naturalSampling_radioButton = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.naturalSampling_radioButton.sizePolicy().hasHeightForWidth())
        self.naturalSampling_radioButton.setSizePolicy(sizePolicy)
        self.naturalSampling_radioButton.setObjectName("naturalSampling_radioButton")
        self.gridLayout_10.addWidget(self.naturalSampling_radioButton, 0, 0, 1, 1)
        self.instSampling_radioButton = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instSampling_radioButton.sizePolicy().hasHeightForWidth())
        self.instSampling_radioButton.setSizePolicy(sizePolicy)
        self.instSampling_radioButton.setObjectName("instSampling_radioButton")
        self.gridLayout_10.addWidget(self.instSampling_radioButton, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_12.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_12.addWidget(self.label_2, 2, 0, 1, 1)
        self.sampleRat_spinBox = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sampleRat_spinBox.sizePolicy().hasHeightForWidth())
        self.sampleRat_spinBox.setSizePolicy(sizePolicy)
        self.sampleRat_spinBox.setObjectName("sampleRat_spinBox")
        self.gridLayout_12.addWidget(self.sampleRat_spinBox, 1, 1, 1, 1)
        self.sampleCycle_spinBox = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sampleCycle_spinBox.sizePolicy().hasHeightForWidth())
        self.sampleCycle_spinBox.setSizePolicy(sizePolicy)
        self.sampleCycle_spinBox.setMaximum(1.0)
        self.sampleCycle_spinBox.setObjectName("sampleCycle_spinBox")
        self.gridLayout_12.addWidget(self.sampleCycle_spinBox, 2, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.conf_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.squareWaveform_radioButton = QtWidgets.QRadioButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.squareWaveform_radioButton.sizePolicy().hasHeightForWidth())
        self.squareWaveform_radioButton.setSizePolicy(sizePolicy)
        self.squareWaveform_radioButton.setObjectName("squareWaveform_radioButton")
        self.gridLayout_17.addWidget(self.squareWaveform_radioButton, 2, 0, 1, 1)
        self.altSinWaveform_RadioButton = QtWidgets.QRadioButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.altSinWaveform_RadioButton.sizePolicy().hasHeightForWidth())
        self.altSinWaveform_RadioButton.setSizePolicy(sizePolicy)
        self.altSinWaveform_RadioButton.setObjectName("altSinWaveform_RadioButton")
        self.gridLayout_17.addWidget(self.altSinWaveform_RadioButton, 1, 0, 1, 1)
        self.sinWave_radioButton = QtWidgets.QRadioButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sinWave_radioButton.sizePolicy().hasHeightForWidth())
        self.sinWave_radioButton.setSizePolicy(sizePolicy)
        self.sinWave_radioButton.setObjectName("sinWave_radioButton")
        self.gridLayout_17.addWidget(self.sinWave_radioButton, 0, 0, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_17, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_7, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_15.addWidget(self.label_3, 1, 0, 1, 1)
        self.inputSignalFreq_spinBox = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputSignalFreq_spinBox.sizePolicy().hasHeightForWidth())
        self.inputSignalFreq_spinBox.setSizePolicy(sizePolicy)
        self.inputSignalFreq_spinBox.setObjectName("inputSignalFreq_spinBox")
        self.gridLayout_15.addWidget(self.inputSignalFreq_spinBox, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_15.addWidget(self.label_4, 2, 0, 1, 1)
        self.inputSignalAmp_spinBox = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputSignalAmp_spinBox.sizePolicy().hasHeightForWidth())
        self.inputSignalAmp_spinBox.setSizePolicy(sizePolicy)
        self.inputSignalAmp_spinBox.setObjectName("inputSignalAmp_spinBox")
        self.gridLayout_15.addWidget(self.inputSignalAmp_spinBox, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.mainGridLayout.addWidget(self.conf_groupBox, 0, 0, 2, 1)
        self.figureLayout = QtWidgets.QVBoxLayout()
        self.figureLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.figureLayout.setObjectName("figureLayout")
        self.mainGridLayout.addLayout(self.figureLayout, 0, 1, 2, 1)
        self.gridLayout_2.addLayout(self.mainGridLayout, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1044, 26))
        self.menubar.setObjectName("menubar")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConfig_AAF_Settings = QtWidgets.QAction(MainWindow)
        self.actionConfig_AAF_Settings.setObjectName("actionConfig_AAF_Settings")
        self.actionRecovery_Filter_Settings = QtWidgets.QAction(MainWindow)
        self.actionRecovery_Filter_Settings.setObjectName("actionRecovery_Filter_Settings")
        self.menuTools.addAction(self.actionConfig_AAF_Settings)
        self.menuTools.addAction(self.actionRecovery_Filter_Settings)
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.conf_groupBox.setTitle(_translate("MainWindow", "Configuration"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Stage ON/OFF"))
        self.antiAliasStage_checkBox.setText(_translate("MainWindow", "Anti Aliasing Filter"))
        self.sampleHoldStage_checkBox.setText(_translate("MainWindow", "Sample && Hold"))
        self.recovFilterStage_checkBox.setText(_translate("MainWindow", "Recovery Filter"))
        self.analogSwitchStage_checkBox.setText(_translate("MainWindow", "Analog Switch"))
        self.inputSignalOut_checkBox.setText(_translate("MainWindow", "Input Signal"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output Node"))
        self.antiAliasOut_checkBox.setText(_translate("MainWindow", "Anti Aliasing Filter"))
        self.analogSwitchOut_checkBox.setText(_translate("MainWindow", "Analog Switch"))
        self.sampleHoldOut_checkBox.setText(_translate("MainWindow", "Sample && Hold"))
        self.recovFilterOut_checkBox.setText(_translate("MainWindow", "Recovery Filter"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Sampling"))
        self.groupBox.setTitle(_translate("MainWindow", "Sampling Mode"))
        self.naturalSampling_radioButton.setText(_translate("MainWindow", "Natural"))
        self.instSampling_radioButton.setText(_translate("MainWindow", "Instantaneous"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Sampling Configuration"))
        self.label.setText(_translate("MainWindow", "Sample Rate (Hz)"))
        self.label_2.setText(_translate("MainWindow", "Sample Cycle"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Input Signal"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Waveform"))
        self.squareWaveform_radioButton.setText(_translate("MainWindow", "Square"))
        self.altSinWaveform_RadioButton.setText(_translate("MainWindow", "3/2 Sin"))
        self.sinWave_radioButton.setText(_translate("MainWindow", "Sin"))
        self.label_3.setText(_translate("MainWindow", "Input Signal Frequency (Hz)"))
        self.label_4.setText(_translate("MainWindow", "Input Signal Amplitude (V)"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionConfig_AAF_Settings.setText(_translate("MainWindow", "AAF Settings"))
        self.actionRecovery_Filter_Settings.setText(_translate("MainWindow", "Recovery Filter Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
