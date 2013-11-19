# -*- coding: utf-8 -*-
'''
Created on Nov 19, 2013

@author: Ricardo Silva
'''
from pagseguro.validators import Email, PhoneArea, PhoneNumber, BrState
from voluptuous import Schema, Required, All, Length, Range, Optional, Match, \
    Any

item_schema = Schema({
    Required('item_id'): All(str, Length(min=1, max=100)),
    Required('description'): All(str, Length(min=1, max=100)),
    Required('amount'): All(float, Range(min=0.01, max=9999999)),
    Required('quantity'): All(int, Range(min=1, max=999)),
    'shipping_cost': All(float, Range(min=0.01, max=9999999)),
    Optional('weight'): All(int, Range(max=30000)),
})

client_schema = Schema({
    'name': str,
    'email': All(Email(), Length(max=60)),
    'phone_area_code': All(PhoneArea(), Length(min=2, max=2)),
    'phone_number': All(PhoneNumber(), Length(min=7, max=9)),
    'cpf': All(Match('[\d]{11}', msg='CPF invalido. Informe um numero com 11 digitos'), Length(min=11, max=11)), # TODO: Validar CPF
    'born_date': str #TODO: Validar data
})

shipping_schema = Schema({
    'type': Any(1, 2, 3),
    'cost': All(float, Range(min=0.01, max=9999999)),
    'street': All(str, Length(max=80)),
    'number': All(str, Length(max=20)),
    'complement': All(str, Length(max=40)),
    'district': All(str, Length(max=60)),
    'postal_code': All(Match('[\d]{8,8}', msg=u'PostalCode invalido. Informe um numero com oito digitos'), 
                         Length(min=8, max=8)),
    'city': All(str, Length(min=2, max=60)),
    'state': All(BrState(), Length(min=2, max=2)),
    'country': 'BRA',
})
