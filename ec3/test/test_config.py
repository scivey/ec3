#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import unittest
from ec3.config import parse_tag_filters
from ec3 import exceptions


class TestConfig(unittest.TestCase):
    def test_parse_tag_filters_happy_1(self):
        tags = parse_tag_filters("foo=bar")
        self.assertEqual({
            'foo': 'bar'
        }, tags)

    def test_parse_tag_filters_happy_2(self):
        tags = parse_tag_filters("foo=bar,fish=pescado")
        self.assertEqual({
            'foo': 'bar',
            'fish': 'pescado'
        }, tags)

    def test_parse_tag_filters_sad_panda_1(self):
        with self.assertRaises(exceptions.InvalidInput):
            parse_tag_filters("foobar")

    def test_parse_tag_filters_sad_panda_2(self):
        with self.assertRaises(exceptions.InvalidInput):
            parse_tag_filters("foo=bar,baz")

    def test_parse_tag_filters_sad_panda_3(self):
        with self.assertRaises(exceptions.InvalidInput):
            parse_tag_filters("foo=,baz=yes")
