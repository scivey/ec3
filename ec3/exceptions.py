#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import botocore.exceptions

class EC3Exception(Exception):
    pass


class InvalidInput(EC3Exception):
    pass


class UnsupportedMethod(EC3Exception):
    pass


class NoInstancesFound(EC3Exception, LookupError):
    pass


class CredentialError(EC3Exception, botocore.exceptions.NoCredentialsError, botocore.exceptions.ClientError):
    def __init__(self, err):
        self.err = err
