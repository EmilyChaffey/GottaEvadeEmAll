"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class generates the comparison data for the reports."""

import csv, os
file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
os.chdir(file_path) 

class comparison_gen():
    def genSigs(self, fileName):
        dict_reader = open(fileName,'r')
        sigs = dict()
        for row in dict_reader:
            row_data = str(row).split(";")
            sigs[row_data[0]] =  row_data[2]
        dict_reader.close()
        return sigs
        
    def __init__(self):
        file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
        os.chdir(file_path)
        m_dict = self.genSigs('resultsM.csv') 
        b_dict = self.genSigs('resultsB.csv')

        comp = []

        for sigB in b_dict:
            if str(sigB) == "Signature":
                comp.append("Signature;OccurrenceB;OccurrenceM")
            elif sigB in m_dict.keys():
                comp.append(str(sigB)+";"+str(b_dict[sigB])+";"+str(m_dict[sigB]))
        
        writer = open('comparison.csv','w')
        for item in comp:
            val = str(item)+ "\n"
            writer.write(val)
        writer.close()