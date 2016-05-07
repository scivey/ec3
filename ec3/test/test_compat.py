#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import unittest
from ec3.util import is_iterator
from ec3 import compat


class TestCompat(unittest.TestCase):
    def test_iteritems(self):
        data = {'x': 5, 'y': 7}
        result = compat.iteritems(data)
        self.assertTrue(is_iterator(result))
        result = set(result)
        self.assertFalse(is_iterator(result))
        self.assertEqual(set([
            ('x', 5),
            ('y', 7)
        ]), result)

    def test_iterkeys(self):
        data = {'x': 5, 'y': 7}
        result = compat.iterkeys(data)
        self.assertTrue(is_iterator(result))
        result = set(result)
        self.assertFalse(is_iterator(result))
        self.assertEqual(set(['x', 'y']), result)

    def test_list_keys(self):
        data = {'x': 5, 'y': 7}
        result = compat.list_keys(data)
        self.assertTrue(isinstance(result, list))
        self.assertEqual(
            set(['x', 'y']),
            set(result)
        )
