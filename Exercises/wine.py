# -*- coding: UTF-8 -*-
# File name: wine
# Created by JKChang
# 02/11/2020, 20:31
# Description:

from owlready2 import get_ontology
from owlready2 import sync_reasoner


# List all grape growing regions (in the ontology)
def get_all_regions():
    '''
    Get all grape growing regions
    :return: List of grape growing regions
    '''
    onto = get_ontology('file://./wine.owl').load()
    with onto:
        sync_reasoner()
        return [x.name for x in onto.region.instances()]


# List all varietals (in the ontology)
def get_all_varietals():
    '''
    Get all grape varietals, include also_called
    :return: List of grape varietals
    '''
    onto = get_ontology('file://./wine.owl').load()
    with onto:
        sync_reasoner()
        subs = onto.varietal.descendants()
        subs.remove(onto.varietal)
        res = [x.name for x in subs]
        for c in subs:
            if len(c.also_called) > 0:
                res += c.also_called
        return res


# List all types (classes) of wine (in the ontology)
def get_all_types():
    '''
    List all types of wine
    :return: List of wine types
    '''
    onto = get_ontology('file://./wine.owl').load()
    with onto:
        sync_reasoner()
        subs = onto.color.descendants()
        subs.remove(onto.color)
        return [x.name for x in subs]


# Query for wine types and individual wines by: colour, varietal, region
def query(color=None, varietal=None, region=None):
    '''
    :param color: wine color
    :param varietal: grape varietal
    :param region: region
    :return: types and individuals by given colour, varietal and region
    '''
    onto = get_ontology('file://./wine.owl').load()
    with onto:
        sync_reasoner()
        wines = onto.wine.descendants()
        wines.remove(onto.wine)
        res = list(wines.copy())
        for wine in wines:
            if color:
                wine_c = [x.name.lower() for x in wine.has_color]
                if color.lower() not in wine_c:
                    res.remove(wine)
                    continue
            if varietal:
                wine_v = [x.name.lower() for x in wine.made_from]
                if varietal.lower() not in wine_v:
                    res.remove(wine)
                    continue
            if region:
                wine_r = [x.name.lower() for x in wine.grown_in]
                if region.lower() not in wine_r:
                    res.remove(wine)
                    continue

        for i in res:
            try:
                if len(i.instances()) > 0:
                    inst = i.instances()
                    res += inst
            except:
                pass
        return list(set([x.name for x in res]))
