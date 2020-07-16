"""Gotta Evade 'em All - Emily Chaffey"""

""" This is the main class for accessing the scripts which generate the machine learning training data."""

import gc, os, sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from mlReportParser import reportParser as ml_report_parser
from mlTrainingDataParser import trainingDataParser as ml_training_parser
from mlTrainingDataGenerator import trainingDataGen
from mlFinalFormatting import finalForamtting

class main():
    def __init__(self):
        ml_report_parser(True)
        gc.collect() #garbage collection
        ml_report_parser(False)
        gc.collect()
        ml_training_parser()
        gc.collect()
        trainingDataGen()
        gc.collect()
        finalForamtting()
