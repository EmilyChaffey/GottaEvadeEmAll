"""Gotta Evade 'em All - Emily Chaffey"""

""" This class displays the machine learning results, showing the predicted labels for each classifier and then the confusion matrix values."""

import arcade as arc
import time

from current_status import currentStatus

class ml(arc.View):
    def __init__(self, data, manager):
        super().__init__()
        self.data = data
        self.manager = manager
        self.data.genML()
        self.pred_img = self.data.getPred()
        self.background = self.data.getMainBackground()
        self.correct_classifiers = self.data.getCorrectClassifiers()


    def on_show(self):
        pass

    def on_draw(self):
        arc.start_render()
        width = self.data.getWidth()
        height = self.data.getHeight()
        arc.draw_texture_rectangle(width // 2, height // 2, width, height, self.background)
        arc.draw_text("Machine Learning Predicted Label Results", width // 2, height - height * 0.1, font_size=35, color=arc.color.WHITE, align="center", anchor_x="center", anchor_y="center")
        arc.draw_texture_rectangle(width // 2, height // 2, 2 * width // 3, 2 * height // 3, self.pred_img)
        arc.draw_text("Correct Classifiers: "+self.correct_classifiers, width // 2, height * 0.1, font_size=24, color=arc.color.WHITE, align="center", anchor_x="center", anchor_y="center")
        arc.draw_text("<< Click to close >>", width // 2, height * 0.05, font_size=24, color=arc.color.WHITE, align="center", anchor_x="center", anchor_y="center")
        

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        arc.close_window()
        
       