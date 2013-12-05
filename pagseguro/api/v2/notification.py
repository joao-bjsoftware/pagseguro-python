# -*- coding: utf-8 -*-
from pagseguro.api.v2 import settings
from pagseguro.api.v2.transaction import Transaction
from pagseguro.exceptions import PagSeguroApiException
import logging
import requests
import xmltodict

logger = logging.getLogger(__name__)

class Notification(object):
    '''
    Classe para tratamento das notificações sobre o status de pagamentos
    '''

    def __init__(self, email, token, notification_code, notification_type='transaction'):
        if notification_type != 'transaction':
            logger.warning(u'O campo notificationType recebido é diferente do valor esperado: Deveria ser "transaction" mas foi recebido "%s"' % notification_type)

        self.response = self._get_notification(email, token, notification_code)
        self.notification_code = notification_code

    def _get_notification(self, email, token, notification_code):
        ''' Consulta o status do pagamento '''        
        url = u'{notification_url}{notification_code}?email={email}&token={token}'.format(
                                                                                  notification_url=settings.PAGSEGURO_NOTIFICATION_URL,
                                                                                  notification_code=notification_code,
                                                                                  email=email,
                                                                                  token=token)
        req = requests.get(url)
        if req.status_code == 200:
            transaction_text = xmltodict.parse(req.text)
            self.transaction = Transaction(transaction_text)
        else:
            raise PagSeguroApiException(
                        u'Erro ao fazer request para a API de notificacao:' +
                        ' HTTP Status=%s - Response: %s' % (req.status_code, req.text))                
            