# -*- coding: utf-8 -*-

from . import db


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    value = db.Column(db.Float, nullable=False)


class Gem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    corrupted = db.Column(db.Boolean, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    quality = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)
    listed = db.Column(db.Integer, nullable=False)


class GemInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    has_vaal = db.Column(db.Boolean, nullable=False)
    max_level = db.Column(db.Integer, nullable=False)
    is_skill = db.Column(db.Boolean, nullable=False)
