"""Gotta Evade 'em All - Emily Chaffey"""

""" This class contains the code for running the scripts for generating the trainging data for the machine learning scripts."""

import os, sys, shutil

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from MachineLearningScripts.mlMain import main as m

def main():
    m()
    #copy and move training data file from ML folder to the Results folder
    file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
    os.chdir(file_path)
    src = "MachineLearningScripts/training_data.csv"
    dst = "Results/"
    shutil.copy(src,dst)


if __name__ == "__main__":
    main()