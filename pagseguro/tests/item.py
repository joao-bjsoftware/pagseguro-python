# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from pagseguro.api.v2.objects.item import Item
from unittest.case import TestCase


class ItemTestCase(TestCase):

    @staticmethod
    def build_item():
        item = Item()
        item.item_id = 'id-do-produto'
        item.description = 'Descricao do produto'
        item.quantity = 1
        item.amount = 15.0
        return item

    def setUp(self):
        self.item = ItemTestCase.build_item()
