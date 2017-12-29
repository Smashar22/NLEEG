import os
from PyQt5 import QtCore, QtGui, QtWidgets
import nleeg

class Ui_scalpMap(object):

    """
    def load_map(self):
        cwd = os.getcwd()
        self.pixm = QtGui.QPixmap(cwd + '/scalp_cap.png')
        self.map_image.setPixmap(self.pixm)
        self.vbox = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbox)
        self.setMinimumSize(QtCore.QSize(526, 526))
        self.setMaximumSize(QtCore.QSize(526, 526))
        self.vbox.addWidget(self.map_image)
        # self.move(400, 180)
        # self.show()
    """

    def setupUi4(self, scalpMap):
        scalpMap.setObjectName("scalpMap")
        scalpMap.resize(450, 450)
        scalpMap.setMinimumSize(QtCore.QSize(370, 370))
        scalpMap.setMaximumSize(QtCore.QSize(370, 370))
        scalpMap.move(863, 70)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(scalpMap)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.map_image = QtWidgets.QLabel(scalpMap)
        self.map_image.setLineWidth(0)
        self.map_image.setText("")
        self.map_image.setObjectName("map_image")
        cwd = os.getcwd()
        self.pixm = QtGui.QPixmap(cwd + '/scalp_cap.png')
        self.map_image.setPixmap(self.pixm)

        self.verticalLayout.addWidget(self.map_image)
        self.loadElectrodes = QtWidgets.QPushButton(scalpMap)
        self.loadElectrodes.setObjectName("loadElectrodes")
        # self.loadElectrodes.clicked.connect(lambda x:self.load_map())
        self.verticalLayout.addWidget(self.loadElectrodes)
        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(scalpMap)
        QtCore.QMetaObject.connectSlotsByName(scalpMap)

    def retranslateUi(self, scalpMap):
        _translate = QtCore.QCoreApplication.translate
        scalpMap.setWindowTitle(_translate("scalpMap", "Scalp Map"))
        self.loadElectrodes.setText(_translate("scalpMap", "Load Electrodes"))

