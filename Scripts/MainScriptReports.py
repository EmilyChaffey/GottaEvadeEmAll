"""Gotta Evade 'em All - Emily Chaffey"""

""" This class generates the data used for occurrence of signatures for use in the reports."""

import os, sys
from multiprocessing import Pool
from shutil import copy

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from Signature.reportParser import parserForReports
from Utils.rmv_xtr_nw_lns import rm_xtr_lns as rm
from Utils.rm_spch_mrks import rm_spch_mrks as rs

def main():
    pool = Pool(processes=2)
    pool.map(parserForReports,[True,False])
    file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
    os.chdir(file_path)
    pool.map(rm, [['Signature\\','resultsB.csv'],['Signature\\','resultsM.csv']])
    pool.map(rs, [['Signature\\','resultsB.csv'],['Signature\\','resultsM.csv']])
    file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
    os.chdir(file_path)
    src1, src2 = "Signature/resultsB.csv", "Signature/resultsM.csv"
    dst1, dst2 = "Results/SignaturesB.csv","Results/SignaturesM.csv"    
    copy(src1,dst1)
    copy(src2,dst2)

if __name__ == "__main__":
    main()


