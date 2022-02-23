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


def get_gems():
    response = requests.get(SKILL_GEM_URL)
    content = response.json()["lines"]
    keys = ["name", "corrupted", "gemLevel",
            "gemQuality", "chaosValue", "listingCount"]
    columns = {"name": "name", "corrupted": "corrupted", "gemLevel": "level",
               "gemQuality": "quality", "chaosValue": "value", "listingCount": "listed"}

    gems = []
    for gem in content:
        gem.setdefault("gemQuality", 0)
        gem.setdefault("corrupted", False)
        gems.append({columns[key]: gem[key] for key in keys})

    return gems


def disassemble(name):
    # get alternative
    alternative_opt = ("Anomalous", "Divergent", "Phantasmal")
    if name.startswith(alternative_opt):
        alternative = name.split()[0]
        name = " ".join(name.split()[1:])
    else:
        alternative = "Normal"

    # get vaal
    if name.startswith("Vaal"):
        vaal = True
        name = " ".join(name.split()[1:])
    else:
        vaal = False

    return (alternative, vaal, name)


def update_gem():
    gems = get_gems()
    for gem in gems:
        alternative, vaal, name = disassemble(gem["name"])
        gem["name"] = name
        gem["vaal"] = vaal
        gem["alternative"] = alternative

        db.session.add(Gem(**gem))

    db.session.commit()


def gems_by(flipping_method):
    pass
