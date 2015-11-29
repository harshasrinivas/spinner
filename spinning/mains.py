#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
import sys
import time
import os
import itertools
from termcolor import colored

frames = {
    'tetris': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
    'swords': ['-', '/', '\\'],
    'circles': ['.', 'o', 'O', '°', 'O', 'o', '.'],
    'hourglass': ['⏳', '⌛'],
    'moons': ["◐", "◓", "◑", "◒"],
    'histogram': ['▁', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃', '▁'],
    'clock': ['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚']
}


class Spinner:

    def __init__(self, sec=5, color='cyan', shape='tetris'):
        self.shape = shape
        self.color = color
        self.sec = sec

    def cursor_on(self):
        os.system('setterm -cursor on')

    def cursor_off(self):
        os.system('setterm -cursor off')

    def spin(self):
        shape = frames[self.shape]
        frame_gen = itertools.cycle(shape)
        self.cursor_off()
        for _ in xrange(self.sec*10):
            frame = colored(next(frame_gen), self.color)
            sys.stdout.write(frame)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')
        self.cursor_on()

spinner = Spinner(color='blue', shape='clock')
while True:
    spinner.spin()