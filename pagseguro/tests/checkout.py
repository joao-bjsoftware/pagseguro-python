# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from pagseguro.api.v2.objects.checkout import Checkout
from pagseguro.tests.item import ItemTestCase
from unittest.case import TestCase


class CheckoutTestCase(TestCase):

    @staticmethod
    def build_checkout():
        checkout = Checkout()
        item = ItemTestCase.build_item()
        checkout.items = [item, ]
        return checkout
