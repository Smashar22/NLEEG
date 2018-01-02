import os, sys, csv, time, math
import pandas as pd
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from sklearn import preprocessing
from scipy.fftpack import fft, ifft, rfft
from scipy.signal import lfilter, hilbert, butter, freqz
from loadFile import Ui_inputFile
from setMarker import Ui_setMarker
from scalpMap import Ui_scalpMap
from userScript import Ui_user_script
from jumpP import Ui_jumpP
from sliceD import Ui_slice_D
from loadFFT import Ui_fft_win
from loadHilbert import Ui_hilbert_win
from loadBandp import Ui_loadBandp_win
from chanPass import Ui_chanPass

import time


class Ui_Form(object):

    def fill_info(self, data):
        #code: populates info panel with eeg data specifics
        self.label.setText("")
        self.label.setText(self.label.text() + "\n\n File: " + "\t\t\t\t" + 
                                                             data["file_csv"])
        self.label.setText(self.label.text() + "\n Num Samples: " + "\t\t\t\t"
                                                   + str(data["num_samples"]))
        self.label.setText(self.label.text() + "\n Sample Rate (Hz): " 
                                        + "\t\t\t\t" + str(data["samp_rate"]))
        self.label.setText(self.label.text() + "\n Total Time (ms): " 
                                     + "\t\t\t\t" + str(data["time_ln_msec"]))
        self.label.setText(self.label.text() + "\n Channels: " + "\t\t\t\t"
                                                        + str(data["ch_cnt"]))
        self.label.setText(self.label.text() + "\n Nyquist: " + "\t\t\t\t"
                                                       + str(data["nyquist"]))

    def loadCsv(self, data):    
        self.window = QtWidgets.QWidget()
        temp = Ui_inputFile() #self.ui
        temp.setupUi2(self, self.window, data)
        cwd = os.getcwd() + '/data_eeg'
        i = 0
        for file in os.listdir(cwd):
            if file.endswith(".csv"):
                i = i + 1
                item = QtWidgets.QListWidgetItem(file)
                temp.listWidget.insertItem(i, item)
        self.window.show()

    def mark2plot(self, mark_arr):
        # code: draw mark onto main plotter1 canvas
        # mark_arr[0] = time pos
        # mark_arr[1] = time dur
        # mark_arr[2] = label

        # Top graph for word
        self.mark_list.append(mark_arr[0])
        self.plot_arr[0].axvline(x=mark_arr[0], color='r', linestyle=':', linewidth=0.5) 
        self.plot_arr[0].text(mark_arr[0], self.lines[0].max(),
                              str(mark_arr[2]) + ', ' + str(mark_arr[1]) + 'ms',
                              fontsize=6, color='r', 
                              bbox={'facecolor':'red', 'alpha':0.2, 'pad':1})
        # Lower graphs for dotted lines
        for pl in np.arange(1,len(self.plot_arr)):
            self.plot_arr[pl].axvline(x=mark_arr[0], color='r', linestyle=':', linewidth=0.5)
        self.canvas.draw()
    
    def loadUpCsv(self, data):
        #main function to setup plotting data
        self.figure.clear()

        path = os.getcwd() + "/data_eeg/"
        os.chdir(path)
        file = open(data["file_csv"],'rU')
        reader = csv.reader(file, delimiter=',', dialect=csv.excel_tab)
        ch_cnt = 1 #reader.next() means this doesn't start at 0
        data["num_samples"] = len(reader.next())

        for row in reader:
          ch_cnt = ch_cnt + 1
        data["ch_cnt"] = ch_cnt
        #Plot scaling for increase amounts of channels
        if ch_cnt < 11:
            self.xinch = 5.7   # Size of canvas area scaling 
            self.yinch = 6     # Scale for more channels
        elif ch_cnt < 16:
            self.xinch = 5.7  
            self.yinch = 15   
        elif ch_cnt < 21:
            self.xinch = 5.7   
            self.yinch = 21   
        elif ch_cnt < 31:
            self.xinch = 5.7  
            self.yinch = 32   
        elif ch_cnt < 46:
            self.xinch = 5.7   
            self.yinch = 40   
        elif ch_cnt < 61:
            self.xinch = 5.7   
            self.yinch = 46 
        else:
            self.xinch = 5.7   
            self.yinch = 56

        file.close()
        plt.close(self.figure) #Reset self.figure for new figure size
        self.figure = plt.figure(num=1, dpi=70, figsize=(self.xinch, self.yinch))
        self.canvas = FigureCanvas(self.figure)
        self.figure.tight_layout(pad=0.3, w_pad=0, h_pad=1.0)
            

        data["time_ln_msec"] = int((float(data["num_samples"])/float(data["samp_rate"])) * 1000)
        data["nyquist"] = data["samp_rate"]/2
        ##########

        t1 = time.time()

        """
        dataframe = pd.read_csv(data["file_csv"], sep = ',', header = None)
        ndarr = dataframe.as_matrix()
        ndarr = ndarr.astype(int)
        ndarr = np.swapaxes(ndarr, 0, 1)
        """

        ndarr = np.loadtxt(data["file_csv"], 
                  dtype = float,
                  unpack = True, 
                  delimiter = ',')

        t2 = time.time()
        total = t2 - t1

        print(total)

        """ old method
        ndarr = np.loadtxt(data["file_csv"], 
                  dtype = float,
                  unpack = True, 
                  delimiter = ',')
        """

        ####### IMPORTANT ########
        self.ndarr = ndarr # source ndarray
        ####### IMPORTANT ########

        # substitute loadtxt for read_csv

        self.x_axis_r = np.arange(data["num_samples"])
        path = path[:-len("/data_eeg/")] #reset directory to Nleeg
        os.chdir(path)
        ####### IMPORTANT ########
        self.plot_arr = []  ####### IMPORTANT ########
        self.lines = []     ####### IMPORTANT ########
        ####### IMPORTANT ########

        # Plot layering
        x = ch_cnt
        self.lines.append(np.hstack(ndarr[:, 0, np.newaxis]))
        temp = self.figure.add_subplot(ch_cnt, 1, 1) # facecolor='cream'
        self.plot_arr.append(temp)
        self.temp = temp # top line template (for adding words)
        temp.yaxis.label.set_color('orange')
        temp.set_ylim((self.lines[0].min()-5), (self.lines[0].max()+5))
        R = ((self.lines[0].max()) - (self.lines[0].min()))/2
        
        plt.yticks(np.arange(int(self.lines[0].min()), 
                              int(self.lines[0].max()+2), int(R)), fontsize=4)
        plt.xticks(np.arange(0, data["num_samples"], 200), fontsize=4)
        # temp.spines['right'].set_visible(False)
        temp.spines['top'].set_visible(False)
        temp.spines['bottom'].set_visible(False)
        self.figure.set_facecolor('yellow')
        self.figure.patch.set_alpha(0.02)

        ############
        self.xlim_min = 0
        self.xlim_max = data["num_samples"]
        self.xlim_max = math.ceil(self.xlim_max / 1000) * 1000
        temp.set_xlim(xmin=0,xmax= self.xlim_max)
        ############
        plt.plot(self.x_axis_r, self.lines[0], '-', linewidth=0.4)
        plt.ylabel('Ch.1', fontsize=8, weight='bold', verticalalignment= 'center',
                    horizontalalignment= 'right', rotation='horizontal')
        y = 2
        for z in range(1, ch_cnt):
            line = np.hstack(ndarr[:, z, np.newaxis])
            self.lines.append(np.hstack(ndarr[:, z, np.newaxis]))
            self.plot_arr.append(self.figure.add_subplot(ch_cnt,1,y, sharex=self.temp))
            self.plot_arr[z].yaxis.label.set_color('orange')
            self.plot_arr[z].set_ylim((line.min()-5), (line.max()+5))
            R = ((line.max()) - (line.min()))/2
            plt.yticks(np.arange(int(line.min()), int(line.max()+2), int(R)), fontsize=4)
            plt.ylabel('Ch.'+str(y), fontsize=8, weight='bold', verticalalignment= 'center',
                       horizontalalignment= 'right', rotation='horizontal')
            # self.plot_arr[z].grid()
            # self.plot_arr[z].spines['right'].set_visible(False)
            self.plot_arr[z].spines['top'].set_visible(False)
            self.plot_arr[z].spines['bottom'].set_visible(False)
            plt.xticks(np.arange(0, self.xlim_max, 
                                     (self.xlim_max - 100)/4), fontsize=4)
            self.plot_arr[z].plot(self.x_axis_r, line, '-', linewidth=0.4)
            y = y + 1
        self.figure.set_size_inches(self.xinch, self.yinch, forward=True)
        self.figure.tight_layout(pad=0.3, w_pad=0.2, h_pad=0.2)
        self.canvas = FigureCanvas(self.figure)
        # self.figure.clear() #clears data, but doesn't renew size
        self.canvas.draw()
        self.scroll.setWidget(self.canvas) #these four lines refresh plotter
        self.add_tools()
        self.fill_info(data)

    def loadMark(self, data):
        # code: Load markers UI window, populates
        if data["ch_cnt"] == 0:
            warn = QtWidgets.QMessageBox.question(self, 'Empty!', 'No Data Has Been Loaded To Plotter',
                                    QtWidgets.QMessageBox.Ok)
            if warn == QtWidgets.QMessageBox.Ok:
                print('Return to Main')
            else:
                pass
        else:
            self.window2 = QtWidgets.QWidget()
            temp2 = Ui_setMarker() # self.ui2
            temp2.setupUi3(self, self.window2, data)
            cwd = os.getcwd() + '/data_events'
            i = 0
            for file in os.listdir(cwd):
                if file.endswith(".csv"):
                    i = i + 1
                    item = QtWidgets.QListWidgetItem(file)
                    temp2.listWidget.insertItem(i, item)
            self.window2.show()

    def loadScalp(self):
        # load scalp UI window and image
        self.window3 = QtWidgets.QWidget()
        temp3 = Ui_scalpMap()
        temp3.setupUi4(self.window3)
        self.window3.show()

    def data2array(self, file_name):
        with open(file_name, "rU") as file:
            reader = csv.reader(file, delimiter=',', dialect=csv.excel_tab)
            size = -1 #header at top
            for row in reader: #attain number of rows
              size = size + 1
            array = [[0 for x in range(3)] for y in range(size)] 
            file.seek(0)
            y = 0
            next(reader) # skip header
            for row in reader: #put data into array
                array[y][1] = int(row[0])
                array[y][0] = int(row[1])
                array[y][2] = str(row[2])
                y = y + 1
            file.close()
        return array

    #mostly finished
    def loadUpMark(self, file, file_bool):
        # code: Loads markers onto current .csv and plot
        cwd = os.getcwd() + '/data_events/'
        os.chdir(cwd)

        if not file_bool:
            #code: open selected .csv and plot it
            arr = self.data2array(file["mark_csv"])
            for row in arr:
                self.mark2plot(row)
        else:
            #code: add new .csv to existing .csv, plot new points
            with open(file["mark_csv"], "a") as old_file:
                add_file = open(file["mark_csv_add"]) # loop
                old_file.write("\n")
                old_file.write(add_file)

            old_file.close()
            # plot the new points
            self.mark2plot(add_file)
            file["mark_csv_add"] = "_empty_"

        cwd = cwd[:-len("/data_events/")] #reset directory to Nleeg
        os.chdir(cwd)

    def set1Mark(self, file, file_bool, time_dur, time_pos, m_label):
        # code: Loads one marker onto current plot
        cwd = os.getcwd()

        if not file_bool:
            file["mark_csv"] = 'new_events.csv'
            with open('new_events.csv', "w") as new_file:
                new_file.write("duration(ms), time(ms), word")
                new_file.write("\n" + str(time_dur) + "," + str(time_pos) + "," + str(m_label))
                new_file.close()
            arr = [time_dur, time_pos, m_label]
            self.mark2plot(arr) # plot onto the graph code
        else:
            # file exists already, append the data 
            path = cwd + file["mark_csv"]
            with open(path, "a") as csv_file:
                csv_file.write("\n" + str(time_dur) + "," + str(time_pos) + "," + str(m_label))
                csv_file.close()
            arr = [time_dur, time_pos, m_label]
            self.mark2plot(arr)
     
