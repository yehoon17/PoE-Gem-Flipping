# -*- coding: utf-8 -*-

from . import db


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    value = db.Column(db.Float, nullable=False)


class Gem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    corrupted = db.Column(db.Boolean, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    quality = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)
    listed = db.Column(db.Integer, nullable=False)
