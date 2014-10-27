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


class Exp():
    def __init__ (self):
        positionX = np.linspace(-23.5, 23.5, num=10, endpoint=True, retstep=False)
        positionY = np.linspace(-14.1, 14.1, num=6, endpoint=True, retstep=False)
        xys = np.transpose([np.tile(positionX, len(positionY)), np.repeat(positionY, len(positionX))])
        self.positions = xys
        self.counter = 0
        self.waitForKeys = True
        mon = monitors.Monitor('myMonitor1')
        self.window = visual.Window(size=mon.getSizePix(), color=(1,1,1), colorSpace='rgb', fullscr=True, monitor=mon, units='cm')
        self.window.mouseVisible = False
        self.resultData = np.zeros(shape = (360,7),dtype=np.float64)

        
        fixationX = visual.Line(win=self.window, lineColor=(-1,-1,-1), lineColorSpace='rgb', start=(-0.5,0), end=(0.5,0),lineWidth = 2.5, interpolate=False)
        fixationY = visual.Line(win=self.window, lineColor=(-1,-1,-1), lineColorSpace='rgb', start=(0,-0.5), end=(0,0.5),lineWidth = 2.5, interpolate=False)
        self.fixation = [fixationX, fixationY]
        
        
        self.text1 = visual.TextStim(win=self.window, text='Ist', color=(-1,-1,-1), colorSpace='rgb', height=2, bold=True, wrapWidth=50, pos=(0.0, 2))
        self.text3 = visual.TextStim(win=self.window, text='im folgenden Bild enthalten?', color=(-1,-1,-1), colorSpace='rgb', height=2, bold=True, wrapWidth=50, pos=(0.0, -2.0))
        
        
        imgStart1 = visual.SimpleImageStim(win=self.window, image="..\\img\\auftrag1.png")
        imgStart2 = visual.SimpleImageStim(win=self.window, image="..\\img\\aufgabe2.png")
        imgPractice1 = visual.SimpleImageStim(win=self.window, image="..\\img\\training1.png")
        imgExperiment = visual.SimpleImageStim(win=self.window, image="..\\img\\Versuch.jpg")
        thankyou = visual.SimpleImageStim(win=self.window, image="..\\img\\danke.jpg")
        
        # block slides
        block1 = visual.SimpleImageStim(win=self.window, image="..\\img\\Block_1.jpg")
        block2 = visual.SimpleImageStim(win=self.window, image="..\\img\\Block_2.jpg")
        block3 = visual.SimpleImageStim(win=self.window, image="..\\img\\Block_3.jpg")
        block4 = visual.SimpleImageStim(win=self.window, image="..\\img\\Block_4.jpg")
        block5 = visual.SimpleImageStim(win=self.window, image="..\\img\\Block_5.jpg")
        block6 = visual.SimpleImageStim(win=self.window, image="..\\img\\Block_6.jpg")
        
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
                
        self.instructions = {'start1': imgStart1,
                             'start2': imgStart2,
                             'practice1': imgPractice1,
                             'experiment': imgExperiment,
                             'danke': thankyou,
                             'block1': block1,
                             'block2': block2,
                             'block3': block3,
                             'block4': block4,
                             'block5': block5,
                             'block6': block6
                             }
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
        
        '''creating the constellation using the code for six time: constellation = random.sample(xrange(1, 61), 60)'''
        constellation1 = [7, 43, 46, 16, 27, 5, 31, 36, 44, 52, 22, 25, 59, 24, 17, 48, 8, 32, 40, 20, 29, 21, 57, 15, 26, 13, 10, 35, 53, 2, 51, 30, 33, 38, 47, 34, 3, 55, 4, 6, 50, 23, 28, 12, 54, 1, 9, 60, 18, 37, 42, 39, 11, 19, 14, 41, 45, 58, 56, 49]
        constellation2 = [29, 9, 1, 4, 45, 3, 35, 16, 13, 22, 57, 25, 24, 37, 19, 26, 60, 32, 59, 36, 2, 18, 46, 58, 14, 48, 49, 44, 12, 39, 38, 40, 56, 8, 51, 28, 47, 43, 50, 34, 41, 21, 55, 31, 33, 17, 53, 42, 30, 15, 23, 11, 7, 52, 20, 54, 10, 6, 27, 5]
        constellation3 = [57, 19, 53, 47, 13, 55, 14, 52, 29, 39, 9, 1, 25, 38, 18, 56, 49, 31, 28, 15, 3, 5, 4, 54, 58, 41, 27, 2, 44, 59, 35, 60, 24, 16, 40, 23, 43, 34, 32, 20, 17, 37, 6, 26, 33, 45, 51, 11, 50, 46, 30, 8, 36, 22, 48, 12, 21, 7, 42, 10]
        constellation4 = [13, 27, 32, 49, 2, 57, 35, 60, 11, 25, 19, 5, 59, 24, 34, 6, 54, 21, 3, 51, 52, 23, 18, 31, 42, 45, 9, 10, 15, 38, 16, 53, 47, 8, 22, 37, 4, 40, 44, 17, 58, 7, 29, 46, 12, 20, 39, 26, 50, 56, 14, 1, 43, 33, 36, 30, 41, 55, 48, 28]
        constellation5 = [51, 27, 15, 48, 59, 20, 9, 19, 53, 13, 43, 39, 37, 58, 38, 45, 47, 40, 31, 17, 18, 26, 30, 8, 32, 4, 55, 54, 56, 25, 14, 50, 1, 12, 28, 16, 10, 44, 52, 24, 3, 34, 6, 5, 42, 35, 46, 36, 57, 7, 23, 11, 21, 22, 60, 2, 41, 49, 29, 33]
        constellation6 = [20, 60, 35, 54, 26, 7, 4, 29, 30, 59, 34, 37, 42, 1, 46, 48, 9, 31, 21, 36, 32, 45, 5, 33, 53, 14, 22, 11, 55, 23, 18, 28, 52, 2, 25, 41, 51, 47, 43, 27, 10, 57, 6, 40, 50, 49, 19, 39, 56, 13, 8, 12, 16, 3, 17, 38, 15, 24, 44, 58]
        constellationPrac = [19, 43, 39, 13, 12, 46, 25, 41, 16, 60, 20, 49, 8, 33, 36, 35, 9, 37, 21, 42, 31, 55, 23, 24, 34, 57, 53, 5, 18, 14, 32, 1, 26, 11, 3, 50, 15, 4, 30, 58, 22, 54, 56, 45, 28, 47, 38, 40, 29, 44, 10, 59, 7, 6, 52, 27, 51, 17, 48, 2]
        
        '''a dict to access the constellation block wise'''
        self.constellation = {
                         1 : constellation1,
                         2 : constellation2,
                         3 : constellation3,
                         4 : constellation4,
                         5 : constellation5,
                         6 : constellation6,
                         7 : constellationPrac
                         }        

    def showAndSetImage(self,pointsPlot):
        for img in pointsPlot:
            self.counter += 1
            a = self.positions[self.counter - 1]
            self.images[img].setPos(a)
            self.images[img].draw()
        self.window.flip()
    def quit(self):
        self.window.getMovieFrame(buffer='front')
        self.window.saveMovieFrames('stimuli1.png')
    def run(self):
        blockNo=1
        self.showAndSetImage(self.constellation[blockNo])
        key = event.waitKeys(keyList=['escape'])
        if key[0] == 'escape':
                '''Escape quits the program by calling the method self.quit()'''
                self.quit()
exp = Exp()
exp.run()  

                    