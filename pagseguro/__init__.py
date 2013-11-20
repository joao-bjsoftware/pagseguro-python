# -*- coding: utf-8 -*-
from pagseguro.api.v2.payment import Payment as PaymentV2


class Payment(object):
    '''
    Esta é a classe principal do PagSeguro-Python. É ela que você vai utilizar para realizar toda a 
    comunicação com a API do PagSeguro.

    Documentação da classe:
    
    .. autofunction:: pagseguro.api.v2.payment.Payment


    Exemplos:

    >>> payment = Payment(email=local_settings.PAGSEGURO_ACCOUNT_EMAIL, token=local_settings.PAGSEGURO_TOKEN, version=2)
    >>> payment.add_item(item_id='id-do-item-1', description='Desc. do produto', amount=7, quantity=2)
    >>> payment.add_item(item_id='id-do-item-2', description='Um outro produto', amount=24.1, quantity=2)
    >>> payment.set_client(name='Adam Yauch', phone_area_code=11, phone_number=12341234, cpf='93537621701')
    >>> payment.set_shipping(cost=1.2)
    >>> payment.request()
    >>> url = payment.payment_url
    
    '''

    @staticmethod
    def _payment_factory(version=2, **kwargs):
        if version == 2:
            return PaymentV2(**kwargs)
        else:
            raise NotImplementedError()

    def __init__(self, **kwargs):
        self._payment = self._payment_factory(**kwargs)

    def add_item(self, *args, **kwargs):
        '''
        Método proxy para a classe que implementa o método add_item na
        versão da API escolhida
        '''
        return self._payment.add_item(*args, **kwargs)

    def set_client(self, *args, **kwargs):
        '''
        Método proxy para a classe que implementa o método set_client na
        versão da API escolhida
        '''
        return self._payment.set_client(*args, **kwargs)

    def set_shipping(self, *args, **kwargs):
        '''
        Método proxy para a classe que implementa o método set_shipping na
        versão da API escolhida
        '''
        return self._payment.set_shipping(*args, **kwargs)

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
        ''' URL para redirecionar o usuário para completar o pagamento '''
        return self._payment.payment_url()
