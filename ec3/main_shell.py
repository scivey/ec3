#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import prompt_toolkit
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from .boto_cache import BotoCache

def main_shell(conf):
    print('conf: ', conf)
    boto_cache = BotoCache.get_or_create()
    keys = [tag.key for tag in boto_cache.tags]
    words = ['fish', 'cat', 'gorilla', 'ssh'] + keys
    completer = WordCompleter(words, ignore_case=True)
    text = prompt('yes? ', completer=completer)
    print('yeah : "%s"' % text)
