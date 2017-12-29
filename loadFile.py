import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import nleeg

class Ui_inputFile(object):

    def chooseCsv(self, base, file):
        file["file_csv"] = self.listWidget.currentItem().text()

        if self.textEdit.toPlainText() == '':
            print('No sample rate entered: defaulted to 1000Hz')
            file["samp_rate"] = 1000
        else:
            file["samp_rate"] = int(self.textEdit.toPlainText())
        base.loadUpCsv(file)

    def setupUi2(self, base, inputFile, file):
        inputFile.setObjectName("inputFile")
        inputFile.resize(200, 300)
        inputFile.move(48, 390)
        inputFile.setMaximumSize(QtCore.QSize(200, 300))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(inputFile)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(inputFile)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.loadInput = QtWidgets.QPushButton(inputFile)
        self.loadInput.setObjectName("loadInput") #The button
        self.loadInput.clicked.connect(lambda x:self.chooseCsv(base, file))

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.samp_rate = QtWidgets.QLabel(inputFile)
        self.samp_rate.setObjectName("samp_rate")
        self.horizontalLayout.addWidget(self.samp_rate)
        self.textEdit = QtWidgets.QTextEdit(inputFile)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.addWidget(self.loadInput)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(inputFile)
        QtCore.QMetaObject.connectSlotsByName(inputFile)

    def retranslateUi(self, inputFile):
        _translate = QtCore.QCoreApplication.translate
        inputFile.setWindowTitle(_translate("inputFile", "Load File"))
        self.loadInput.setText(_translate("inputFile", "Load .csv"))
        self.samp_rate.setText(_translate("inputFile", "Sample Rate(Hz):"))

