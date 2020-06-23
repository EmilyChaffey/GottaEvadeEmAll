"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class contains utilities which are used by the parser engine in order to move, save and copy files."""

import os, sys, shutil, platform, csv
file_dir = os.path.dirname(__file__)

class utils():
    def save(self, moves, won, msg):
        print("Saving...")
        fileW =  open ('visualisation_data.csv','w',newline='')
        writer = csv.writer(fileW, delimiter = "\n")
        writer.writerow(["Moves"])
        writer.writerow(moves)
        writer.writerow(["Won",str(won)])
        writer.writerow(["Msg",msg])
        print("Done")

    def checkFolderExists(self, pathDir):
        if not os.path.exists(pathDir): #check to ensure the folder exists
            print("Destination Doesn't Exist")
            print("Creating folder...")
            if platform.system() == 'Linux':
                os.system('mkdir '+file_dir+'/'+pathDir)
            elif platform.system() == 'Windows':
                os.system('MKDIR '+file_dir.replace('/','\\')+'\\'+pathDir.replace('/','\\'))
                print("Folder created")
            else: 
                sys.exit("OS Unknown...Stopping")
            
    def copy(self, pathRep):
        print("Copying Report to Destination")
        self.checkFolderExists('Reports')
        if platform.system() == 'Linux':
            os.system('cp '+file_dir+'/'+pathRep+' ../Reports/')
        elif platform.system() == 'Windows':
            pathRep = '..\\HOST\\reports\\report.json'
            os.system('COPY '+file_dir.replace('/','\\')+'\\'+pathRep+' '+file_dir.replace('/','\\')+'\\Reports\\')
        else: 
            sys.exit("OS Unknown...Stopping")
        print("Done")

    def cpy_report(self):
        print("Checking Destination Exists")
        pathDir = '../HOST'
        self.checkFolderExists(pathDir)
        pathDir = '../HOST/reports'
        self.checkFolderExists(pathDir)
        pathRep = '../HOST/reports/report.json'
        while not os.path.exists(pathRep):
            pass #waiting for file to be generated
        self.copy(pathRep)
        print("Done")