# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
import requests
import pandas as pd

CURRENCY_URL = "https://poe.ninja/api/data/currencyoverview?league=Archnemesis&type=Currency"
SKILL_GEM_URL = "https://poe.ninja/api/data/itemoverview?league=Archnemesis&type=SkillGem"

views = Blueprint("views", __name__)


def get_currency():
    response = requests.get(CURRENCY_URL)
    content = response.json()["lines"]
    currencies = ["Vaal Orb", "Prime Regrading Lens",
                  "Secondary Regrading Lens"]
    filtered = filter(lambda x: x["currencyTypeName"] in currencies, content)
    return list(map(lambda x: (x["currencyTypeName"], x["chaosEquivalent"]), filtered))


def get_gem_sample():
    pass


@views.route("/")
def home():
    costs = get_currency()
    return render_template("home.html", costs=costs)
