# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from pagseguro.api.v2.objects.checkout import checkout_schema
from pagseguro.validators import Email
from voluptuous import Schema, Object, Required, All, Length


class PaymentRequest(object):
    '''
    Representacão do objeto utilizado para fazer a requisição de pagamento ao PagSeguro

    :param email: (Obrigatório) E-mail da conta que chama a API.
    :type email: String. Um endereço de email válido com no máximo 60 caracteres.

    :param token: (Obrigatório) Token da conta que chama a API.
    :type token: String com 32 caracteres.

    '''

    def __init__(self, email=None, token=None, checkout=None):
        self.email = email
        self.token = token
        self.checkout = checkout

    def validate(self):
        payment_request_schema(self)

    def generate_params(self):
        '''
        Valida os dados e gera dicionario os parâmetros para a requisição HTTP ao
        PagSeguro

        :returns: dictionary
        '''
        self.validate()
        params = {}
        params['email'] = self.email
        params['token'] = self.token
        params['currency'] = self.checkout.currency
        for index, item in enumerate(self.checkout.items, start=1):
            params['itemId%d' % index] = item.item_id
            params['itemDescription%d' % index] = item.description
            params['itemAmount%d' % index] = item.amount
            params['itemQuantity%s' % index] = item.quantity
            if item.shipping_cost:
                params['itemShippingCost%d' % index] = item.shipping_cost
            if item.weight:
                params['itemWeight%d' % index] = item.weight
        return params


payment_request_schema = Schema(Object(
    {
        Required('email'): All(Email(), Length(max=60)),
        Required('token'): All(str, Length(min=32, max=32)),
        Required('checkout'): checkout_schema,
    }, cls=PaymentRequest)
)
