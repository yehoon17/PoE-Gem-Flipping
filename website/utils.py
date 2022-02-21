# -*- coding: utf-8 -*-

import requests
from . import db
from website.models import Currency, Gem

LEAGUE_NAME = "Archnemesis"
CURRENCY_URL = f"https://poe.ninja/api/data/currencyoverview?league={LEAGUE_NAME}&type=Currency"
SKILL_GEM_URL = f"https://poe.ninja/api/data/itemoverview?league={LEAGUE_NAME}&type=SkillGem"


def update_currency():
    response = requests.get(CURRENCY_URL)
    content = response.json()["lines"]
    currencies = ["Vaal Orb", "Prime Regrading Lens",
                  "Secondary Regrading Lens", ]

    for currency in filter(lambda x: x["currencyTypeName"] in currencies, content):
        name = currency["currencyTypeName"]
        value = currency["chaosEquivalent"]

        ### update database ###
        if x := Currency.query.filter_by(name=name).first():
            # update
            x.value = value
        else:
            # create
            db.session.add(Currency(name=name, value=value))

    db.session.commit()


def update_gem():
    response = requests.get(SKILL_GEM_URL)
    content = response.json()["lines"]
    keys = ["name", "corrupted", "gemLevel",
            "gemQuality", "chaosValue", "listingCount"]
    columns = {"name": "name", "corrupted": "corrupted", "gemLevel": "level",
               "gemQuality": "quality", "chaosValue": "value", "listingCount": "listed"}

    gems = [{columns[key]: gem[key] for key in keys} for gem in content]
    for gem in gems:
        pass

    db.session.commit()
