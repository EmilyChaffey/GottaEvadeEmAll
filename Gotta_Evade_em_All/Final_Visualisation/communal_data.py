"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This is a singleton class which stores all of the visualisation data. It has getters and setters so that the data is easy to access."""

import arcade as arc
import os, csv
from current_status import currentStatus
from Machine_Learning.ml_classifiers_comparison import mlComparison

class communal_data ():
    file_path = os.path.dirname(os.path.abspath(__file__)) #These two lines of code enable the program to know where its file directory sits so that it can load files.
    os.chdir(file_path)
    
    WIDTH = 0
    HEIGHT = 0
    TITLE = '0'
    STATUS = currentStatus.BATTLE_ROUND_M
    WINDOW = 0
    WINNER = 'AMS'
    CURRENT_ROUND = 0

    MAIN_BACKGROUND = None
    START_BACKGROUND = None
    MALWARE_ICON = None
    AMS_ICON = None
    ENCOUNTER_1 = None
    ENCOUNTER_2 = None
    M_BATTLE_start_1 = None
    M_BATTLE_start_2 = None
    M_BATTLE_start_3 = None
    m_mv_imgs = []
    ams_mv_imgs = []
    no_of_rounds = 0

    def __init__(self):
        self.MAIN_BACKGROUND = arc.load_texture("imgs/background.jpg")
        self.START_BACKGROUND = arc.load_texture("imgs/start.png")
        self.MALWARE_ICON = arc.load_texture("imgs/malware.png")
        self.AMS_ICON = arc.load_texture("imgs/ams.png")
        self.ENCOUNTER_1 = arc.load_texture("imgs/encounter_1.png")
        self.ENCOUNTER_2 = arc.load_texture("imgs/encounter_2.png")
        self.M_BATTLE_start_1 = arc.load_texture("imgs/battle_m_1.png")
        self.M_BATTLE_start_2 = arc.load_texture("imgs/battle_m_6.png")
        self.M_BATTLE_start_3 = arc.load_texture("imgs/battle_m_7.png")
        self.WIDTH = 1200
        self.HEIGHT = 1000
        self.TITLE = 'Gotta Evade \'em All!'
        self.STATUS = currentStatus.ENCOUNTER
        self.loadData()
        self.determineWhoWon()
        self.load_m_move_imgs()
        self.load_ams_move_imgs()
        self.no_of_rounds = len(self.m_mv_imgs)
        self.WINDOW = arc.Window(self.WIDTH,self.HEIGHT,self.TITLE)
        self.correct_classifiers = ""


    def getMsg(self):
        return self.msg
    def getNoOfRounds(self):
        return self.no_of_rounds
    def getCurrentRound(self):
        return self.CURRENT_ROUND
    def getWidth(self):
        return self.WIDTH
    def getHeight(self):
        return self.HEIGHT
    def getTitle(self):
        return self.TITLE
    def getStatus(self):
        return self.STATUS
    def setStatus(self, newStatus):
        self.STATUS = newStatus
    def getWinner(self):
        return self.WINNER
    def getWonBackground(self):
        self.determineWhichWinner()
        return self.WON_BACKGROUND
    def getStartBackground(self):
        return self.START_BACKGROUND
    def getMainBackground(self):
        return self.MAIN_BACKGROUND
    def getMalwareIcon(self):
        return self.MALWARE_ICON
    def getAMSicon(self):
        return self.AMS_ICON
    def getEncounter1(self):
        return self.ENCOUNTER_1
    def getEncounter2(self):
        return self.ENCOUNTER_2
    def getWindow(self):
        return self.WINDOW
    def getBattle(self):
        if(self.STATUS == currentStatus.BATTLE_ROUND_M):
            return self.M_BATTLE_start_1, self.M_BATTLE_start_2, self.M_BATTLE_start_3, self.m_mv_imgs, self.moves
        else:
            return self.ams_mv_imgs, self.moves

    def setWinner(self,newWinner):
        self.WINNER = newWinner

    def determineWhichWinner(self):
        if(self.WINNER == 'AMS'):
            self.WON_BACKGROUND = arc.load_texture("imgs/ams_won.png")
        else:
            self.WON_BACKGROUND = arc.load_texture("imgs/m_won.png")

    def switchView(self, nextView):
        self.WINDOW.show_view(nextView)

    def setCurrentRound(self, newRound):
        self.CURRENT_ROUND = newRound

    def determineWhoWon(self):
        if self.malware_won:
            self.WINNER = 'Mal'
        else: #self.ams_won == true
            self.WINNER = 'AMS'

    def loadData(self):
        reader = open ('../Parser_Engine/visualisation_data.csv', 'r')
        self.moves = []
        self.malware_won = False
        self.msg = ""
        current = 0
        for row in reader:
            str_row = str(row).strip()
            if str_row == "Moves":
                current = 1
            elif str_row == "Won":
                current = 2
            elif str_row == "Msg":
                current = 3
            else:
                if current == 1:
                    name, move = str_row.replace('(','').replace(')','').replace("'","").split(", ")
                    self.moves.append((name, move))
                elif current == 2:
                    self.malware_won = (str_row == "True")
                elif current == 3:
                    self.msg = str_row

    def look_up_img_ref(self, m):
        fileR = open('img_lookup.csv', 'r')
        reader = csv.DictReader(fileR)
        for row in reader:
            if m.lower() in str(row["Category"]).lower() or str(row["Category"]).lower() in m.lower():
                return str(row["Ref"])


    def load_m_move_imgs(self):
        move_imgs_ref = []
        for m in self.moves:
            move_imgs_ref.append(self.look_up_img_ref(m[1]))
        for ref in move_imgs_ref:
            self.m_mv_imgs.append(arc.load_texture("imgs/"+str(ref)+".png"))

    def load_ams_move_imgs(self):
        for i in range(1,7):
            self.ams_mv_imgs.append(arc.load_texture("imgs/battle_ams_"+str(i)+".png"))

    def genML(self):
        self.correct_classifiers = mlComparison().main()

    def getPred(self):
        return arc.load_texture(self.file_path+"/Machine_Learning/MachineLearningScripts/pred.png")

    def getCorrectClassifiers(self):
        return self.correct_classifiers