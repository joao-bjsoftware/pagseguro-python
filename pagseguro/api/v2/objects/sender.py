# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from pagseguro.api.v2.objects.document import document_schema
from pagseguro.api.v2.objects.phone import phone_schema
from pagseguro.validators import Email
from voluptuous import Schema, Object, All, Length


class Sender(object):

    def __init__(self, name=None, email=None, phone=None, documents=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.documents = documents

    def validate(self):
        sender_schema(self)


sender_schema = Schema(Object(
    {
        'name': str,
        'email': All(Email(), Length(max=60)),
        'phone': phone_schema,
        'documents': [document_schema, ],
    }, cls=Sender)
)
