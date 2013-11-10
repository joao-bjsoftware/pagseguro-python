# -*- coding: utf-8 -*-
'''
Created on Nov 7, 2013

@author: Ricardo Silva
'''
from abc import ABCMeta, abstractmethod


class BasePaymentResponse:
    '''
    Classe abstrata que define a interface para o objeto que trata a resposta
    à requisição enviada ao PagSeguro. As classes que a implementarem devem
    processar a resposta e gerar as exceções adequadas em caso de erro ou
    popular um dicionario com os dados em caso de sucesso
    '''

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, payment_response):
        ''' O construtor da classe receberá o texto retornado pelo metodo'''
        raise NotImplementedError()

    @abstractmethod
    def response_data(self):
        ''' Retorna um dicionario com os dados extraidos da resposta ao pedido de pagamento '''
        raise NotImplementedError()


class BasePaymentRequest:
    '''
    Classe abstrata que define a interface para o objeto que faz a
    requisição ao PagSeguro.

    Esta definição precisa ser ampla o bastante para ser utilizada por
    todas as versões já existentes ou que venham a surgir da API.
    '''

    __metaclass__ = ABCMeta

    @abstractmethod
    def api_version(self):
        ''' A versão da API que esta classe implementa '''
        raise NotImplementedError()

    @abstractmethod
    def add_item(self, item_id, description, amount, quantity, shipping_cost=None, weight=None):
        raise NotImplementedError()

    @abstractmethod
    def request(self):
        '''
        A implementação deste método deve:
        1 - Fazer a validação dos dados do pedido
        2 - Construir a requisição HTTP ao servidor do PagSeguro
        3 - Retornar um objeto PaymentRequest
        '''
        raise NotImplementedError()
