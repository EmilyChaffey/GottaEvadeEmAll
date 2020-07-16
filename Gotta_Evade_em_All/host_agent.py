"""Gotta Evade 'em All - Emily Chaffey"""

""" This class is the agent for the host. It opens the Ubuntu vm and adds the HOST folder to it."""

import os, sys, time, subprocess, platform
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

def add_folder():
    print("Adding HOST Folder to VM...")
    file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
    os.chdir(file_path)
    path = os.path.abspath(file_path+"/HOST").replace("/","\\")
    subprocess.call(["vboxmanage", "sharedfolder", "add", "GottaEvadeEmAll", "--name", "HOST", "--hostpath", path ,"--automount"])
    print("Done")

def check_for_previous_report():
    print("Checking For Old report.json file...")
    path = 'HOST/Reports/report.json'
    if os.path.exists(path):
        print("File found, deleting...")
        if platform.system() == 'Linux':
            os.system('rm '+ path)
        elif platform.system() == 'Windows':
            pathRep = path.replace('/','\\')
            os.system('DEL '+pathRep)
        else: 
            sys.exit("OS Unknown...Stopping")
    print("Done")

def launch_vm():
    print("Starting VM...")
    subprocess.call(["vboxmanage", "startvm", "GottaEvadeEmAll"])
    print("Done")

def main():
    add_folder()
    check_for_previous_report()
    launch_vm()
    