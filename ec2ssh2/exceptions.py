#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals


class EC2SSH2Exception(Exception):
    pass


class InvalidInput(EC2SSH2Exception):
    pass

class UnsupportedMethod(EC2SSH2Exception):
    pass


class NoInstancesFound(EC2SSH2Exception, LookupError):
    pass
