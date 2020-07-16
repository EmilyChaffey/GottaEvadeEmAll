"""Gotta Evade 'em All - Emily Chaffey"""

""" This class adds the labels to the data - 1 = malware, 0 = benign"""

import csv, os
file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
os.chdir(file_path) 

class trainingDataParser():
    def __init__(self, genTraining):
        file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
        os.chdir(file_path)
        
        if genTraining:
            m_reader = open('results_M.csv', 'rb') 
            b_reader = open('results_B.csv', 'rb')
            listM = []
            for row in m_reader:
                val = str(row).replace("b'","").replace("'","").replace("\\r\\n","")
                val = val+", 1" #1 represents sample is malware
                listM.append(val)
            listB = []

            for row in b_reader:
                val = str(row).replace("b'","").replace("'","").replace("\\r\\n","")
                val = val+", 0" #0 represents sample is not a malware (i.e. it is benign)
                listB.append(val)

            total = listM+listB
            writer = open('trainingResults.csv', 'w')
            for item in total:
                val = str(item).replace('"b\'','').replace('"','') + "\n"
                writer.write(val)   
        else:
            testing_reader = open('testSample.csv', 'rb')
            listT = []
            for row in testing_reader:
                val = str(row).replace("b'","").replace("'","").replace("\\r\\n","")
                val = val+", 1" #1 represents sample is malware
                listT.append(val)
            writer = open('testingResults.csv', 'w')
            for item in listT:
                val = str(item).replace('"b\'','').replace('"','') + "\n"
                writer.write(val)      
        writer.close()