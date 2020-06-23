"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class creates the categories for the training data."""

import json, os, csv, gc
import numpy as np

class createCats():
    def addSig(self,sigs, currentName, c):
        newVal = {currentName: c}
        sigs.update(newVal)
        count = c + 1
        return count 

    def checkIfAlreadyIn(self,sigs, currentName, c):
        count = c
        if not currentName in sigs:
            count = self.addSig(sigs, currentName, c)
        return count

    def malware(self):
        sig_dict = dict()
        sig_dict['Signature'] = 'keyvalue'
        inputdir = "../../../Reports/MalwareReports/"
        count = 1 
        for file in os.listdir(inputdir):
            json_file = open(inputdir+file)
            data = json.load(json_file)
            json_file.close()
            gc.collect()
            json_str = json.dumps(data)
            data = json.loads(json_str)
            signatures = data['signatures']
            for s in signatures:
                n = s['name']
                count = self.checkIfAlreadyIn(sig_dict, n, count)
        gc.collect()
        return sig_dict

    def benign(self, sig_dict):
        inputdir = "../Reports/BenignReports/"
        count = 1 
        for file in os.listdir(inputdir):
            json_file = open(inputdir+file)
            data = json.load(json_file)
            json_file.close()
            gc.collect()
            json_str = json.dumps(data)
            data = json.loads(json_str)
            signatures = data['signatures']
            for s in signatures:
                n = s['name']
                count = self.checkIfAlreadyIn(sig_dict, n, count)
        gc.collect()    
        return sig_dict

    def __init__(self): 
        sig_dict = self.malware()
        gc.collect()
        sig_dict = self.benign(sig_dict)
        gc.collect()
        writer = open('training_sigs.csv', 'w')
        for item in sig_dict:
            writer.write(str(item)+","+str(sig_dict[item])+"\n")
        writer.close()