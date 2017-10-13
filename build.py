#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# see: https://en.wikipedia.org/wiki/ISO_3166-2:IR
PROVINCE_MAP = {
    u'آذربایجان شرقی': 1,
    u'آذربایجان غربی': 2,
    u'اردبیل': 3,
    u'اصفهان': 4,
    u'ایلام': 5,
    u'بوشهر': 6,
    u'تهران': 7,
    u'چهار محال و بختیاری': 8,
    u'خوزستان': 9,
    u'زنجان': 10,
    u'سمنان': 11,
    u'سیستان و بلوچستان': 12,
    u'فارس': 13,
    u'کرمان': 14,
    u'کردستان': 15,
    u'کرمانشاه': 16,
    u'کهگیلویه و بویراحمد': 17,
    u'گیلان': 18,
    u'لرستان': 19,
    u'مازندران': 20,
    u'مرکزی': 21,
    u'هرمزگان': 22,
    u'همدان': 23,
    u'یزد': 24,
    u'قم': 25,
    u'گلستان': 26,
    u'قزوین': 27,
    u'خراسان جنوبی': 28,
    u'خراسان رضوی': 29,
    u'خراسان شمالی': 30,
    u'البرز': 31,
}

def get_province_id(name):
    """return province id by its name"""
    if name in PROVINCE_MAP:
        return PROVINCE_MAP[name]
    else:
        return 0


with open('./iran/dist/iran.json') as opened:
    iran = json.load(opened)

data = {}

for city in iran:
    pid = get_province_id(city['province_name']);
    if pid > 0:
        if not pid in data.keys():
            data[pid] = []
        data[pid].append(city['city_name'])

for pid in data.keys():
    with open('./dist/' + str(pid) + '.json', 'w', encoding='utf8') as out:
        json.dump(data[pid], out, ensure_ascii=False)
