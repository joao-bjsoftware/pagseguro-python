# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''


class PagSeguroException(Exception):
    ''' Exception base para operações com o PagSeguro '''

    def __str__(self):
        return self.message.encode('ascii', 'replace')


class PagSeguroApiException(PagSeguroException):
    ''' Erros de chamada à API do PagSeguro em geral '''


class PagSeguroPaymentException(PagSeguroApiException):
    ''' Erros durante o processo de pagamento '''


class PagSeguroNotificationException(PagSeguroApiException):
    ''' Erros durante o processo de notificacoes de pagamento '''
