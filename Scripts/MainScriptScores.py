"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class generates the samples/score data."""

import os, sys
from multiprocessing import Pool
from shutil import copy

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from ScoresScraper.reportParser import scoreScraper
from Utils.rmv_xtr_nw_lns import rm_xtr_lns as rm
from Utils.rm_spch_mrks import rm_spch_mrks as rs

def main():
    pool = Pool(processes=2)
    pool.map(scoreScraper,[True,False])
    file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
    os.chdir(file_path)
    pool.map(rm, [['ScoresScraper\\','resultsB.csv'],['ScoresScraper\\','resultsM.csv']])
    pool.map(rs, [['ScoresScraper\\','resultsB.csv'],['ScoresScraper\\','resultsM.csv']])
    file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
    os.chdir(file_path)
    src1,src2 = "ScoresScraper/resultsB.csv", "ScoresScraper/resultsM.csv"
    dst1,dst2 = "Results/ScoresB.csv", "Results/ScoresM.csv" 
    copy(src1,dst1)
    copy(src2,dst2)

if __name__ == "__main__":
    main()


