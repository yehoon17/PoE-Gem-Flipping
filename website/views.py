# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request
from . import db
from website.utils import *

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/flipping/")
def flipping_method():
    flipping_method = request.args.get("flipping-method")

    ### query gems of flipping-method from database ###
    gems = None
    ###################################################

    return render_template("home.html", gems=gems)
