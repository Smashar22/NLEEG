from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import nleeg

class Ui_chanPass(object):

    def setupUi10(self, base, bPass_win, data, time, orig_sig, pass_sig):
        bPass_win.setObjectName("bPass_win")
        bPass_win.resize(280, 166)
        bPass_win.setMinimumSize(QtCore.QSize(790, 346))
        bPass_win.setMaximumSize(QtCore.QSize(790, 346))
        bPass_win.move(49, 100)

        self.verticalLayout = QtWidgets.QVBoxLayout(bPass_win)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plotter3 = QtWidgets.QWidget()
        self.plotter3.setLayout(QtWidgets.QVBoxLayout())
        self.plotter3.layout().setContentsMargins(0,0,0,0)
        self.plotter3.layout().setSpacing(0)
        self.plotter3.setMinimumSize(QtCore.QSize(750, 306))

        self.figure3 = plt.figure(dpi=70, figsize=(3, 2))
        self.canvas3 = FigureCanvas(self.figure3)
        # self.toolbar = NavigationToolbar(self.canvas, self)
        self.figure3.tight_layout(pad=0.1, w_pad=0, h_pad=2)
        self.plotter3.layout().addWidget(self.canvas3)
        self.verticalLayout.addWidget(self.plotter3)

        d = self.figure3.add_subplot(2,1,1)
        d.plot(time, orig_sig, label ='Original Signal')
        plt.ylabel('Original', fontsize= 6, weight='bold', 
                    verticalalignment= 'center', horizontalalignment= 'right',
                                                        rotation='horizontal')
        plt.xlabel('Time(s)', fontsize= 6, weight='bold',
                    verticalalignment= 'center', horizontalalignment= 'center',
                                                        rotation='horizontal')

        e = self.figure3.add_subplot(2,1,2)
        e.plot(time, pass_sig, label ='Bandpassed Signal', color='orange')
        plt.ylabel('Band Passed', fontsize= 6, weight='bold', 
                    verticalalignment= 'center', horizontalalignment= 'right',
                                                        rotation='horizontal')
        plt.xlabel('Time(s)', fontsize= 6, weight='bold', 
                    verticalalignment= 'center', horizontalalignment= 'center', 
                                                        rotation='horizontal')
        self.canvas3.draw()

        self.retranslateUi(bPass_win)
        QtCore.QMetaObject.connectSlotsByName(bPass_win)

    def retranslateUi(self, bPass_win):
        _translate = QtCore.QCoreApplication.translate
        bPass_win.setWindowTitle(_translate("bPass_win", "EEG Band Pass Data"))


