# -*- coding: utf-8 -*-
'''
Created on Nov 7, 2013

@author: ricardo
'''
from pagseguro.api.v2.payment import Payment as PaymentV2


class Payment(object):
    '''
    Utilize esta classe para instanciar o objeto que fara a conexão
    com o PagSeguro
    
    :param: email: O email do comprador no PagSeguro
    :param: token,
    '''

    @staticmethod
    def _payment_factory(email, token, version):
        if version == 2:
            return PaymentV2(email, token)
        else:
            raise NotImplementedError()

    def __init__(self, email, token, version=2):
        self._payment = self._payment_factory(email, token, version)

    def add_item(self,
                 item_id,
                 description,
                 amount,
                 quantity,
                 shipping_cost=None,
                 weight=None):
        '''
        Método proxy para a classe que implementa o método add_item na
        versão da API escolhida
        '''
        return self._payment.add_item(item_id,
                                      description,
                                      amount,
                                      quantity,
                                      shipping_cost,
                                      weight)

    def request(self):
        ''' Método proxy para a classe que implementa o método request na
        versão da API escolhida

        :returns: PaymentResponse object
        '''
        return self._payment.request()

    @property
    def response(self):
        ''' Objeto com resposta à requisição '''
        return self._payment.response

    @property
    def payment_url(self):
        ''' '''
        return self._payment.payment_url()
