# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from pagseguro import local_settings
from pagseguro.tests.payment import PaymentTest
import doctest
import pagseguro
import unittest


def suite():
    suite = unittest.TestSuite()
#    suite.addTest(doctest.DocTestSuite(pagseguro))
    suite.addTest(
        unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
    )
    return suite
