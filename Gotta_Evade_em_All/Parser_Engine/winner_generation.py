"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class generates the winner based on arguments passed through the __init__ function."""

import json, os, csv, gc
import numpy as np

class winner_generation():

    def get_winner_and_msg(self):
        self.determine_score_range()
        return self.won, self.msg

    def determine_score_range(self):
        if self.score < 1:
            self.msg = 'sample appears fairly benign'
            self.won = True
        elif self.score < 2:
            self.msg = 'sample shows some signs of potential malicious behaviour'
            self.won = True
        elif self.score < 5:
            self.msg = 'sample shows numerous signs of malicious behaviour'
            self.won = False
        else:
            self.msg = 'sample is very suspicious'
            self.won = False

    def __init__(self, rawData):
        self.data = rawData
        self.score = self.data[0]
        self.won = False
        self.msg = ""
        