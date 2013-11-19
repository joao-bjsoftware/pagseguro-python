# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from voluptuous import Schema, Object, Required, All, Length, Range


class Item(object):

    def __init__(self,
                 item_id=None,
                 description=None,
                 amount=None,
                 quantity=None,
                 shipping_cost=None,
                 weight=None):
        self.item_id = item_id
        self.description = description
        if amount:
            self.amount = float(amount)
        else:
            self.amount = None
        self.quantity = quantity
        self.shipping_cost = shipping_cost
        self.weight = weight

    def validate(self):
        item_schema(self)

    def __getattribute__(self, name):
        '''
        Customizando a leitura dos atributos amount e shipping_cost
        para sempre retornar duas casas decimais, como esperado pelo PagSeguro
        '''
        attr = object.__getattribute__(self, name)
        if name in ('amount', 'shipping_cost') and attr:
            return '%.2f' % attr
        else:
            # Default behaviour
            return attr

item_schema = Schema(Object(
    {
        Required('item_id'): All(str, Length(min=1, max=100)),
        Required('description'): All(str, Length(min=1, max=100)),
        Required('amount'): All(float, Range(min=0.01, max=9999999)),
        Required('quantity'): All(int, Range(min=1, max=999)),
        'shipping_cost': All(float, Range(min=0.01, max=9999999)),
        'weight': All(int, Range(max=30000)),
    }, cls=Item)
)
