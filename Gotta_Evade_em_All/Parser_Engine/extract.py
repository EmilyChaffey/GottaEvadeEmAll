"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class extracts the relevant data from the report."""

import json, os, csv, gc
import numpy as np

class extract():

    def getData(self):
        return self.data

    def genData(self):
        inputdir = "../HOST/Reports/"
        for file in os.listdir(inputdir):
            json_file = open(inputdir+file)
            data = json.load(json_file)
            json_file.close()
            gc.collect()
            json_str = json.dumps(data)
            data = json.loads(json_str)
            score = data ['info']['score']
            self.data.append(score)
            signatures = data['signatures']
            for s in signatures:
                n = s['name']
                self.data.append(n)
            gc.collect()
        writer = open('results.csv', 'w')
        for item in self.data:
            writer.write(str(item))
        writer.close()


    def __init__(self):
        file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
        os.chdir(file_path)
        self.data = []
        self.genData()
