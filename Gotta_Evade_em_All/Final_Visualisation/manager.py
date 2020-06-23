"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class manages all of the possible views in the visualisation """

import arcade as arc
import time


from current_status import currentStatus

class Manager ():
    def __init__ (self, data):
        self.data = data

    def getBattleView(self):
        from battle import battle
        battle_view = battle(self.data, self)
        return battle_view

    def getEncounterView(self):
        from encounter import encounter
        encounter_view = encounter(self.data, self)
        return encounter_view

    def getWinnerView(self):
        from winner import winner
        winner_view = winner(self.data, self)
        return winner_view
    
    def getMLView(self):
        from ml import ml
        ml_view = ml(self.data,self)
        return ml_view
    
    def getReportView(self):
        from report import report
        report_view = report(self.data, self)
        return report_view