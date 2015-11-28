#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from future.standard_library import install_aliases
install_aliases()
import sys
import time
import blessings
import os

term = blessings.Terminal()

shapes = {
    'tetris': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
    'swords': ['-', '/', '\\'],
    'circles': ['.', 'o', 'O', '°', 'O', 'o', '.'],
    'hourglass': ['⏳', '⌛'],
    'moons': ["◐", "◓", "◑", "◒"],
    'progressbar': ['█▒▒▒▒', '███▒▒', '█████'],
    'histogram': ['▁', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃', '▁'],
    'clock': ['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚']
}


class spin:

    def __init__(self, sec=5, color='cyan', form='tetris'):
        self.display = {
            'cyan': term.cyan,
            'red': term.red,
            'magenta': term.magenta,
            'green': term.green,
            'yellow': term.yellow,
            'white': term.white
        }

        def spin():
            while True:
                for x in shapes[form]:
                    yield self.display.get(color, term.cyan)(x)

        spinner = spin()
        os.system('setterm -cursor off')
        for _ in range(sec*10):
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')
        os.system('setterm -cursor on')
