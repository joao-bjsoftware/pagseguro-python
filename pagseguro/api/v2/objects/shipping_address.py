# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from pagseguro.validators import BrState
from voluptuous import Schema, Object, All, Length, Match


class ShippingAddress(object):
    '''
    Dados do endereço de envio.

    :param street: Nome da rua do endereço de envio. (Opcional)
    :type street: String com tamanho máximo de 80 caracteres

    :param number: Número do endereço de envio. (Opcional)
    :type number: String com tamanho máximo de 20 caracteres

    :param complement: Complemento do endereço de envio. Informa o complemento
    (bloco, apartamento, etc.) do endereço de envio do produto. Este campo é
    opcional e você pode enviá-lo caso já tenha capturado os dados do comprador
    em seu sistema e queira evitar que ele preencha esses dados novamente no
    PagSeguro. (Opcional)
    :type complement: String, com tamanho máximo de 40 caracteres.

    :param district: Bairro do endereço de envio.
    :type district: String. com tamanho máximo de 60 caracteres

    :param postal_code: CEP do endereço de envio.
    :type postal_code: Um número de 8 dígitos.

    :param city: Cidade do endereço de envio. (Opcional)
    :param city: String. Deve ser um nome válido de cidade do Brasil, com no
    mínimo 2 e no máximo 60 caracteres.

    :param state: Estado do endereço de envio. (Opcional)
    :type state: String. Duas letras, representando a sigla do estado brasileiro
    correspondente

    :param country: País do endereço de envio. (Opcional)
    :type country: String. No momento, apenas o valor BRA é permitido.


    >>> address = ShippingAddress(street='Avenida Paulista', number='20', postal_code='12345678', state='SP')
    >>> address.validate()

    >>> address = ShippingAddress(state='AB')
    >>> address.validate()
    Traceback (most recent call last):
       ...
    MultipleInvalid: State invalido. Informe a sigla de um estado brasileiro for object value @ data['state']

    >>> address = ShippingAddress(postal_code='12345678')
    >>> address.validate()

    >>> address = ShippingAddress(postal_code='01234-567')
    >>> address.validate()
    Traceback (most recent call last):
       ...
    MultipleInvalid: PostalCode invalido. Informe um numero com oito digitos for object value @ data['postal_code']

    '''

    def __init__(self,
                 street=None,
                 number=None,
                 complement=None,
                 district=None,
                 postal_code=None,
                 city=None,
                 state=None,
                 country='BRA'):

        self.street = street
        self.number = number
        self.complement = complement
        self.district = district
        self.postal_code = postal_code
        self.city = city
        self.state = state
        self.country = country

    def validate(self):
        shipping_address_schema(self)


shipping_address_schema = Schema(Object(
    {
        'street': All(str, Length(max=80)),
        'number': All(str, Length(max=20)),
        'complement': All(str, Length(max=40)),
        'district': All(str, Length(max=60)),
        'postal_code': All(Match('[\d]{8,8}',
                                 msg=u'PostalCode invalido. Informe um numero com oito digitos'),
                           Length(min=8, max=8)),
        'city': All(str, Length(min=2, max=60)),
        'state': All(BrState(), Length(min=2, max=2)),
        'country': 'BRA',
    }, cls=ShippingAddress)
)
