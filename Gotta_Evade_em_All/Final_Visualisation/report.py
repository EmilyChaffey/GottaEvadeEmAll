"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This class displays the report generated about the battle and requires the user to click in order to switch views."""

import arcade as arc
import time

from current_status import currentStatus

class report(arc.View):
    def __init__(self, data, manager):
        super().__init__()
        self.data = data
        self.manager = manager
        self.background = self.data.getMainBackground()
        self.width = self.data.getWidth()
        self.height = self.data.getHeight()
        self.msg = self.data.getMsg()

    def on_show(self):
        pass

    def on_draw(self):
        arc.start_render()
        
        arc.draw_texture_rectangle(self.width // 2, self.height // 2, self.width, self.height, self.background)
        arc.draw_text("AMS's Message to User:\n\n\n"+self.msg.title() , self.width // 2, self.height // 2, font_size=35, color=arc.color.WHITE, align="center", anchor_x="center", anchor_y="center")
        arc.draw_text("<< Next page >>", self.width // 2, self.height * 0.05, font_size=24, color=arc.color.WHITE, align="center", anchor_x="center", anchor_y="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.data.setStatus(currentStatus.ML)
        self.data.switchView(self.manager.getMLView())
        
       