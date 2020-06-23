"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class takes the report generated by Cuckoo and applies some functions to it to begin its transformation into training data."""

import json, os, csv, gc
import numpy as np
from mlCreateCats import createCats

class finalForamtting():
    def genSigs(self):
        dict_reader = open('training_sigs.csv','r')
        sigs = dict()
        for row in dict_reader:
            row_data = str(row).split(",")
            sigs[row_data[0]] =  row_data[1]
        dict_reader.close()
        return sigs

    def genTrainingData(self):
        reader = open('training_data.csv','r')
        sigs = self.genSigs()
        sig_dict = dict()
        for row in reader:
            row_data = str(row).split(",")
            number_of_items = len(row_data)
            sample_sigs = np.zeros(len(sigs)) #contains the binary options of whether the current sample has certain signatures 1 = yes, 0 = no
            for i in range(1,number_of_items-3): # index 0 = sample number, n-2 = score, n-1 = malware t or f
                    sample_sigs[int(row_data[i])] = 1
            if row_data[0] == "Sample":
                #make headers 
                sig_dict['Sample'] = 'Signatures, Score, Malware?'
            else:
                score = row_data[number_of_items-2]
                mal = row_data[number_of_items-1]
                signatures = ""
                for s in sample_sigs:
                    signatures += str(s) + ","
                newRowData = signatures + score + "," + mal
                sig_dict[row_data[0]] = newRowData.replace("\n","")
        reader.close()
        gc.collect()
        writer = open('training_data.csv', 'w')
        for item in sig_dict:
            writer.write(str(item)+","+str(sig_dict[item])+"\n")
        writer.close()

    def __init__(self):
        path = 'training_sigs.csv'
        if not os.path.exists(path): 
            createCats()
            gc.collect()
        self.genTrainingData()