# --------------------
# Bottom Panel Buttons
    def add_tools(self):
        self.verticalLayout_3.removeWidget(self.label)
        self.verticalLayout_3.removeWidget(self.toolbar)
        # Reset and Readd Widgets (navbar not connected, otherwise)
        self.toolbar = NavigationToolbar(self.canvas, self)      
        self.verticalLayout_3.addWidget(self.toolbar)
        # Insert code to update info panel on right corner
        self.verticalLayout_3.addWidget(self.label)

    def low_bandP(self, data):
        #code: sets up the bandpass load window
        if data["ch_cnt"] == 0:
            warn = QtWidgets.QMessageBox.question(self, 'Empty!', 'No Data Has Been Loaded To Plotter',
                                    QtWidgets.QMessageBox.Ok)
            if warn == QtWidgets.QMessageBox.Ok:
                print('Return to Main')
            else:
                pass
        else:
            self.window9 = QtWidgets.QWidget()
            temp9 = Ui_loadBandp_win()
            temp9.setupUi9(self, self.window9, data)
            self.window9.show()

    def chan_pass_plot(self, data, ch_num, samp_rate, num_samps, time_ln,
                             nyquist, start_t, end_t, order, lowcut, highcut):
        # code: plots the changes to the eeg plot from bandpass filter

        # Start Logic for when bandpass filter is ready
        if data["ch_cnt"] == 0:
            warn = QtWidgets.QMessageBox.question(self, 'Empty!', 'No Data Has Been Loaded To Plotter',
                                    QtWidgets.QMessageBox.Ok)
            if warn == QtWidgets.QMessageBox.Ok:
                print('Return to Main')
            else:
                pass
        else:
            self.figure2.clear()
            fs = data["samp_rate"]
            nyq = data["nyquist"]

            low = lowcut/nyq
            high = highcut/nyq
            b, a = butter(order, [low, high], btype='band')
            w, h = freqz(b, a, worN=2000)

            d = self.figure2.add_subplot(1,1,1)
            d.plot((fs*0.5/ np.pi) * w, abs(h), label="Order %d Frequency Response" % order)
            d.set_xlabel('Frequency (Hz)')
            d.set_ylabel('Gain')
            d.legend(loc='best')
            self.canvas2.draw()

        # Prep the chopped data and send to new plot window
        orig_plot = self.lines[(ch_num-1)][start_t:end_t]
        pass_plot = self.lines[(ch_num-1)][start_t:end_t]
        pass_plot = lfilter(b, a, pass_plot)
        nsamps = end_t - start_t
        T = 1.0 / samp_rate
        time = np.linspace(0, nsamps*T, nsamps, endpoint = False)

        #Loads new timeline plot for altered eeg data
        self.window10 = QtWidgets.QWidget()
        temp10 = Ui_chanPass()
        temp10.setupUi10(self, self.window10, data, time, orig_plot, pass_plot)
        self.window10.show()

    def nleeg_fft(self, data):

        """
        # spell out the args that were passed to the Matlab function
        N = 10
        Fc = 40
        Fs = 1600
        # provide them to firwin
        # h = scipy.signal.firwin(numtaps=N, cutoff=40, nyq=Fs/2)
        # 'x' is the time-series data you are filtering
        # y = scipy.signal.hfilter(h, 1.0, x)
        """
        if data["ch_cnt"] == 0:
            warn = QtWidgets.QMessageBox.question(self, 'Empty!', 'No Data Has Been Loaded To Plotter',
                                    QtWidgets.QMessageBox.Ok)
            if warn == QtWidgets.QMessageBox.Ok:
                print('Return to Main')
            else:
                pass
        else:
            self.window6 = QtWidgets.QWidget()
            temp6 = Ui_fft_win()
            temp6.setupUi6(self, self.window6, data)
            self.window6.show()

    def plot_fft(self, data, ch_num, samp_rate, num_samps, time_ln, nyquist, start_t, end_t):
        # code: computes the fft and plots it
        # scaled = preprocessing.scale(self.lines[(ch_num-1)])

        print(start_t, end_t)

        if start_t > end_t:
            # error msg: incorrect values
            warn = QtWidgets.QMessageBox.question(self, 'Empty!', 'Start Time is after End Time',
                                    QtWidgets.QMessageBox.Ok)
            if warn == QtWidgets.QMessageBox.Ok:
                print('Return to Main')
            else:
                pass
        elif 0 > ch_num > data["ch_cnt"]:
            # error msg: channel outside of range
            warn = QtWidgets.QMessageBox.question(self, 'Empty!', 'Channel Number too High',
                                    QtWidgets.QMessageBox.Ok)
            if warn == QtWidgets.QMessageBox.Ok:
                print('Return to Main')
            else:
                pass
        else:
            self.figure2.clear()
            N = num_samps # Number of samplepoints
            Fs = samp_rate # Sample Rate
            # sample spacing
            T = 1.0 / Fs # N_samps*T (#samples x sample period) is the sample spacing.
            N_fft = samp_rate/100        # Number of bins (chooses granularity), samp_rate/10
            x = np.linspace(0.0, N*T, N) # the interval
            y = self.lines[(ch_num-1)][start_t:end_t]   # the signal

            # mean adjusted
            m_rem = np.ones_like(y)*np.mean(y)
            y = y - m_rem
            yf = fft(y, n=N_fft) # Compute the fft
            xf = np.arange(0,Fs,Fs/N_fft)
            # xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
            d = self.figure2.add_subplot(1,1,1)
            d.plot(xf,np.abs(yf), lw=2.0, c='b')
            d.set_ylabel('FFT magnitude (power)')
            d.set_xlabel('Frequency (Hz)')
            # d.set_title('FFT', fontsize= 20, fontweight="bold")
            self.canvas2.draw()

    def nleeg_hilbert(self, data):
        # scipy.signal.hilbert()
        if data["ch_cnt"] == 0:
            warn = QtWidgets.QMessageBox.question(self, 'Empty!', 'No Data Has Been Loaded To Plotter',
                                    QtWidgets.QMessageBox.Ok)
            if warn == QtWidgets.QMessageBox.Ok:
                print('Return to Main')
            else:
                pass
        else:
            self.window7 = QtWidgets.QWidget()
            temp7 = Ui_hilbert_win() #self.ui
            temp7.setupUi7(self, self.window7, data)
            self.window7.show()

    def plot_hilb(self, data, ch_num, samp_rate, num_samps, time_ln, nyquist, start_t, end_t):
        # code: computes the hilbert transform and plots it

        print(start_t, end_t)

        self.figure2.clear()
        a = self.figure2.add_subplot(1,1,1)
        self.figure2.tight_layout(pad=3.0, w_pad=1.0, h_pad=2.0)

        num_samps = end_t-start_t
        time = np.arange(0, num_samps)

        sig = self.lines[(ch_num-1)][start_t:end_t]

        # removing the mean of the signal
        mean_removed = np.ones_like(sig)*np.mean(sig)
        sig = sig - mean_removed

        an_sig = hilbert(sig)

        # envelope = math.sqrt((y.real**2) + (y.imag**2))
        env_real = an_sig.real ** 2
        env_imag = an_sig.imag ** 2
        combine = env_real + env_imag
        envelope = np.sqrt(combine)
        # print(envelope)
        inst_phase = np.unwrap(np.angle(an_sig))
        inst_freq = (np.diff(inst_phase)/(2*np.pi)*samp_rate)

        imagine = a.plot(time, an_sig.imag, color = 'black', linewidth=0.4, label="Imaginary")
        real = a.plot(time, an_sig.real, color = 'blue', linewidth=0.4, label="Real")
        envy = a.plot(time, envelope, color = 'green', linewidth=0.4, label="Envelope")
        # plt.legend()
        a.set_ylabel('Amplitude', fontsize=8)
        a.set_xlabel('Time', fontsize=8)
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)
        a.legend(loc='best')
        # a.set_title('Hilbert Transform', fontsize= 20, fontweight="bold")
        self.canvas2.draw()

