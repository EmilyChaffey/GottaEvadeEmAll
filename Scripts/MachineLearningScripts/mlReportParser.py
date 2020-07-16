"""Gotta Evade 'em All - Emily Chaffey"""

""" This class is the report parser, which applies some transformations to the data."""

import json, os, csv, gc
import numpy as np


class reportParser():
    def increaseCount(self, sigs, currentName, sig, score):
        current = sigs[currentName]
        currentVal = str(current[0] )
        currentVal = currentVal + "," + str(sig)
        newVal = {currentName: [currentVal, score]}
        sigs.update(newVal)

    def addSig(self, sigs, currentName, sig, score):
        newVal = {currentName: [sig, score]}
        sigs.update(newVal)

    def checkIfAlreadyIn(self, sigs, currentName, sig, score):
        if currentName in sigs:
            self.increaseCount(sigs, currentName, sig, score)
        else:
            self.addSig(sigs, currentName, sig, score)

    def malware(self):
        sig_dict = dict()
        sig_dict['Sample'] = 'Signatures', 'Score'
        inputdir = "../Reports/MalwareReports/"
        for file in os.listdir(inputdir):
            json_file = open(inputdir+file)
            data = json.load(json_file)
            json_file.close()
            gc.collect()
            json_str = json.dumps(data)
            data = json.loads(json_str)
            dict_val = str(file).replace(".report.json", "")
            score = data ['info']['score']
            signatures = data['signatures']
            for s in signatures:
                n = s['name']
                self.checkIfAlreadyIn(sig_dict, dict_val, n, score)
            gc.collect()
        writer = open('results_M.csv', 'w')
        for item in sig_dict:
            n = str(item)
            si = str(sig_dict[item][0])
            sc = str(sig_dict[item][1]).replace('"','') + "\n"
            val = n +","+ si +","+ sc
            writer.write(val)
        writer.close()
    
    def benign(self):
        sig_dict = dict()
        sig_dict['Sample'] = 'Signatures', 'Score'
        inputdir = "../Reports/BenignReports/"
        for file in os.listdir(inputdir):
            json_file = open(inputdir+file)
            data = json.load(json_file)
            json_file.close()
            gc.collect()
            json_str = json.dumps(data)
            data = json.loads(json_str)
            dict_val = str(file).replace("report_", "").replace(".json","")
            score = data ['info']['score']
            signatures = data['signatures']
            for s in signatures:
                n = s['name']
                self.checkIfAlreadyIn(sig_dict, dict_val, n, score)
            gc.collect()
        writer = open('results_B.csv', 'w')
        for item in sig_dict:
            n = str(item)
            si = str(sig_dict[item][0])
            sc = str(sig_dict[item][1]).replace('"','') + "\n"
            val = n +"," + si +","+ sc
            writer.write(val)
        writer.close()

    def __init__(self, malicious):
        file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
        os.chdir(file_path)
        if malicious:
            self.malware()
        else:
            self.benign()
        

        