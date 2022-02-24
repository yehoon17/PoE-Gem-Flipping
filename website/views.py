# -*- coding: utf-8 -*-

from locale import currency
from flask import Blueprint, render_template, request
from . import db
from website.utils import *
from website.models import Currency, GemInfo

views = Blueprint("views", __name__)


@views.route("/")
def home():
    update_currency()
    currency = Currency.query.all()
    return render_template("home.html", currency=currency)


@views.route("/flipping/")
def flipping_method():
    flipping_method = request.args.get("flipping-method")

    # gems = gems_by(flipping_method)

    ####### testing ######
    update_gem()
    gems = Gem.query.all()
    ######################

    return render_template("home.html", gems=gems)


@views.route("/gem-info")
def gem_info():
    info = GemInfo.query.all()
    return render_template("info.html", info=info)
