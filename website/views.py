# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
import requests

CURRENCY_URL = "https://poe.ninja/api/data/currencyoverview?league=Archnemesis&type=Currency"

views = Blueprint("views", __name__)


@views.route("/")
def home():
    response = requests.get(CURRENCY_URL)
    content = response.json()["lines"]
    currencies = ["Vaal Orb", "Prime Regrading Lens", "Secondary Regrading Lens"]
    filtered = filter(lambda x: x["currencyTypeName"] in currencies, content)
    costs = list(map(lambda x: (x["currencyTypeName"], x["chaosEquivalent"]), filtered))
    
    return render_template("home.html", costs=costs)
