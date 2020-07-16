"""Gotta Evade 'em All - Emily Chaffey"""

""" This class is the main for the parser engine. All of the parser engine's functionality is executed from here."""

import os, sys, shutil, platform
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


from extract import extract
from winner_generation import winner_generation as gen_winner
from move_generation import move_generation as gen_moves
from utils import utils


class parser_engine():
    def __init__(self):
        self.main()
        
    def main(self):
        file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
        os.chdir(file_path)
        # cpy report from shared folder (between vm and host) to another folder
        utils().cpy_report()
        # extract  relevant info
        raw_data = extract().getData()
        # convert into moves & winner
        moves = gen_moves(raw_data).get_moves()
        won, msg = gen_winner(raw_data).get_winner_and_msg()
        # save to file for visualisation program
        utils().save(moves, won, msg)