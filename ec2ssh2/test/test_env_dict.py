#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import unittest
import mock
from ec2ssh2.env_dict import EnvDict


class TestEnvDict(unittest.TestCase):
    def setUp(self):
        self.environ = {}

        def getter(key):
            return self.environ.get(key, None)
        get_env = mock.patch(
            'ec2ssh2.env_dict.EnvDict._get_env',
            side_effect=getter
        )
        get_env.start()
        self.addCleanup(get_env.stop)

    def test_happy(self):
        self.environ.update({
            'GOOD_KEY': 'yes'
        })
        env = EnvDict(BAD_KEY='nope')
        self.assertEqual('yes', env.GOOD_KEY)
        self.assertEqual('nope', env.BAD_KEY)

    def test_missing_getitem(self):
        self.environ.update({
            'GOOD_KEY': 'yes'
        })
        env = EnvDict(OTHER_KEY='other')
        with self.assertRaises(KeyError):
            unused = env['MISSING_KEY']
            self.assertTrue(unused)  # not reached

    def test_missing_getattr(self):
        self.environ.update({
            'GOOD_KEY': 'yes'
        })
        env = EnvDict(OTHER_KEY='other')
        with self.assertRaises(AttributeError):
            unused = env.MISSING_KEY
            self.assertTrue(unused)  # not reached
