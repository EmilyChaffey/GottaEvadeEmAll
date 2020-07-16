"""Gotta Evade 'em All - Emily Chaffey """

""" This class filters the categories, so that there is a more managable quantity"""

import csv, os
from re import search

class cat_filter():
    def __init__(self):
        self.main()
        
    def main(self):
        file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
        os.chdir(file_path)
        fileR = open('cuckoo_sig_categories.csv')
        fileW = open('categories.csv', 'w')
        reader = csv.DictReader(fileR)
        count = 0
        seen = set()
        for row in reader: 
            rowStr = str(row["categories"]).replace("['", "").lower() #removing all the unnecessary symbols/formatting
            rowStr = rowStr.replace(",", "")
            rowStr = rowStr.replace("]", "")
            rowStr = rowStr.replace("'", "")
            rowStr = rowStr.replace("-", "")
            
            if str(row["categories"] not in seen):
                rowContent = rowStr
                split = rowContent.split(" ")
                if len(split) > 1 : #if more than one category assigned to the signature
                    for item in split: #if item hasn't been seen before or been a substring or parent string to something already seen before
                        if (item not in seen) and (all(string not in item for string in seen)) and (all(item not in string for string in seen)):
                            seen.add(item)
                else:
                    rowContent = rowContent.replace("']","")
                    if (rowContent not in seen) and (all(string not in rowContent for string in seen)) and (all(rowContent not in string for string in seen)):
                        seen.add(rowContent)
            count += 1
        writer = csv.writer(fileW, delimiter = "\n")
        writer.writerow(sorted(seen))
