#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

from collections import namedtuple
import argparse

from ec2ssh2.env_dict import EnvDict
from ec2ssh2.util import ConstantDict
from ec2ssh2 import exceptions

DEFAULTS = ConstantDict(
    EC2SSH2_VPC_SCOPE=None,
    EC2SSH2_TAG_FILTERS='',
    EC2SSH2_KEY_FILE_PATH=None,
    EC2SSH2_REMOTE_USER='ubuntu'
)


def parse_tag_filters(tag_str):
    tags = {}
    if tag_str:
        if ',' in tag_str:
            pieces = tag_str.split(',')
        else:
            pieces = [tag_str]

        for piece in pieces:
            failed_to_split = False
            try:
                key, val = piece.split('=')
            except ValueError:
                failed_to_split = True

            if failed_to_split or (not val):
                raise exceptions.InvalidInput(
                    tag_str,
                    "EC2SSH2_TAG_FILTERS should be formatted as: 'key1=val1,key2=val2"
                )
            key = key.strip()
            val = val.strip()
            tags[key] = val
    return tags


ParsedArgs = namedtuple('ParsedArgs', [
    'tags', 'vpc_scope', 'escape_env', 'remote_user', 'key_file_path'
])


def make_parser():
    parser = argparse.ArgumentParser(description='SSH into ec2 instances.')
    parser.add_argument(
        'tags', action='append', nargs='*',
        help='additional tag filters, formatted as "key1=val1 key2=val2"')

    parser.add_argument('--vpc', dest='vpc_scope',
                        default='', help='vpc id')

    parser.add_argument('--escape-env', metavar='escape_env', type=bool,
                        default=False,
                        help='disable filters due to environment variables')

    parser.add_argument('-i', dest='key_file_path', type=str,
                        default='',
                        help='specify the path of the SSH key to use.')

    parser.add_argument('-u', dest='remote_user', type=str,
                        default='',
                        help='specify user to connect as.')
    return parser


def get_args():
    parser = make_parser()
    args = parser.parse_args()
    tags = {}
    for key_val in args.tags[0]:
        tags.update(parse_tag_filters(key_val))
    return ParsedArgs(
        vpc_scope=args.vpc_scope,
        escape_env=args.escape_env,
        remote_user=args.remote_user,
        tags=tags,
        key_file_path=args.key_file_path
    )


class Config(object):
    def __init__(self, env, tag_filters, args):
        self.env = env
        self.args = args
        self.tag_filters = tag_filters

    @classmethod
    def create(cls):
        env = EnvDict(DEFAULTS)
        args = get_args()
        tag_filters = {}
        if not args.escape_env:
            # doing this lazily would make InvalidInput
            # exceptions more confusing
            tag_filters.update(parse_tag_filters(
                env.EC2SSH2_TAG_FILTERS
            ))

        # command-line args have precedence
        tag_filters.update(args.tags)
        tag_filters = ConstantDict(**tag_filters)
        return cls(
            env=env,
            tag_filters=tag_filters,
            args=args
        )

    @property
    def vpc_scope(self):
        if self.args.vpc_scope:
            return self.args.vpc_scope
        elif not self.args.escape_env:
            return self.env.EC2SSH2_VPC_SCOPE
        return ''

    @property
    def remote_user(self):
        if self.args.remote_user:
            return self.args.remote_user
        elif not self.args.escape_env:
            return self.env.EC2SSH2_REMOTE_USER
        return ''

    @property
    def key_file_path(self):
        if self.args.key_file_path:
            return self.args.key_file_path
        elif not self.args.escape_env:
            return self.env.EC2SSH2_KEY_FILE_PATH
        return ''

    def __repr__(self):
        result = {
            attr: getattr(self, attr) for attr in ('vpc_scope', 'remote_user', 'key_file_path')
        }
        result['tag_filters'] = {k: v for k, v in self.tag_filters.iteritems()}
        return repr(result)
