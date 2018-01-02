import os, sys, time
from PyQt5 import QtWidgets, QtGui, QtCore
import nleeg, loadFile, setMarker, scalpMap, jumpP, chanPass
import sliceD, loadFFT, loadHilbert, userScript, loadBandp


class nleegStart(QtWidgets.QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupCard()
        QtCore.QTimer.singleShot(1000, self.close) #2400 best

    def setupCard(self):
        self.lab = QtWidgets.QLabel()
        cwd = os.getcwd()
        self.pixmap = QtGui.QPixmap(cwd + '/CCC.jpg')
        self.lab.setPixmap(self.pixmap)
        self.vbox = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbox)
        self.setMinimumSize(QtCore.QSize(526, 526))
        self.setMaximumSize(QtCore.QSize(526, 526))
        self.vbox.addWidget(self.lab)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.move(400, 180)


class nleegApp(QtWidgets.QWidget, nleeg.Ui_Form, loadFile.Ui_inputFile, 
               setMarker.Ui_setMarker, scalpMap.Ui_scalpMap, jumpP.Ui_jumpP,
               sliceD.Ui_slice_D, loadFFT.Ui_fft_win, userScript.Ui_user_script,
               loadHilbert.Ui_hilbert_win, loadBandp.Ui_loadBandp_win,
               chanPass.Ui_chanPass):

    def __init__(self):
        super(self.__class__, self).__init__()
        data = self.varies()
        self.setupUi(self, data)

    def varies(self):
        # Nyquist = sample_rate/2.
        # fneeg = raw_input("Filename (full path & extension): ")
        # t = int(raw_input("How many secs in total of EEG?: "))
        # ch = int(raw_input("How many channels of EEG?: "))
        # le = t*sample_rate  # length of recording = time x sample_rate
        # fid = open(fneeg, 'r')
        # EEG = fromfile(fneeg, int16)
        var_dic = {"file_csv":"_empty_", "ch_cnt":0, "time_ln_msec":0, 
                   "samp_rate":0, "num_samples": 0, "nyquist":0, 
                   "mark_csv": "_empty_", "mark_csv_add": "_empty_",
                   "tick_bool": True}
        return var_dic
        

def main():
    # Title Card
    app_t = QtWidgets.QApplication(sys.argv)
    title = nleegStart()
    title.show()
    app_t.exec_()

    # Application
    app = QtWidgets.QApplication(sys.argv)
    form = nleegApp()
    form.show()                
    app.exec_()


if __name__ == '__main__':              
    main()                             






