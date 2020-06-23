"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class deals with the visualisation of an encounter. i.e. the first piece of animation when the ams 'meets' the malware."""

import arcade as arc
import time

from current_status import currentStatus

class encounter(arc.View):
    def __init__(self, data, manager):
        super().__init__()
        self.data = data
        self.manager = manager
        self.background = self.data.getMainBackground()
        self.left_encounter = self.data.getEncounter1()
        self.right_encounter = self.data.getEncounter2()

    def on_show(self):
        self.height = self.data.getHeight()
        self.width = self.data.getWidth()
        self.position = 0
        self.velocity = 5
        self.turns = 0
        

    def on_draw(self):
        if self.position == self.width:
            time.sleep(1.5)
            self.data.setStatus(currentStatus.BATTLE_ROUND_M)
            self.data.switchView(self.manager.getBattleView())

        else:
            x1_cent = 0 - self.data.getWidth() // 2 + self.position
            x2_cent = self.data.getWidth() + self.data.getWidth() // 2 - self.position

            arc.start_render()
            arc.draw_texture_rectangle(self.width // 2, self.height // 2, self.width, self.height, self.background)
            arc.draw_texture_rectangle(x1_cent, self.height // 2, self.width, self.height,self.left_encounter)
            arc.draw_texture_rectangle(x2_cent, self.height // 2, self.width, self.height,self.right_encounter)


    def on_update(self, delta_time):
        if self.turns == 1:
            self.turns += 1
            time.sleep(1.5) #pauses animation for x seconds
        else:
            self.turns += 1
        if self.position < self.width: #end pos for the box to move.
            self.position += self.velocity
        else:
            self.data.setStatus(currentStatus.ENCOUNTER)