#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import prompt_toolkit
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter

def main_shell(conf):
    print('conf: ', conf)
    words = ['fish', 'cat', 'gorilla', 'ssh']
    completer = WordCompleter(words, ignore_case=True)
    text = prompt('yes? ', completer=completer)
    print('yeah : "%s"' % text)
