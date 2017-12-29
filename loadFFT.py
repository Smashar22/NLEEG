from PyQt5 import QtCore, QtGui, QtWidgets
import nleeg

class Ui_fft_win(object):

    def send_vars(self, base, data):
        #code: sends variables to plotter function
        ch_num = int(self.textEdit.toPlainText())
        samp_rate = int(self.textEdit_2.toPlainText())
        num_samps = int(self.textEdit_3.toPlainText())
        time_len = int(self.textEdit_4.toPlainText())
        nyquist = int(self.textEdit_5.toPlainText())

        base.plot_fft(data, ch_num, samp_rate, num_samps, time_len, nyquist)

    def setupUi6(self, base, fft_win, data):
        fft_win.setObjectName("fft_win")
        fft_win.resize(280, 166)
        fft_win.setMinimumSize(QtCore.QSize(260, 296))
        fft_win.setMaximumSize(QtCore.QSize(260, 296))
        fft_win.move(578, 392)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(fft_win)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(fft_win)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(fft_win)
        self.label.setMinimumSize(QtCore.QSize(128, 30))
        self.label.setMaximumSize(QtCore.QSize(128, 15))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(fft_win)
        self.textEdit.setObjectName("textEdit")
        #
        # self.textEdit.setText("Chan Select")
        #
        self.horizontalLayout_4.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(fft_win)
        self.label_2.setMinimumSize(QtCore.QSize(128, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.textEdit_2 = QtWidgets.QTextEdit(fft_win)
        self.textEdit_2.setObjectName("textEdit_2")
        #
        self.textEdit_2.setText(str(data["samp_rate"]))
        #
        self.horizontalLayout.addWidget(self.textEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(fft_win)
        self.label_3.setMinimumSize(QtCore.QSize(128, 30))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.textEdit_3 = QtWidgets.QTextEdit(fft_win)
        self.textEdit_3.setObjectName("textEdit_3")
        #
        self.textEdit_3.setText(str(data["num_samples"]))
        #
        self.horizontalLayout_2.addWidget(self.textEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(fft_win)
        self.label_5.setMinimumSize(QtCore.QSize(128, 30))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.textEdit_4 = QtWidgets.QTextEdit(fft_win)
        self.textEdit_4.setObjectName("textEdit_4")
        #
        self.textEdit_4.setText(str(data["time_ln_msec"]))
        #
        self.horizontalLayout_3.addWidget(self.textEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(fft_win)
        self.label_6.setMinimumSize(QtCore.QSize(128, 30))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.textEdit_5 = QtWidgets.QTextEdit(fft_win)
        self.textEdit_5.setObjectName("textEdit_5")
        #
        self.textEdit_5.setText(str(data["nyquist"]))
        #
        self.horizontalLayout_5.addWidget(self.textEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.pushButton = QtWidgets.QPushButton(fft_win)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda x:self.send_vars(base, data))

        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(fft_win)
        QtCore.QMetaObject.connectSlotsByName(fft_win)

    def retranslateUi(self, fft_win):
        _translate = QtCore.QCoreApplication.translate
        fft_win.setWindowTitle(_translate("fft_win", "Fast Fourier Transform"))
        self.label_4.setText(_translate("fft_win", "Variables"))
        self.label_4.setFont(QtGui.QFont("Arial",weight=QtGui.QFont.Bold))
        self.label.setText(_translate("fft_win", "Select Channel: "))
        self.label_2.setText(_translate("fft_win", "Sample Rate: "))
        self.label_3.setText(_translate("fft_win", "Number of Samples: "))
        self.label_5.setText(_translate("fft_win", "Time Length (ms): "))
        self.label_6.setText(_translate("fft_win", "Nyquist: "))
        self.pushButton.setText(_translate("fft_win", "Plot to Graph"))

