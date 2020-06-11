import os, csv, numpy as np
from sklearn.utils import Bunch
from MachineLearningScripts.mlMain import main as m

file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
os.chdir(file_path)

def load_dataset():
    path = file_path+'/MachineLearningScripts/training_sigs.csv'
    if not os.path.exists(path): 
        m(True)
    csv = np.genfromtxt(file_path+"/MachineLearningScripts/training_data.csv", delimiter=",", skip_header = 1)
    row = csv.shape[0]
    column = csv.shape[1]
    target = np.zeros(row)
    data = np.zeros(shape = (row, column-1))
    temp = np.zeros(column-1)
    for i in range(row):
        for j in range(1, column-1):
            temp[j] = csv[i][j]
        data[i] = temp
        target[i] = csv[i][column-1]

    scores = list()

    for r in range(row):
        scores.append(csv[r][column-2])


    reader = open(file_path+"/MachineLearningScripts/training_sigs.csv")
    sig_names = list()
    for row in reader:
        names = str(row).split(",")
        sig_names.append(names[0])

    return Bunch(data=data, target=target,  feature_names=sig_names, report_scores = scores)