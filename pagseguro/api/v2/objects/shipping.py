# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from pagseguro.api.v2.objects.shipping_address import shipping_address_schema
from voluptuous import Schema, Object, Any, All, Range


class Shipping(object):
    '''
    Dados do frete.

    :param shipping_type: (Opcional) Tipo de frete.Informa o tipo de frete a ser usado para o envio do
    produto. Esta informação é usada pelo PagSeguro para calcular, junto aos Correios, o valor
    do frete a partir do peso dos itens. A tabela abaixo descreve os valores aceitos e seus significados:
    1 - Encomenda normal (PAC).
    2 - Sedex
    3 - Tipo de frete não especificado.
    :type shipping_type: Inteiro: 1, 2 ou 3.

    :param cost: Valor total do frete. (Opcional)
    :type cost: float, com duas casas decimais separadas por ponto (p.e, 1234.56), maior que 0.00 e menor ou igual a 9999999.00.

    :param address: Dados do endereço de envio.
    :type address: Objeto do tipo ShippingAddress


    >>> shipping = Shipping(shipping_type=3)
    >>> shipping.validate()

    >>> shipping = Shipping(shipping_type=4)
    >>> shipping.validate()
    Traceback (most recent call last):
        ...
    MultipleInvalid: not a valid value for object value @ data['shipping_type']

    >>>

    '''

    def __init__(self, shipping_type=None, cost=None, address=None,):
        self.shipping_type = shipping_type
        self.cost = cost
        self.address = address

    def validate(self):
        shipping_schema(self)


shipping_schema = Schema(Object(
    {
        'shipping_type': Any(1, 2, 3),
        'cost': All(float, Range(min=0.01, max=9999999)),
        'address': shipping_address_schema,
    }, cls=Shipping))
