# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''

from pagseguro.api.v2.objects import document, checkout, item, sender, \
    payment_request, shipping_address, shipping
from pagseguro.tests.payment import PaymentTestCase
from pagseguro.tests.payment_request import PaymentRequestTestCase
import doctest
import pagseguro
import unittest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(doctest.DocTestSuite(pagseguro))
    suite.addTest(doctest.DocTestSuite(checkout))
    suite.addTest(doctest.DocTestSuite(document))
    suite.addTest(doctest.DocTestSuite(item))
    suite.addTest(doctest.DocTestSuite(payment_request))
    suite.addTest(doctest.DocTestSuite(sender))
    suite.addTest(doctest.DocTestSuite(shipping_address))
    suite.addTest(doctest.DocTestSuite(shipping))
    suite.addTest(
        unittest.TestLoader().loadTestsFromTestCase(PaymentRequestTestCase)
    )
    suite.addTest(
        unittest.TestLoader().loadTestsFromTestCase(PaymentTestCase)
    )
    return suite