# --------------------
# Right Panel Buttons
    def zoom_closer(self, data):
        #code: zoom in about 25%

        if data["ch_cnt"] == 0:
            warn = QtWidgets.QMessageBox.question(self, 'Empty!', 'No Data Has Been Loaded To Plotter',
                                    QtWidgets.QMessageBox.Ok)
            if warn == QtWidgets.QMessageBox.Ok:
                print('')
            else:
                pass
        elif self.xlim_max > 1000:
            try:
                self.xlim_min = int(self.xlim_min * 1.25)
                self.xlim_min = math.ceil(self.xlim_min / 1000) * 1000         
                self.xlim_max = int(self.xlim_max / 1.25)
                self.xlim_max = math.ceil(self.xlim_max / 1000) * 1000
                self.plot_arr[0].set_xlim(xmin=self.xlim_min, xmax=self.xlim_max)
                ticks_r = int(int(self.xlim_max - self.xlim_min)/4)
                self.plot_arr[0].set_xticks(np.arange(self.xlim_min, self.xlim_max, ticks_r))
                self.canvas.draw()
            except:
                print("Closest Zoom Position")
        else:
            print('Closest Zoom Position')

    def zoom_away(self, data):
        #code: zoom out about 25%
        if data["ch_cnt"] == 0:
            warn = QtWidgets.QMessageBox.question(self, 'Empty!', 'No Data Has Been Loaded To Plotter',
                                    QtWidgets.QMessageBox.Ok)
            if warn == QtWidgets.QMessageBox.Ok:
                print('')
            else:
                pass
        else:
            try:
                if self.xlim_max < 4000:
                    self.xlim_max = self.xlim_max + 1000
                else:
                    self.xlim_min = int(self.xlim_min / 1.25)
                    self.xlim_min = math.ceil(self.xlim_min / 1000) * 1000
                    self.xlim_max = int(self.xlim_max * 1.25)
                    self.xlim_max = math.ceil(self.xlim_max / 1000) * 1000

                self.plot_arr[0].set_xlim(xmin=self.xlim_min, xmax=self.xlim_max)
                ticks_r = int(int(self.xlim_max - self.xlim_min)/4)
                self.plot_arr[0].set_xticks(np.arange(self.xlim_min, self.xlim_max, ticks_r))
                self.canvas.draw()
            except:
                print("Fully Zoomed Out Position")

    def jump_to(self, data):
        #code: jump to a specific time position
        if data["ch_cnt"] == 0:
            warn = QtWidgets.QMessageBox.question(self, 'Empty!', 'No Data Has Been Loaded To Plotter',
                                    QtWidgets.QMessageBox.Ok)
            if warn == QtWidgets.QMessageBox.Ok:
                print('Return to Main')
            else:
                pass
        else:
            self.window4 = QtWidgets.QWidget()
            temp4 = Ui_jumpP()
            temp4.setupUi4(self, self.window4, data, self.mark_list)
            self.window4.show()

    def jump_to_load(self, data):
        #code: jumps to the specified data location

        margin = data/4
        if (data - margin) > 0:
            self.xlim_min = data - margin
        else:
            self.xlim_min = 0

        self.xlim_max = data + margin
        self.plot_arr[0].set_xlim(xmin=self.xlim_min, xmax=self.xlim_max)
        ticks_r = int(int(self.xlim_max - self.xlim_min)/4)
        self.plot_arr[0].set_xticks(np.arange(self.xlim_min, self.xlim_max, ticks_r))
        self.canvas.draw()

    def slice_D(self, data):
        #code: show/hide the ticks

        if data["ch_cnt"] == 0:
            warn = QtWidgets.QMessageBox.question(self, 'Empty!', 'No Data Has Been Loaded To Plotter',
                                    QtWidgets.QMessageBox.Ok)
            if warn == QtWidgets.QMessageBox.Ok:
                print('Return to Main')
            else:
                pass
        else:
            if data["tick_bool"] == True:
                for pl in range(0, len(self.plot_arr)):
                    self.plot_arr[pl].tick_params(   #Turns ticks off
                        axis='x',
                        which='major',
                        bottom='off',
                        top='off',
                        labelbottom='off')
                data["tick_bool"] = False    
            else:
                for pl in range(0,len(self.plot_arr)):
                    self.plot_arr[pl].tick_params(   #Turns ticks on
                        axis='x',
                        which='both',
                        bottom='on',
                        top='off',
                        labelbottom='on')
                data["tick_bool"] = True
            self.canvas.draw()


        # self.window5 = QtWidgets.QWidget()
        # temp5 = Ui_slice_D()
        # temp5.setupUi5(self.window5, data)
        # self.window5.show()

        """
        warn = QtWidgets.QMessageBox.question(self, 'Empty!', 'Unimplemented Feature',
                                    QtWidgets.QMessageBox.Yes) #| QtWidgets.QMessageBox.No)
        if warn == QtWidgets.QMessageBox.Yes:
            print('Return to Main')
        else:
            pass
        """

