"""Gotta Evade 'em All - Emily Chaffey"""

""" This is the main class for the visualisation system."""

import arcade as arc
import os,sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from communal_data import communal_data
from start import start
from battle import battle
from manager import Manager

class visualisation ():
    def __init__(self):
        self.main()

    def main(self):
        file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
        os.chdir(file_path)
        data = communal_data()
        window = data.getWindow()
        manager = Manager(data)
        start_view = start(data, manager)
        window.show_view(start_view)
        arc.run()

if __name__ == "__main__":
    visualisation()    