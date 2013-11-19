# -*- coding: utf-8 -*-
'''
Created on Nov 19, 2013

@author: Ricardo Silva
'''
from pagseguro import Payment
from unittest.case import TestCase


class PaymentTestCase(TestCase):

    def setUp(self):
        email = 'nada@nada.com'
        token = '12345678901234567890123456789012'
        self.payment = Payment(email=email, token=token)


    def test__payment(self):
        print self.payment
        