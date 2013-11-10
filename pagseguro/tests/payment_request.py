# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from pagseguro.api.v2.objects.payment_request import PaymentRequest
from pagseguro.tests.checkout import CheckoutTestCase
from unittest.case import TestCase


class PaymentRequestTestCase(TestCase):

    def setUp(self):
        payment_request = PaymentRequest()
        payment_request.email = 'vendedor@nada.com'
        payment_request.token = '12345678901234567890123456789012'

        checkout = CheckoutTestCase.build_checkout()
        payment_request.checkout = checkout
        self.payment_request = payment_request

    def test__payment(self):
        self.payment_request.validate()
