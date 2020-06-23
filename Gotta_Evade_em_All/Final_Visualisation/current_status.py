"""Gotta Evade 'em All - Emily Chaffey - Full Unit 1920 IY4500 """

""" This is a enum class used to determine which state the visualisation system is in at the current moment."""

from enum import Enum

class currentStatus(Enum):
    BATTLE_ROUND_M = 2,
    BATTLE_ROUND_AMS = 3
    FINISHED = 4,
    START = 1
    ENCOUNTER = 5
    VICTORY_M = 6
    VICTORY_AMS = 7
    REPORT = 8
    ML = 9


