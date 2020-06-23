"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class generates the binary values for the training data."""

import json, os, csv, gc
import numpy as np
from mlCreateCats import createCats

class trainingDataGen():
    def genSigs(self):
        dict_reader = open('training_sigs.csv','r')
        sigs = dict()
        for row in dict_reader:
            row_data = str(row).split(",")
            sigs[row_data[0]] =  row_data[1]
        dict_reader.close()
        return sigs

    def genTrainingData(self, genTraining):
        if genTraining:
            reader = open('trainingResults.csv','r')
        else:
            reader = open('testingResults.csv','r')
        sigs = self.genSigs()
        sig_dict = dict()
        for row in reader:
            row_data = str(row).split(",")
            number_of_items = len(row_data)
            signatures = ""
            for i in range(1,number_of_items-3):
                try: #testing for int
                    val=int(row_data[i]+"000") #ensuring no errors caused by decimals
                    break
                except ValueError: #STRING
                    val = sigs[row_data[i]]
                    signatures += str(val)+","
            if row_data[0] == "Sample":
                #make headers 
                sig_dict['Sample'] = 'Signatures, Score, Malware?'
            else:
                score = row_data[number_of_items-2]
                mal = row_data[number_of_items-1]
                newRowData = signatures + score + "," + mal
                sig_dict[row_data[0]] = newRowData.replace("\n","")
        reader.close()
        gc.collect()
        if genTraining:
            writer = open('training_data.csv', 'w')
        else:
            writer = open('testing_data.csv', 'w')
        for item in sig_dict:
            writer.write(str(item)+","+str(sig_dict[item])+"\n")
        writer.close()

    def __init__(self, genTraining): #gentraining determines if the data to be generated is training data or testing data.
        path = 'training_sigs.csv'
        if not os.path.exists(path): 
            createCats()
            gc.collect()
        self.genTrainingData(genTraining)
