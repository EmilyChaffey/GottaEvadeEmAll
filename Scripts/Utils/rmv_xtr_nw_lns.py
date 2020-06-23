"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class removes extra lines from data passed through the arguments."""

import os, csv

class rm_xtr_lns():
    def __init__(self, file_data):
        filePath, fileName = file_data[0], file_data[1]
        file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
        file_path = file_path.replace("Utils", filePath)
        os.chdir(file_path)
        fileR = open(fileName)
        newValues = []
        for row in fileR:
            if not row in ['\n', '\r\n']:
                val = str(row).replace("\\r\\n","")
                newValues.append(val)
        writer = open(fileName, 'w')
        for item in newValues:
            val = str(item)
            writer.write(val)
        writer.close()