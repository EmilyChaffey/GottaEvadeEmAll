"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class executes the code for generating the data for the comparison section in the report."""

import os, sys
from shutil import copy

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from Signature.comparison_gen import comparison_gen

def main():
    comparison_gen()
    file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
    os.chdir(file_path)
    src, dst = "Signature/comparison.csv", "Results/comparisonSigs.csv"    
    copy(src,dst)

if __name__ == "__main__":
    main()