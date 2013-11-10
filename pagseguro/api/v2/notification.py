# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from pagseguro.api.v2 import settings
from pagseguro.exceptions import PagSeguroApiException
import requests
import xmltodict


class Notification(object):
    '''
    Classe para tratamento das notificações sobre o status de pagamentos
    '''

    def __init__(self, email, token, notification_code):
        self.response = self._get_notification(email, token, notification_code)
        self.notification_code = notification_code

    def _get_notification(self, email, token, notification_code):
        ''' Consulta o status do pagamento '''
        url = u'%s%s?email=%s&token=%s' % (settings.PAGSEGURO_NOTIFICATION_URL, notification_code, email, token)
        req = requests.get(url)
        if req.status_code == 200:
            self.transaction = xmltodict.parse(req.text)
        else:
            raise PagSeguroApiException(
                u'Erro ao fazer request para a API de notificacao:' +
                ' HTTP Status=%s - Response: %s' % (req.status_code, req.text))
