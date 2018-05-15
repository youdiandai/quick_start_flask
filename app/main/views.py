#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/5/15'
"""
from . import main
from flask import send_from_directory


@main.route('/')
def index():
    return 'welcome'
