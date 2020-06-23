"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class displays the start screen and (like a game) requires you to click in order to proceed."""

import arcade as arc
import time

from current_status import currentStatus

class start(arc.View):
    def __init__(self, data, manager):
        super().__init__()
        self.data = data
        self.manager = manager
        self.background = self.data.getStartBackground()


    def on_show(self):
        pass

    def on_draw(self):
        arc.start_render()
        arc.draw_texture_rectangle(self.data.getWidth() // 2, self.data.getHeight() // 2, self.data.getWidth(), self.data.getHeight(), self.background)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.data.switchView(self.manager.getEncounterView())
        
       