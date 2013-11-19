# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from pagseguro.api.v2.objects.document import document_schema
from pagseguro.validators import Email, PhoneArea, PhoneNumber
from voluptuous import Schema, Object, All, Length


class Sender(object):

    def __init__(self, name=None, email=None, phone_area_code=None, phone_number=None, documents=None, born_date=None):
        self.name = name
        self.email = email
        self.phone_area_code = phone_area_code
        self.phone_number = phone_number
        self.documents = documents
        self.born_date = born_date

    def validate(self):
        sender_schema(self)


sender_schema = Schema(Object(
    {
        'name': str,
        'email': All(Email(), Length(max=60)),
        'phone_area_code': All(PhoneArea(), Length(min=2, max=2)),
        'phone_number': All(PhoneNumber(), Length(min=7, max=9)),
        'documents': [document_schema, ],
        'born_date': str #TODO: VALIDAR DATA
    }, cls=Sender)
)
