from PyQt5 import QtCore, QtGui, QtWidgets
import nleeg

class Ui_slice_D(object):
    def setupUi5(self, slice_D, data):
        slice_D.setObjectName("slice_D")
        slice_D.setEnabled(True)
        slice_D.resize(368, 148)
        slice_D.move(864, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(slice_D.sizePolicy().hasHeightForWidth())
        slice_D.setSizePolicy(sizePolicy)
        slice_D.setMinimumSize(QtCore.QSize(368, 120))
        slice_D.setMaximumSize(QtCore.QSize(368, 148))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(slice_D)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(slice_D)
        self.label.setMinimumSize(QtCore.QSize(155, 0))
        self.label.setMaximumSize(QtCore.QSize(155, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(slice_D)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(slice_D)
        self.label_2.setMinimumSize(QtCore.QSize(155, 0))
        self.label_2.setMaximumSize(QtCore.QSize(155, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.textEdit_2 = QtWidgets.QTextEdit(slice_D)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.slice_btn = QtWidgets.QPushButton(slice_D)
        self.slice_btn.setObjectName("slice_btn")
        self.verticalLayout.addWidget(self.slice_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(slice_D)
        QtCore.QMetaObject.connectSlotsByName(slice_D)

    def retranslateUi(self, slice_D):
        _translate = QtCore.QCoreApplication.translate
        slice_D.setWindowTitle(_translate("slice_D", "Slice"))
        self.label.setText(_translate("slice_D", "Start Slice Time (m/s): "))
        self.label_2.setText(_translate("slice_D", "End Slice Time (m/s): "))
        self.slice_btn.setText(_translate("slice_D", "Slice Data"))

