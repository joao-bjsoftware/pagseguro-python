# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from voluptuous import Schema, Object, All, Length, Match


class Document(object):
    '''
    Representa um documento do comprador.

    >>> d = Document(document_type='CDF')
    >>> d.validate()
    Traceback (most recent call last):
       ...
    MultipleInvalid: not a valid value for object value @ data['document_type']

    >>> valid_cpf = Document(value='12345678901')
    >>> valid_cpf.validate()

    >>> invalid_cpf = Document(value='123456789as')
    >>> invalid_cpf.validate()
    Traceback (most recent call last):
       ...
    MultipleInvalid: CPF invalido. Informe um numero com 11 digitos for object value @ data['value']
    '''

    def __init__(self, document_type='CPF', value=None):
        self.document_type = document_type
        self.value = value

    def validate(self):
        document_schema(self)

document_schema = Schema(Object(
    {
        'document_type': 'CPF',
        'value': All(Match('[\d]{11}', msg='CPF invalido. Informe um numero com 11 digitos'), Length(min=11, max=11)),
    }, cls=Document)
)