#---------------------
#
    def user_plot(self, user_string, data):
        # code:plots the user's algorithm
        self.figure2.clear()
        try:
            exec(user_string)
        except Exception as e:
            print(e)
            warn = QtWidgets.QMessageBox.question(self, 'Error', 'Code Input Error: Check Console For Clues',
                                    QtWidgets.QMessageBox.Ok) #| QtWidgets.QMessageBox.No)
            if warn == QtWidgets.QMessageBox.Ok:
                print('^ Error message above ^')
            else:
                pass

        """
        self.figure2.clear()
        ax = self.figure2.add_subplot(1,1,1)
        T = np.arange(0.0, 2.0, 0.01)
        Q = 1 + np.sin(2*np.pi*T)
        ax.plot(T, Q)
        plt.title('Simple Example')
        self.canvas2.draw()
        """

    def add_algo_win(self, data):
        # creates the script window
        self.window8 = QtWidgets.QWidget()
        temp8 = Ui_user_script()
        temp8.setupUi8(self, self.window8, data)
        self.window8.show()

    def add_algo(self, data, Form):
        #code: add another button to the ui
        if len(self.new_userAlgo_btn) < 3:
            self.new_userAlgo_btn.append(QtWidgets.QPushButton(Form))
            self.new_userAlgo_btn[self.button_cntr].setObjectName("new_userAlgo_btn"
                                                      + str(self.button_cntr))
            self.new_userAlgo_btn[self.button_cntr].setText('Script' 
                                                  + str((self.button_cntr+1)))
            self.new_userAlgo_btn[self.button_cntr].clicked.connect(
                                             lambda x:self.add_algo_win(data))
            self.horizontalLayout_2.addWidget(self.new_userAlgo_btn[self.button_cntr])
            self.button_cntr = self.button_cntr + 1

    def error(self):
        #code: delivers error message relating to algorithm usage
        warn = QtWidgets.QMessageBox.question(self, 'Empty!', 
                'Incorrect Channel or Start/End Time\n Try to fill all the Fields',
                                QtWidgets.QMessageBox.Ok)
        if warn == QtWidgets.QMessageBox.Ok:
            print('')
        else:
            pass

    def setupUi(self, Form, data):
        Form.setObjectName("Form")
        Form.resize(1200, 751)
        Form.setMaximumSize(QtCore.QSize(1200, 800))
        Form.move(24, 0)
        self.button_cntr = 0
        self.new_userAlgo_btn = []
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 12)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.script_save = ""
        self.mark_list = []

        # Plotting Canvas
        self.plotter = QtWidgets.QWidget()
        self.plotter.setLayout(QtWidgets.QVBoxLayout())
        self.plotter.layout().setContentsMargins(0,0,0,0)
        self.plotter.layout().setSpacing(0)
        self.plotter.setMinimumSize(QtCore.QSize(800, 600))

        # Plot details
        self.xinch = 11.392   # Exact size of plot window
        self.yinch = 9.3      # Exact size of plot window
        self.figure = plt.figure(num=1, dpi=70, figsize=(self.xinch, self.yinch)) #Scale depending on data
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.figure.tight_layout(pad=0.3, w_pad=0, h_pad=1.0)
        # self.canvas.draw()
        self.scroll = QtWidgets.QScrollArea(self.plotter)
        self.scroll.setWidget(self.canvas)
        self.plotter.layout().addWidget(self.scroll)


        self.horizontalLayout.addWidget(self.plotter)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        #Second Plotter
        self.plotter2 = QtWidgets.QWidget()
        self.plotter2.setLayout(QtWidgets.QVBoxLayout())
        self.plotter2.layout().setContentsMargins(0,0,0,0)
        self.plotter2.layout().setSpacing(0)
        self.plotter2.setMinimumSize(QtCore.QSize(300, 360))
        self.plotter2.setMaximumSize(QtCore.QSize(400, 360))
        self.figure2 = plt.figure(num=2, dpi=70, figsize=(3, 3))
        self.canvas2 = FigureCanvas(self.figure2)
        self.figure2.tight_layout(pad=0.3, w_pad=0, h_pad=1.0)
        self.canvas2.draw()
        self.plotter2.layout().addWidget(self.canvas2)


        self.verticalLayout_3.addWidget(self.plotter2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")  
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.toolbar) #canvas controller 

        #-------------
        # Zoom buttons #
        self.zoom_in = QtWidgets.QPushButton(Form)
        self.zoom_in.setObjectName("zoom_in")
        self.horizontalLayout_3.addWidget(self.zoom_in)
        self.zoom_in.clicked.connect(lambda x:self.zoom_closer(data))

        self.zoom_out = QtWidgets.QPushButton(Form)
        self.zoom_out.setObjectName("zoom_out")
        self.horizontalLayout_3.addWidget(self.zoom_out)
        self.zoom_out.clicked.connect(lambda x:self.zoom_away(data))

        self.jump_sec = QtWidgets.QPushButton(Form)
        self.jump_sec.setObjectName("jump_sec")
        self.horizontalLayout_3.addWidget(self.jump_sec)
        self.jump_sec.clicked.connect(lambda x:self.jump_to(data))

        self.slice_sec = QtWidgets.QPushButton(Form)
        self.slice_sec.setObjectName("slice_sec")
        self.horizontalLayout_3.addWidget(self.slice_sec)
        self.slice_sec.clicked.connect(lambda x:self.slice_D(data))
        #--------------

        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(600, 600))
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        #
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        font = QtGui.QFont("Andale Mono")
        font.setPointSize(14)
        # font.setBold(True)
        font.setUnderline(True)

        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setMinimumSize(QtCore.QSize(815, 10))
        self.label2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label2.setObjectName("label2")
        self.label2.setText(" EEG Plotter ")
        self.label2.setFont(font)

        self.label3 = QtWidgets.QLabel(Form)
        self.label3.setMinimumSize(QtCore.QSize(350, 10))
        self.label3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label3.setObjectName("label3")
        self.label3.setText(" Algorithm Plotter ")
        self.label3.setFont(font)

        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_4.addWidget(self.label2)
        self.horizontalLayout_4.addWidget(self.label3)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #Buttons Stack
        self.input_btn = QtWidgets.QPushButton(Form)
        self.input_btn.setObjectName("input_btn")
        self.horizontalLayout_2.addWidget(self.input_btn)
        self.input_btn.clicked.connect(lambda x:self.loadCsv(data))

        self.marker_btn = QtWidgets.QPushButton(Form)
        self.marker_btn.setObjectName("marker_btn")
        self.horizontalLayout_2.addWidget(self.marker_btn)
        self.marker_btn.clicked.connect(lambda x:self.loadMark(data))

        self.scalp_btn = QtWidgets.QPushButton(Form)
        self.scalp_btn.setObjectName("scalp_btn")
        self.horizontalLayout_2.addWidget(self.scalp_btn)
        self.scalp_btn.clicked.connect(lambda x:self.loadScalp())

        self.low_bandPass = QtWidgets.QPushButton(Form)
        self.low_bandPass.setObjectName("low_bandPass")
        self.horizontalLayout_2.addWidget(self.low_bandPass)
        self.low_bandPass.clicked.connect(lambda x:self.low_bandP(data))

        self.fft = QtWidgets.QPushButton(Form)
        self.fft.setObjectName("fft")
        self.horizontalLayout_2.addWidget(self.fft)
        self.fft.clicked.connect(lambda x:self.nleeg_fft(data))

        self.hilbert_btn = QtWidgets.QPushButton(Form)
        self.hilbert_btn.setObjectName("hilbert_btn")
        self.horizontalLayout_2.addWidget(self.hilbert_btn)
        self.hilbert_btn.clicked.connect(lambda x:self.nleeg_hilbert(data))

        self.save_btn = QtWidgets.QPushButton(Form)
        self.save_btn.setEnabled(True)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_2.addWidget(self.save_btn)
        #self.input_btn.clicked.connect(lambda x:self.hilbert(data))

        self.userAlgo_btn = QtWidgets.QPushButton(Form)
        self.userAlgo_btn.setObjectName("userAlgo_btn")
        self.horizontalLayout_2.addWidget(self.userAlgo_btn)
        self.userAlgo_btn.clicked.connect(lambda x:self.add_algo(data, Form))

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        Form.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Neuro Linguistic EEG"))

        self.zoom_in.setText(_translate("Form", "Zoom In"))
        self.zoom_out.setText(_translate("Form", "Zoom Out"))
        self.jump_sec.setText(_translate("Form", "Jump"))
        self.slice_sec.setText(_translate("Form", "Hide X-Axis"))
        self.input_btn.setText(_translate("Form", "Input Csv"))
        self.marker_btn.setText(_translate("Form", "Set Marker"))
        self.scalp_btn.setText(_translate("Form", "Scalp Map"))
        self.low_bandPass.setText(_translate("Form", "Band Pass"))
        self.fft.setText(_translate("Form", "FFT"))
        self.hilbert_btn.setText(_translate("Form", "Hilbert Transform"))
        self.userAlgo_btn.setText(_translate("Form", "..."))
        self.save_btn.setText(_translate("Form", "Save Csv"))








