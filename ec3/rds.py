#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

def make_db_arn(account_number, aws_region, db_instance_id):
    return 'arn:aws:%s:%s:%s' % (
        db_instance_id, aws_region, account_number
    )



