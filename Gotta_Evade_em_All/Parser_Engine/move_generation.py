"""Gotta Evade 'em All - Emily Chaffey"""

""" This class generates the moves based on the data passed through the arguments in the __init__ function."""

import json, os, csv, gc
import numpy as np

class move_generation():

    def get_moves(self):
        self.gen_moves()
        return self.moves

    def look_up_category(self, sig):
        fileR = open('../Categories_Filter/cuckoo_sig_categories.csv', 'r')
        reader = csv.DictReader(fileR)
        seen = []
        for row in reader:
            if str(row["name"]) == sig:
                rowStr = str(row["categories"]).replace("['", "").lower()
                rowStr = rowStr.replace(",", "")
                rowStr = rowStr.replace("]", "")
                rowStr = rowStr.replace("'", "")
                rowStr = rowStr.replace("-", "")
                split = rowStr.split(" ")
                if len(split) > 1 :
                    count = 0
                    for item in split: #only picking the first category for each signature
                        if count == 0 :
                            seen = (sig, item)
                            count += 1
                else:
                    seen = (sig, rowStr)
        fileR.close()
        return seen
    
    def gen_moves(self):
        for d in self.data:
            self.moves.append(self.look_up_category(d))

    def __init__(self, rawData):
        length = len(rawData)
        self.data = rawData[1:length-1]
        self.moves = []
     
