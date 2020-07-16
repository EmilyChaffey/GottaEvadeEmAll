"""Gotta Evade 'em All - Emily Chaffey"""

""" This is the main. Running this class: opens the ubuntu vm, runs the parser engine, filters the categories and runs the visualisation software"""

import os, sys, subprocess
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from Final_Visualisation.visualisation_main import visualisation
from Categories_Filter.filter import cat_filter
from Parser_Engine.parser_engine import parser_engine
import host_agent

def pwr_off_vm():
    print("Power off VM...")
    subprocess.call(["vboxmanage", "controlvm", "GottaEvadeEmAll", "poweroff"])
    print("Done")

def main(args):
    stmt = False
    if not(len(args) == 1):
        stmt = True
    if not stmt:    
        host_agent.main()
    print("Starting Parser Engine...")
    parser_engine()
    print("Done")
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)
    cat_filter()
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)
    print("Starting Visualisation...")
    visualisation()
    print("Done")
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)
    if not stmt:
        pwr_off_vm()
    
if __name__ == "__main__":
    main(sys.argv)