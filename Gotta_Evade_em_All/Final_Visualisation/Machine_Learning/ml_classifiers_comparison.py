"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class compares different machine learning classifiers and generates graphs comparing them."""

import os, sys
file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
os.chdir(file_path)
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
import numpy as np
import ams_dataset as ams
import testing_dataset as testing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn import model_selection
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from matplotlib.offsetbox import AnchoredText

class mlComparison:

    def plt_pred_y(self, classifiers, y_test):
        correct_classifiers = ""
        colour_count = 0
        plt.title("Predictions vs Actual with Different Classifiers")
        plt.xlabel('Index of Sample')
        plt.ylabel('Predicted Label')            
        colours = ['blue', 'orange', 'lightseagreen','crimson', 'greenyellow', 'royalblue', 'yellow', 'teal', 'darkslateblue', 'darkorchid', 'darkorange']
        numberOfClassifiers = 0
        x_val = 1
        for name, classifier, graph_X, graph_Y in classifiers:
            numberOfClassifiers += 1
            if (colour_count == len(colours) - 1):
                colour_count = 0
            plt.scatter(x_val, graph_Y , color = colours[colour_count], label = name+": "+str(graph_Y))
            colour_count += 1
            x_val += 1
            if graph_Y == y_test:
                correct_classifiers += name + ", "
        plt.scatter(x_val, y_test, color = colours[len(colours) - 1], label = "y actual: ["+str(y_test)+"]")
        plt.legend()
        plt.savefig('pred.png')
        return correct_classifiers[:-2]

    def main(self):
        dataset = ams.load_dataset()
        X_train = dataset.data
        y_train = dataset.target

        test_data = testing.load_dataset()
        X_test = test_data.data
        y_test = test_data.target
        
        #classifiers structure = (name, classifier, graph_x_coord, graph_y_coord (which is y_pred))

        classifiers = [('1NN', KNeighborsClassifier(1), [], []),
                    ('3NN', KNeighborsClassifier(3), [], []),
                    ('5NN', KNeighborsClassifier(5), [], []),
                    ('Linear SVM', SVC(kernel="linear"), [], []),
                    ('RBF SVM', SVC(), [], []), #default kernal is RBF
                    ('Gaussian Process', GaussianProcessClassifier(), [], []),
                    ('Decision Tree', DecisionTreeClassifier(), [], []),
                    ('Random Forest', RandomForestClassifier(), [], []),
                    ('Neural Network', MLPClassifier(), [], []),
                    ('Ada Boost', AdaBoostClassifier(), [], []),
                    ('Naive Bayes', GaussianNB(), [], []),
                    ('QDA', QuadraticDiscriminantAnalysis(), [], [])]
        
        for name, classifer, graph_X, graph_Y in classifiers:
            classifer.fit(X_train, y_train)
            y_pred = classifer.predict(X_test.reshape(1, -1))
            count = 1
            for item in y_pred:
                graph_X.append(count)
                graph_Y.append(item)
                count += 1     
            
        return self.plt_pred_y(classifiers, y_test)
