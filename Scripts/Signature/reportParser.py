"""Gotta Evade 'em All - Emily Chaffey"""

""" This takes the report for Cuckoo and begins the transformation process."""

import json, os, csv, sys
import numpy as np

class parserForReports():

    def increaseCount(self,sigs, currentName, currentDes):
        current = sigs[currentName]
        currentVal = current[0] + 1
        newVal = {currentName: [currentVal, currentDes]}
        sigs.update(newVal)

    def addSig(self,sigs, currentName, currentDes):
        newVal = {currentName: [1, currentDes]}
        sigs.update(newVal)

    def checkIfAlreadyIn(self,sigs, currentName, currentDes):
        if currentName in sigs:
            self.increaseCount(sigs, currentName, currentDes)
        else:
            self.addSig(sigs, currentName, currentDes)

    def malware(self):        
        sig_dict = dict()
        sig_dict['Signature'] = 'xVal; Occurrence', 'Description'
        inputdir = "../Reports/MalwareReports/"
        for file in os.listdir(inputdir):
            data = json.load(open(inputdir+file))
            json_str = json.dumps(data)
            data = json.loads(json_str)
            signatures = data['signatures']
            for s in signatures:
                n = s['name']
                d = s['description']
                self.checkIfAlreadyIn(sig_dict, n, d)
        fileW = open('resultsM.csv', 'w')
        writer = csv.writer(fileW, delimiter =";")
        count = 1
        for item in sig_dict:
            if not 'Signature' in str(item):
                n = str(item).replace("_","{\_}")
                occurrence = str(sig_dict[item][0]).replace("\"","")
                o = str(count)+";" + occurrence
                d = str(sig_dict[item][1]).replace("_","{\_}")
                count += 1
                val = [n,o,d]
            else:
                n = str(item).replace("_","{\_}")
                occurrence = str(sig_dict[item][0]).replace("\"","")
                o = occurrence
                d = str(sig_dict[item][1]).replace("_","{\_}")
                val = [n,o,d]
            writer.writerow(val)


    def benign(self):
        sig_dict = dict()
        sig_dict['Signature'] = 'xVal; Occurrence', 'Description'
        inputdir = "../Reports/BenignReports/"
        for file in os.listdir(inputdir):
            data = json.load(open(inputdir+file))
            json_str = json.dumps(data)
            data = json.loads(json_str)
            signatures = data['signatures']
            for s in signatures:
                n = s['name']
                d = s['description']
                self.checkIfAlreadyIn(sig_dict, n, d)
        fileW = open('resultsB.csv', 'w')
        writer = csv.writer(fileW, delimiter =";")
        count=1
        for item in sig_dict:
            if not 'Signature' in str(item):
                n = str(item).replace("_","{\_}")
                occurrence = str(sig_dict[item][0]).replace("\"","")
                o = str(count)+"; " + occurrence
                d = str(sig_dict[item][1]).replace("_","{\_}")
                count += 1
                val = [n,o,d]
            else:
                n = str(item).replace("_","{\_}")
                occurrence = str(sig_dict[item][0]).replace("\"","")
                o = occurrence
                d = str(sig_dict[item][1]).replace("_","{\_}")
                val = [n,o,d]
            writer.writerow(val)
            

    def __init__(self, mal):
        file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
        os.chdir(file_path)
        if mal: #if malware
            self.malware()
        else:
            self.benign()