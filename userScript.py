from PyQt5 import QtCore, QtGui, QtWidgets
import nleeg, os

class Ui_user_script(object):

    def plot_it(self, base, data):
        #code: plots the text data
        user_script = self.textEdit.toPlainText()
        base.user_plot(user_script, data)

    def save_it(self, base, data):
        #code: saves the text data
        user_script = self.textEdit.toPlainText()
        path = os.getcwd() + '/user_scripts/'
        os.chdir(path)
        var = 1
        fname = "script"+str(var)+".py"

        while os.path.isfile(fname):
            fname = fname[:-len(str(var)+".py")]
            var = var + 1
            fname = fname +str(var)+".py"

        with open(fname, "w") as text_file:
            text_file.write("%s" % (user_script))
        text_file.close()

        path = path[:-len("/user_scripts/")] #reset directory to Nleeg
        os.chdir(path)
        base.script_save = user_script

    def setupUi8(self, base, user_script, data):
        user_script.setObjectName("user_script")
        user_script.resize(650, 620)
        user_script.move(115, 70)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(user_script)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(user_script)
        self.textEdit.setObjectName("textEdit")
        if base.script_save != "":
            self.textEdit.setText(base.script_save)
        else:
            self.textEdit.setText(
                "#This is a script template for implementation of your Algorithm")
            self.textEdit.setText(self.textEdit.toPlainText() +
                "\n\n #Apply your algorithm to the variables marked below") 
            self.textEdit.setText(self.textEdit.toPlainText() +
                            "\n #Click 'Plot Script' and the 'Algorithm Plotter' will display your data")
            self.textEdit.setText(self.textEdit.toPlainText() +
                        "\n\n\n # self.lines[] contains all EEG lines, apply your algorithms to it")
            self.textEdit.setText(self.textEdit.toPlainText() +
                  "\n\nself.figure2.clear() \t\t\t #clears window for new plot")
            self.textEdit.setText(self.textEdit.toPlainText() +
                     "\nax = self.figure2.add_subplot(1,1,1) \t\t #adds a plot")
            self.textEdit.setText(self.textEdit.toPlainText() +
                              "\nT = np.arange(0.0, 2.0, 0.01) \t\t #x axis ticks")
            self.textEdit.setText(self.textEdit.toPlainText() +
                              "\nQ = 1 + np.sin(2*np.pi*T) \t\t\t #use a sine wave as data")
            self.textEdit.setText(self.textEdit.toPlainText() +
                              "\nax.plot(T, Q) \t\t\t\t #plots variables T and Q")
            self.textEdit.setText(self.textEdit.toPlainText() +
                             "\nself.canvas2.draw() \t\t\t #redraws the canvas")
            self.textEdit.setText(self.textEdit.toPlainText() +
                "\n\n# <--- Remove the hash marks at the front to uncomment code")
            self.textEdit.setText(self.textEdit.toPlainText() +
                "\n\n# Save Script will save to the 'user_scripts' folder, in this folder")
            self.textEdit.setText(self.textEdit.toPlainText() +
                "\n\n# You will also find some example scripts to paste in and plot")                                                       
            self.textEdit.setText(self.textEdit.toPlainText() +
                                        "\n\n# Have Fun Plotting!")

        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton2 = QtWidgets.QPushButton(user_script)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(lambda x:self.save_it(base, data))
        self.pushButton = QtWidgets.QPushButton(user_script)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda x:self.plot_it(base, data))
        self.verticalLayout.addWidget(self.pushButton2)
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(user_script)
        QtCore.QMetaObject.connectSlotsByName(user_script)

    def retranslateUi(self, user_script):
        _translate = QtCore.QCoreApplication.translate
        user_script.setWindowTitle(_translate("user_script", "User Script"))
        self.pushButton.setText(_translate("user_script", "Plot Script"))
        self.pushButton2.setText(_translate("user_script", "Save Script"))

