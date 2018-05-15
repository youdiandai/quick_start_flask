#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/5/15'
"""
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


# 用户表
class User(UserMixin, db.Model):
    """User table"""
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<User> id="{}" username="{}"'.format(self.id, self.username)
