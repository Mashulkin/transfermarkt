# -*- coding: utf-8 -*-
"""
Real player position formatting
"""


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '25.02.2023'


def formatPosition(positionId):
    position = ''
    position = 'GK' if positionId == 1 else position
    position = 'D' if positionId == 2 else position
    position = 'M' if positionId == 3 else position
    position = 'F' if positionId == 4 else position

    return position
