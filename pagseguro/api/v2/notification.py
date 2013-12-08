# -*- coding: utf-8 -*-
from pagseguro.api.v2 import settings
from pagseguro.api.v2.transaction import transaction_schema
from pagseguro.exceptions import PagSeguroApiException
import dateutil.parser
import logging
import requests
import xmltodict

logger = logging.getLogger(__name__)

class Notification(object):
    '''
    Classe para tratamento das notificações sobre o status de pagamentos
    '''

    def __init__(self, email, token, notification_code, notification_type='transaction', notification_url=settings.PAGSEGURO_NOTIFICATION_URL):
        if notification_type != 'transaction':
            logger.warning(u'O campo notificationType recebido é diferente do valor esperado: Deveria ser "transaction" mas foi recebido "%s"' % notification_type)
 
        self.notification_code = notification_code
        self.notification_url = notification_url
        self.response = self._get_notification(email, token)
        self.notification_code = notification_code

    def _get_notification(self, email, token):
        ''' Consulta o status do pagamento '''        
        url = u'{notification_url}{notification_code}?email={email}&token={token}'.format(
                                                                                  notification_url=self.notification_url,
                                                                                  notification_code=self.notification_code,
                                                                                  email=email,
                                                                                  token=token)
        req = requests.get(url)
        if req.status_code == 200:
            self.xml = req.text
            logger.debug( u'XML com informacoes da transacao recebido: {0}'.format(self.xml) )
            transaction_dict = xmltodict.parse(self.xml)
            # Validar informações recebidas
            transaction_schema(transaction_dict)
            self.transaction = transaction_dict.get('transaction')
        else:
            raise PagSeguroApiException(
                        u'Erro ao fazer request para a API de notificacao:' + 
                        ' HTTP Status=%s - Response: %s' % (req.status_code, req.text))                

    @property
    def items(self):
        ''' Lista dos items do pagamento
        '''
        if type(self.transaction['items']['item']) == list:
            return self.transaction['items']['item']
        else:
            return [self.transaction['items']['item'],]

    @property
    def code(self):
        return self.transaction['code']

    @property
    def date(self):
        return dateutil.parser.parse(self.transaction['date'])
