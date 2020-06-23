import os, csv, numpy as np
from MachineLearningScripts.mlMain import main as m
from sklearn.utils import Bunch

file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
os.chdir(file_path)

def load_dataset():
    m(False)
    pathDir = "/MachineLearningScripts/testing_data.csv"
    csv = np.genfromtxt(file_path+pathDir, delimiter=",", skip_header = 1)
    column = csv.shape[0]
    target = np.zeros(1)
    data = np.zeros(shape = (1, column-1))
    temp = np.zeros(column-1)
    for j in range(1, column-1):
        temp[j] = csv[j]
        data = temp
        target = csv[column-1]

    scores = list()
    scores.append(csv[column-2])


    reader = open(file_path+"/MachineLearningScripts/training_sigs.csv")
    sig_names = list()
    for row in reader:
        names = str(row).split(",")
        sig_names.append(names[0])

    return Bunch(data=data, target=target,  feature_names=sig_names, report_scores = scores)