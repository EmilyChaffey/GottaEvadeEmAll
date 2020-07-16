"""Gotta Evade 'em All - Emily Chaffey"""

""" This class displays the winner of the battle and requires the user to click in order to switch views."""

import arcade as arc
import time

from current_status import currentStatus

class winner(arc.View):
    def __init__(self, data, manager):
        super().__init__()
        self.data = data
        self.manager = manager
        self.background = self.data.getWonBackground()

    def on_show(self):
        pass

    def on_draw(self):
        arc.start_render()
        arc.draw_texture_rectangle(self.data.getWidth() // 2, self.data.getHeight() // 2, self.data.getWidth(), self.data.getHeight(), self.background)
        arc.draw_text("<< Click to view report >>", self.data.getWidth() // 2, self.data.getHeight() * 0.05, font_size=24, color=arc.color.NAVY_BLUE, align="center", anchor_x="center", anchor_y="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.data.setStatus(currentStatus.REPORT)
        self.data.switchView(self.manager.getReportView())
        
       