# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from pagseguro.validators import PhoneArea, PhoneNumber
from voluptuous import Schema, Object, All, Length


class Phone(object):

    def __init__(self, area_code=None, number=None):
        self.area_code = area_code
        self.number = number

    def validate(self):
        phone_schema(self)


phone_schema = Schema(Object(
    {
        'area_code': All(PhoneArea(), Length(min=2, max=2)),
        'number': All(PhoneNumber(), Length(min=7, max=9)),
    }, cls=Phone)
)
