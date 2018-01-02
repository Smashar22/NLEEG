from PyQt5 import QtCore, QtGui, QtWidgets
import nleeg

class Ui_hilbert_win(object):

    def send_vars(self, base, data):
        #code: sends variables to plotter function
        try:
            ch_num = int(self.textEdit.toPlainText())
            start_t = int(self.textEdit_6.toPlainText())
            end_t = int(self.textEdit_7.toPlainText())
            samp_rate = int(self.textEdit_2.toPlainText())
            num_samps = int(self.textEdit_3.toPlainText())
            time_len = int(self.textEdit_4.toPlainText())
            nyquist = int(self.textEdit_5.toPlainText())
            base.plot_hilb(data, ch_num, samp_rate, num_samps, time_len, 
                                                      nyquist, start_t, end_t)
        except:
            base.error()

    def setupUi7(self, base, hilbert_win, data):
        hilbert_win.setObjectName("hilbert_win")
        hilbert_win.resize(280, 166)
        hilbert_win.setMinimumSize(QtCore.QSize(260, 316))
        hilbert_win.setMaximumSize(QtCore.QSize(260, 316))
        hilbert_win.move(578, 374)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(hilbert_win)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(hilbert_win)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(hilbert_win)
        self.label.setMinimumSize(QtCore.QSize(128, 0))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(hilbert_win)
        self.textEdit.setObjectName("textEdit")
        #
        self.horizontalLayout_4.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(hilbert_win)
        self.label_2.setMinimumSize(QtCore.QSize(128, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        ######
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(hilbert_win)
        self.label_7.setMinimumSize(QtCore.QSize(128, 0))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.textEdit_6 = QtWidgets.QTextEdit(hilbert_win)
        self.horizontalLayout_6.addWidget(self.textEdit_6)
        self.verticalLayout.addLayout(self.horizontalLayout_6)   

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(hilbert_win)
        self.label_8.setMinimumSize(QtCore.QSize(128, 0))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.textEdit_7 = QtWidgets.QTextEdit(hilbert_win)
        self.horizontalLayout_7.addWidget(self.textEdit_7)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.textEdit_2 = QtWidgets.QTextEdit(hilbert_win)
        self.textEdit_2.setObjectName("textEdit_2")
        #
        self.textEdit_2.setText(str(data["samp_rate"]))
        #
        self.horizontalLayout.addWidget(self.textEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(hilbert_win)
        self.label_3.setMinimumSize(QtCore.QSize(128, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.textEdit_3 = QtWidgets.QTextEdit(hilbert_win)
        self.textEdit_3.setObjectName("textEdit_3")
        #
        self.textEdit_3.setText(str(data["num_samples"]))
        #
        self.horizontalLayout_2.addWidget(self.textEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(hilbert_win)
        self.label_5.setMinimumSize(QtCore.QSize(128, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.textEdit_4 = QtWidgets.QTextEdit(hilbert_win)
        self.textEdit_4.setObjectName("textEdit_4")
        #
        self.textEdit_4.setText(str(data["time_ln_msec"]))
        #
        self.horizontalLayout_3.addWidget(self.textEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(hilbert_win)
        self.label_6.setMinimumSize(QtCore.QSize(128, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.textEdit_5 = QtWidgets.QTextEdit(hilbert_win)
        self.textEdit_5.setObjectName("textEdit_5")
        #
        self.textEdit_5.setText(str(data["nyquist"]))
        #
        self.horizontalLayout_5.addWidget(self.textEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.pushButton = QtWidgets.QPushButton(hilbert_win)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda x:self.send_vars(base, data))


        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(hilbert_win)
        QtCore.QMetaObject.connectSlotsByName(hilbert_win)

    def retranslateUi(self, hilbert_win):
        _translate = QtCore.QCoreApplication.translate
        hilbert_win.setWindowTitle(_translate("hilbert_win", "Hilbert Transform"))
        self.label_4.setText(_translate("hilbert_win", "Variables"))
        self.label_4.setFont(QtGui.QFont("Arial",weight=QtGui.QFont.Bold))
        self.label.setText(_translate("hilbert_win", "Channel Number: "))
        self.label_2.setText(_translate("hilbert_win", "Sample Rate: "))
        self.label_3.setText(_translate("hilbert_win", "Number of Samples: "))
        self.label_5.setText(_translate("hilbert_win", "Time Length: "))
        self.label_6.setText(_translate("hilbert_win", "Nyquist: "))
        self.label_7.setText(_translate("hilbert_win", "Start Time(ms): "))
        self.label_8.setText(_translate("hilbert_win", "End Time(ms): "))

        self.pushButton.setText(_translate("hilbert_win", "Plot to Graph"))

