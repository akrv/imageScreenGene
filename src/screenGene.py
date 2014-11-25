'''
Created on 16.09.2014

@author: Aswin
'''
from __future__ import division
from psychopy import visual, core, event, monitors
import datetime
import numpy as np
import os
import random
from Image import Image
from iViewXAPI import *            #iViewX library


class Exp():
    def __init__ (self):
        self.waitForKeys = True
        mon = monitors.Monitor('myMonitor1')
        self.window = visual.Window(size=mon.getSizePix(), color=(1,1,1), colorSpace='rgb', fullscr=True, monitor=mon, units='cm')
        self.window.mouseVisible = False

        fixationX = visual.Line(win=self.window, lineColor=(-1,-1,-1), lineColorSpace='rgb', start=(-0.5,0), end=(0.5,0),lineWidth = 2.5, interpolate=False)
        fixationY = visual.Line(win=self.window, lineColor=(-1,-1,-1), lineColorSpace='rgb', start=(0,-0.5), end=(0,0.5),lineWidth = 2.5, interpolate=False)
        self.fixation = [fixationX, fixationY]
#
#
#

        'creating the stimulus'
        self.redCircle = visual.ImageStim(win=self.window, image="..\\img\\shapes_13.jpg", units = "cm", pos=(0,0), size = 3.4, contrast=1.0)
        self.greenCircle = visual.ImageStim(win=self.window, image="..\\img\\shapes_11.jpg", units = "cm", pos=(0,0), size = 3.4, contrast=1.0)
        self.redTriangle = visual.ImageStim(win=self.window, image="..\\img\\shapes_15.jpg", units = "cm", pos=(0,0), size = 3.4, ori = -90, contrast=1.0)
        self.greenTriangle = visual.ImageStim(win=self.window, image="..\\img\\shapes_17.png", units = "cm", pos=(0,0), size = 3.4, contrast=1.0)
        self.redSquare = visual.ImageStim(win=self.window, image="..\\img\\shapes_03.jpg", units = "cm", pos=(0,0), size = 3.4, contrast=1.0)
        self.greenSquare = visual.ImageStim(win=self.window, image="..\\img\\shapes_05.jpg", units = "cm", pos=(0,0), size = 3.4, contrast=1.0)
        self.greenRhombus = visual.ImageStim(win=self.window, image="..\\img\\shapes_07.jpg", units = "cm", pos=(0,0), size = 3.4, contrast=1.0)
        self.greenSquareOpen = visual.ImageStim(win=self.window, image="..\\img\\shapes_09.jpg", units = "cm", pos=(0,0), size = 3.4, contrast=1.0)
        self.star4 = visual.ImageStim(win=self.window, image="..\\img\\shapes_25.jpg", units = "cm", pos=(0,0), size = 3.4, contrast=1.0)
        self.star5 = visual.ImageStim(win=self.window, image="..\\img\\shapes_20.jpg", units = "cm", pos=(0,0), size = 3.4, contrast=1.0)


        self.PoI = np.array([ [-10,0], [10,0], [0,10], [0,-10]])


        '''generating a dict with keys 1 to 60 of all the necessary images'''
        self.images = {}
        for x in range(1,17):
            self.images[x] = self.redCircle

        x += 1
        self.images[x] = self.greenCircle

        for x in range (18,29):
            self.images[x] = self.redSquare

        for x in range (29,40):
            self.images[x] = self.greenSquare

        x += 1
        self.images[x] = self.greenSquareOpen

        x += 1
        self.images[x] = self.greenRhombus

        x += 1
        self.images[x] = self.redTriangle

        for x in range (43,59):
            self.images[x] = self.star4

        x += 1
        self.images[x] = self.star5

        x += 1
        self.images[x] = self.greenTriangle

        subjects = 1110
        self.subject = 1110
        self.useSMI = True

        #=======================================================================
        # SMI Handling
        # filefolder should be common for both the computers???
        #=======================================================================
        pathOnLaptop = 'D:\\Renker\\TunnelExpSmi\\data\\'
        Filename = str(subjects)+'_SMI_'
        self.outputfile = pathOnLaptop + Filename + str(subjects)
        self.outputfilecalib = pathOnLaptop + Filename + '_Calib' + str(subjects)

        # ---------------------------------------------
        #---- connect to iViewX
        # ---------------------------------------------
        sendIp='169.254.154.199'  #Eyetracker laptop IP
        recvIp='169.254.154.5'   #psychoPy computer IP

        res = iViewXAPI.iV_SetLogger(c_int(1), c_char_p("iViewXSDK_TrackerTest.txt"))
        res = iViewXAPI.iV_Connect(c_char_p(sendIp), c_int(4444), c_char_p(recvIp), c_int(5555))

        print 'res:' + str(res)
        res = iViewXAPI.iV_GetSystemInfo(byref(systemData))
        print "iV_GetSystemInfo: " + str(res)
        print "Samplerate: " + str(systemData.samplerate)
        print "iViewX Version: " + str(systemData.iV_MajorVersion) + "." + str(systemData.iV_MinorVersion) + "." + str(systemData.iV_Buildnumber)
        print "iViewX API Version: " + str(systemData.API_MajorVersion) + "." + str(systemData.API_MinorVersion) + "." + str(systemData.API_Buildnumber)

        self.trial = range(4)

    def calibration(self,calibrate):
        '''
        # SMI calibration method
        '''
        if calibrate:
            cali=1
            while cali==1:
                calibrationData = CCalibration(9, 1, 1, 0, 1, 250, 220, 2, 20, b"")
                accuracyData = CValidation(-1,-1,-1,-1)
                res = iViewXAPI.iV_SetupCalibration(byref(calibrationData))
                print "iV_SetupCalibration " + str(res)
                res = iViewXAPI.iV_Calibrate()
                print "iV_Calibrate " + str(res)
                res = iViewXAPI.iV_Validate()
                print "iV_Validate " + str(res)

                res = iViewXAPI.iV_GetAccuracy(byref(accuracyData), 0)
                print "iV_GetAccuracy " + str(res)
                print "deviationXLeft " + str(accuracyData.deviationLX) + " deviationYLeft " + str(accuracyData.deviationLY)
                print "deviationXRight " + str(accuracyData.deviationRX) + " deviationYRight " + str(accuracyData.deviationRX)
                res = iViewXAPI.iV_SaveCalibration(self.outputfilecalib)
                print "Saving Calibration data " + str(res)
                self.window.flip()
                key = event.waitKeys(keyList=['space','escape','w'])
                if key[0] == 'escape':
                    self.quit()
                if key[0] == 'space':
                    cali=2
                if key[0] == 'w':
                    cali=1
        else :
            print "no calibaration"

    def showText(self, txt):
        textObj = visual.TextStim(win=self.window, text=txt, color=(-1,-1,-1), colorSpace='rgb', height=2, bold=True, wrapWidth=50)
        textObj.draw()
        self.window.flip()

        key = event.waitKeys(keyList=['space','escape'])
        if key[0] == 'escape':
            self.quit()
        self.window.flip()

    def showAndSetImage(self,pointsPlot):
        self.images[17].setPos(pointsPlot)
        self.images[17].draw()
        self.window.flip()

    def drawFixation(self):
        for f in self.fixation:
            f.draw()
        self.window.flip()
        core.wait(1)

    def quit(self):
        self.window.close()
        if self.useSMI:
            iViewXAPI.iV_StopRecording() #stop eye tracker
            res = iViewXAPI.iV_SaveData(str(self.outputfile), str('TunnelExpSmi'), str(self.subject), 0)
            iViewXAPI.iV_Disconnect() # disconnect the eyetracker connection
        core.quit()

    def run(self):
        if self.useSMI:
            self.showText("Kalibrierung")
            self.calibration(True)
        idx = range(4)
        for j in self.trial:
            self.showText("Trial: " + str(j))
            random.shuffle(idx)
            self.drawFixation()
            if self.useSMI:
                iViewXAPI.iV_StartRecording()
                iViewXAPI.iV_SendImageMessage(c_char_p('Trigger '+ str(j)))
            for i in idx:
                self.showAndSetImage(self.PoI[i])
                while(core.wait(2)):
                    key = event.waitKeys(keyList=['escape','space'])
                    if key[0] == 'escape':
                            '''Escape quits the program by calling the method self.quit()'''
                            self.quit()
        self.quit()


exp = Exp()
exp.run()

