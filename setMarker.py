import os
from PyQt5 import QtCore, QtGui, QtWidgets
import nleeg

class Ui_setMarker(object):

    def markerCsv(self, base, file):
        if file["mark_csv"] == "_empty_":
            file_bool = False
            file["mark_csv"] = self.listWidget.currentItem().text()
        else:
            file_bool = True
            file["mark_csv_add"] = self.listWidget.currentItem().text()
        base.loadUpMark(file, file_bool)
        
    def one_Mark(self, base, file):
        # create csv for markers
        m_label = self.textEdit.toPlainText()
        time_pos = int(self.textEdit_2.toPlainText())
        time_dur = int(self.textEdit_3.toPlainText())


        if (file["mark_csv"] == "_empty_"):
            file_bool = False
            # try:
            base.set1Mark(file, file_bool, time_dur, time_pos, m_label)
            # except:
            # print("Fill all fields to add a marker 111")
        else:
            # use file.csv, add it, and add to plot
            file_bool = True
            try:
                base.set1Mark(file, file_bool, time_dur, time_pos, m_label)
            except:
                print("Fill all fields to add a marker 222")

    def setupUi3(self, base, setMarker, file):
        setMarker.setObjectName("setMarker")
        setMarker.resize(280, 396)
        setMarker.move(558, 260)
        setMarker.setMaximumSize(QtCore.QSize(300, 396))

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(setMarker)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_4 = QtWidgets.QLabel(setMarker)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.listWidget = QtWidgets.QListWidget(setMarker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(150, 130))
        self.listWidget.setMaximumSize(QtCore.QSize(250, 150))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)

        self.load_Markers = QtWidgets.QPushButton(setMarker)
        self.load_Markers.setObjectName("load_Markers")
        self.load_Markers.clicked.connect(lambda z:self.markerCsv(base, file))

        self.verticalLayout.addWidget(self.load_Markers)
        self.label_5 = QtWidgets.QLabel(setMarker)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(setMarker)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(setMarker)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(setMarker)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.textEdit_2 = QtWidgets.QTextEdit(setMarker)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(setMarker)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.textEdit_3 = QtWidgets.QTextEdit(setMarker)
        self.textEdit_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout_3.addWidget(self.textEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.one_pnt = QtWidgets.QPushButton(setMarker)
        self.one_pnt.setObjectName("one_pnt")
        self.one_pnt.clicked.connect(lambda z:self.one_Mark(base, file))

        self.verticalLayout.addWidget(self.one_pnt)
        self.verticalLayout_2.addLayout(self.verticalLayout) #

        self.retranslateUi(setMarker)
        QtCore.QMetaObject.connectSlotsByName(setMarker)

    def retranslateUi(self, setMarker):
        _translate = QtCore.QCoreApplication.translate
        setMarker.setWindowTitle(_translate("setMarker", "Set Markers"))

        font = QtGui.QFont() #Andale Mono
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)

        self.label_5.setText(_translate("setMarker", "Set a Marker"))
        self.label_5.setFont(font)
        self.label_4.setText(_translate("setMarker", "Load Marker File"))
        self.label_4.setFont(font)
        self.load_Markers.setText(_translate("setMarker", "Load Markers.csv"))
        self.label.setText(_translate("setMarker", "Marker Text:"))
        self.label_2.setText(_translate("setMarker", "Duration (ms):"))
        self.label_3.setText(_translate("setMarker", "Timeline Pos (ms):"))
        self.one_pnt.setText(_translate("setMarker", "Set Marker"))





