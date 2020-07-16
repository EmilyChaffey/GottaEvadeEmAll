"""Gotta Evade 'em All - Emily Chaffey"""

""" This class handles the visualisation of the battle scenes."""

import arcade as arc
import time

from current_status import currentStatus

class battle(arc.View):
    def __init__(self, data, manager):
        super().__init__()
        self.data = data
        self.manager = manager
        self.background = self.data.getMainBackground()
        if self.data.getStatus() == currentStatus.BATTLE_ROUND_M:
            self.battle1, self.battle2, self.battle3, self.battle_imgs, self.moves = self.data.getBattle()
        else:
            self.battle_imgs, self.moves = self.data.getBattle()
        self.no_of_rounds = self.data.getNoOfRounds()
        self.currentRound = self.data.getCurrentRound()
        self.count = 0

    def on_show(self):
        self.height = self.data.getHeight()
        self.width = self.data.getWidth()
        self.position = 0
        self.velocity = 5
        self.turns = 0

    def on_draw(self):
        if self.turns > 20 and self.data.getStatus() == currentStatus.BATTLE_ROUND_M: # if current state is m battle
            time.sleep(1.5)
            self.data.setStatus(currentStatus.BATTLE_ROUND_AMS)
            self.data.switchView(self.manager.getBattleView())
        elif self.turns > 25 and not self.data.getStatus() == currentStatus.BATTLE_ROUND_M: #if current state is ams battle
            time.sleep(1.5)
            if self.currentRound == self.no_of_rounds:
                self.data.setStatus(currentStatus.FINISHED)
                self.data.switchView(self.manager.getWinnerView())
            else:
                time.sleep(1.5)
                self.data.setCurrentRound(self.currentRound + 1)
                self.data.setStatus(currentStatus.BATTLE_ROUND_M)
                self.data.switchView(self.manager.getBattleView())            

        else:# main battle animation occurs here, e.g. M perfroms X
            arc.start_render()
            arc.draw_texture_rectangle(self.data.getWidth() // 2, self.data.getHeight() // 2, self.data.getWidth(), self.data.getHeight(), self.background)
            if self.data.getStatus() == currentStatus.BATTLE_ROUND_M: #if the current round is a malware battle           
                
                if self.turns == 1:
                    arc.draw_texture_rectangle(self.data.getWidth() // 2, self.data.getHeight() // 2, self.data.getWidth(), self.data.getHeight(), self.battle1)
                elif self.turns < 5:
                    arc.draw_texture_rectangle(self.data.getWidth() // 2, self.data.getHeight() // 2, self.data.getWidth(), self.data.getHeight(), self.battle2)
                    time.sleep(.1)
                elif self.turns < 10:
                    arc.draw_texture_rectangle(self.data.getWidth() // 2, self.data.getHeight() // 2, self.data.getWidth(), self.data.getHeight(), self.battle3)
                    arc.draw_text("The Malware performed \n\n"+self.moves[self.currentRound-1][0], self.data.getWidth() // 15, self.data.getHeight() // 8,color=arc.color.BLACK,font_name=('terminal','calibri'), font_size=40, align='left')
                    time.sleep(.2)
                else:
                    arc.draw_texture_rectangle(self.data.getWidth() // 2, self.data.getHeight() // 2, self.data.getWidth(), self.data.getHeight(), self.battle3)
                    arc.draw_texture_rectangle(self.data.getWidth() * 0.5, self.data.getHeight() * 0.6, self.data.getWidth()//6, self.data.getHeight()//6, self.battle_imgs[self.currentRound-1])
                    arc.draw_text("The Malware performed \n\n"+self.moves[self.currentRound-1][0], self.data.getWidth() // 15, self.data.getHeight() // 8,color=arc.color.BLACK,font_name=('terminal','calibri'), font_size=40, align='left')
                    time.sleep(.1)
            else: #the current round is an ams battle
                if self.turns == 1:
                    arc.draw_texture_rectangle(self.data.getWidth() // 2, self.data.getHeight() // 2, self.data.getWidth(), self.data.getHeight(), self.battle_imgs[self.count])
                elif self.turns < 5:
                    arc.draw_texture_rectangle(self.data.getWidth() // 2, self.data.getHeight() // 2, self.data.getWidth(), self.data.getHeight(), self.battle_imgs[self.count])
                    time.sleep(.1)
                elif self.turns < 10:
                    arc.draw_texture_rectangle(self.data.getWidth() // 2, self.data.getHeight() // 2, self.data.getWidth(), self.data.getHeight(), self.battle_imgs[self.count])
                    time.sleep(.2)
                elif self.turns < 15:
                    arc.draw_texture_rectangle(self.data.getWidth() // 2, self.data.getHeight() // 2, self.data.getWidth(), self.data.getHeight(), self.battle_imgs[self.count])
                    time.sleep(.2)
                elif self.turns < 20:
                    arc.draw_texture_rectangle(self.data.getWidth() // 2, self.data.getHeight() // 2, self.data.getWidth(), self.data.getHeight(), self.battle_imgs[self.count])
                    time.sleep(.2)
                elif self.turns < 25:
                    arc.draw_texture_rectangle(self.data.getWidth() // 2, self.data.getHeight() // 2, self.data.getWidth(), self.data.getHeight(), self.battle_imgs[self.count])
                    time.sleep(.2)
                else:
                    arc.draw_texture_rectangle(self.data.getWidth() // 2, self.data.getHeight() // 2, self.data.getWidth(), self.data.getHeight(), self.battle_imgs[self.count])
                    arc.draw_text("The AMS detected \n\n"+self.moves[self.currentRound-1][0], self.data.getWidth() // 15, self.data.getHeight() // 8,color=arc.color.BLACK,font_name=('terminal','calibri'), font_size=40, align='left')
                    time.sleep(.05)


    def on_update(self, delta_time):
        if self.turns == 1:
            self.turns += 1
            time.sleep(1) #pauses animation for x seconds
        else:
            self.turns += 1
        if self.turns == 2:
            self.count += 1
        if self.turns == 5:
            self.count += 1
        if self.turns == 10:
            self.count += 1
        if self.turns == 15 and not self.data.getStatus() == currentStatus.BATTLE_ROUND_M:
            self.count + 1
        if self.turns == 20 and not self.data.getStatus() == currentStatus.BATTLE_ROUND_M:
            self.count += 1
        if self.turns == 25 and not self.data.getStatus() == currentStatus.BATTLE_ROUND_M:
            self.count += 1
       