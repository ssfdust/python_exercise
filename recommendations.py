#!/usr/bin/python

from math import sqrt
# -*- coding: utf-8 -*-

critics = {'Lisa Rose':{'Lady in the Water':2.5, 'Snakes on a Plane':3.5, 'Just My Luck':3.0, 'Superman Returns':3.5, 'You, Me and Dupree':2.5, 'The Night Listener': 3.0},
        'Gene Seymour':{'Lady in the Water':3.0, 'Snakes on a Plane':3.5, 'Just My Luck':1.5, 'Superman Returns':5.0, 'You, Me and Dupree':3.5, 'The Night Listener': 3.0},
        'Michael Phillips':{'Lady in the Water':2.5, 'Snakes on a Plane':3.0, 'Superman Returns':3.5, 'The Night Listener': 4.0},
        'Claudia Puig':{'Snakes on a Plane':3.5, 'Just My Luck':3.0, 'Superman Returns':4.0, 'The Night Listener':4.5, 'You, Me and Dupree':2.5},
        'Mick LaSalle':{'Lady in the Water':3.0, 'Snakes on a Plane':4.0, 'Just My Luck':2.0, 'Superman Returns':3.0, 'You, Me and Dupree':2.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 2.0},
        'Jack Mattthews':{'Lady in the Water':3.0, 'Snakes on a Plane':4.0, 'Superman Returns':5.0, 'You, Me and Dupree':3.5, 'The Night Listener': 3.0},
        'Toby':{ 'Snakes on a Plane':4.5, 'Superman Returns':4.0, 'You, Me and Dupree':1.0}}

def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    if len(si) == 0: return 0

    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in si])
    return 1 / (1+sqrt(sum_of_squares))

def sim_pearson(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    count = len(si)

    if count == 0: return 1

    sum1 = sum([prefs[person1][item] for item in si])
    sum2 = sum([prefs[person2][item] for item in si])

    sum1Sq = sum([pow(prefs[person1][item], 2) for item in si])
    sum2Sq = sum([pow(prefs[person2][item], 2) for item in si])

    pSum = sum([prefs[person1][item] * prefs[person2][item] for item in si])

    num = pSum - (sum1 * sum2 / count)
    den = sqrt((sum1Sq - pow(sum1, 2) / count) * (sum2Sq - pow(sum2, 2) / count))
    if den == 0: return 0

    r = num / den

    return r

def transformPrefs(prefs):
    final = dict()
    for person in prefs:
        for item in prefs[person]:
            final.setdefault(item, {})
            final[item][person] = prefs[person][item]

    return final

def topMatch(prefs, person, n = 5, similarity=sim_pearson):
    """Rank the critics.Since we could have similar senses

    :prefs: TODO
    :person: TODO
    :n: TODO
    :similarity: TODO
    :returns: TODO

    """
    scores = [(similarity(prefs, person, other), other)
            for other in prefs if other != person]
    scores.sort(reverse=True)
    return scores[0:n]
