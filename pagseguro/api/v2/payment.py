# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from pagseguro.api.base_payment import BasePaymentRequest
from pagseguro.api.v2 import settings
from pagseguro.api.v2.objects.checkout import Checkout
from pagseguro.api.v2.objects.document import Document
from pagseguro.api.v2.objects.item import Item
from pagseguro.api.v2.objects.payment_request import PaymentRequest
from pagseguro.api.v2.objects.sender import Sender
from pagseguro.api.v2.objects.shipping import Shipping
from pagseguro.exceptions import PagSeguroApiException, \
    PagSeguroPaymentException
from xml.etree import ElementTree
import dateutil.parser
import logging
import requests

logger = logging.getLogger(__name__)


class Payment(BasePaymentRequest):
    '''
    Classe que implementa a requisição à API do PagSeguro versão 2
    '''

    def __init__(self,
                 email,
                 token,
                 receiver_email=None,
                 currency='BRL',
                 reference=None,
                 extra_amount=None,
                 url_redirect=None,
                 notification_url=None,
                 max_uses=None,
                 max_age=None):
        self.payment_request = PaymentRequest(email=email, token=token)
        self.payment_request.checkout = Checkout()
        self.payment_request.checkout.receiver_email = receiver_email
        self.payment_request.checkout.currency = currency
        self.payment_request.checkout.reference = reference
        self.payment_request.checkout.extra_amount = extra_amount
        self.payment_request.checkout.url_redirect = url_redirect
        self.payment_request.checkout.notification_url = notification_url
        self.payment_request.checkout.max_uses = max_uses
        self.payment_request.checkout.max_age = max_age
        self.response = None

    def add_item(self, item_id, description, amount, quantity, shipping_cost=None, weight=None):
        item = Item(
            item_id=item_id,
            description=description,
            amount=amount,
            quantity=quantity,
            shipping_cost=shipping_cost,
            weight=weight
        )
        item.validate()
        if not self.payment_request.checkout.items:
            self.payment_request.checkout.items = []

        self.payment_request.checkout.items.append(item)

    def set_client(self, name=None, email=None, phone_area_code=None, phone_number=None, cpf_number=None, born_date=None):
        document = Document(value=cpf_number) # Como na versão 2 da API só é permitido CPF e uma pessoa tem no máximo 1 CPF não será tratado como lista 
        self.payment_request.checkout.sender = Sender(name=name, email=email, phone_area_code=phone_area_code, phone_number=phone_number, documents=[document,], born_date=born_date) 

    def set_shipping(self, shipping_type=None, cost=None, street=None, address_number=None, complement=None, district=None, postal_code=None, city=None, state=None):
        self.payment_request.checkout.shipping = Shipping(shipping_type=shipping_type)

    def _process_response_xml(self, response_xml):
        '''
        Processa o xml de resposta e caso não existam erros retorna um
        dicionario com o codigo e data.

        :return: dictionary
        '''
        result = {}
        xml = ElementTree.fromstring(response_xml)
        if xml.tag == 'errors':
            logger.error(
                u'Erro no pedido de pagamento ao PagSeguro.' +
                ' O xml de resposta foi: %s' % response_xml)
            errors_message = u'Ocorreu algum problema com os dados do pagamento: '
            for error in xml.findall('error'):
                error_code = error.find('code').text
                error_message = error.find('message').text
                errors_message += u'\n (code=%s) %s' % (error_code,
                                                        error_message)
            raise PagSeguroPaymentException(errors_message)

        if xml.tag == 'checkout':
            result['code'] = xml.find('code').text

            try:
                xml_date = xml.find('date').text
                result['date'] = dateutil.parser.parse(xml_date)
            except:
                logger.exception(u'O campo date não foi encontrado ou é invalido')
                result['date'] = None
        else:
            raise PagSeguroPaymentException(
                u'Erro ao processar resposta do pagamento: tag "checkout" nao encontrada no xml de resposta')
        return result

    def payment_url(self):
        '''
        Retorna a url para onde o cliente deve ser redirecionado para
        continuar o fluxo de pagamento.

        :return: str, URL de pagamento
        '''
        if self.response:
            return u'%s?code=%s' % (settings.PAGSEGURO_API_URL, self.response['code'])
        else:
            return None

    def request(self):
        '''
        Faz a requisição de pagamento ao servidor do PagSeguro.

        :returns: str, URL para o cliente continuar o pagamento
        '''

        params = self.payment_request.generate_params()
        req = requests.post(
            settings.PAGSEGURO_API_URL,
            params=params,
            headers={
                'Content-Type':
                'application/x-www-form-urlencoded; charset=ISO-8859-1'
            }
        )
        if req.status_code == 200:
            self.response = self._process_response_xml(req.text)
        else:
            raise PagSeguroApiException(
                u'Erro ao fazer request para a API:' +
                ' HTTP Status=%s - Response: %s' % (req.status_code, req.text))
        return self.response

    def api_version(self):
        return u'2.0'
