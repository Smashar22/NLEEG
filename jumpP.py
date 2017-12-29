from PyQt5 import QtCore, QtGui, QtWidgets
import nleeg

class Ui_jumpP(object):

    def send_jump(self, base):
        #code: sends the location and jumps there
        time_pos = int(self.textEdit.toPlainText())
        base.jump_to_load(time_pos)


    def setupUi4(self, base, jumpP, data):
        jumpP.setObjectName("jumpP")
        jumpP.setEnabled(True)
        jumpP.resize(368, 148)
        jumpP.move(864, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(jumpP.sizePolicy().hasHeightForWidth())
        jumpP.setSizePolicy(sizePolicy)
        jumpP.setMinimumSize(QtCore.QSize(368, 120))
        jumpP.setMaximumSize(QtCore.QSize(368, 148))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(jumpP)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(jumpP)
        self.label.setMinimumSize(QtCore.QSize(155, 0))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(jumpP)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.jump_btn = QtWidgets.QPushButton(jumpP)
        self.jump_btn.setObjectName("jump_btn")
        self.jump_btn.clicked.connect(lambda x:self.send_jump(base))
        self.verticalLayout.addWidget(self.jump_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(jumpP)
        QtCore.QMetaObject.connectSlotsByName(jumpP)

    def retranslateUi(self, jumpP):
        _translate = QtCore.QCoreApplication.translate
        jumpP.setWindowTitle(_translate("jumpP", "Jump"))
        self.label.setText(_translate("jumpP", "Time Position (m/s): "))
        self.jump_btn.setText(_translate("jumpP", "Jump to"))

