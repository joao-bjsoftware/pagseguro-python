# -*- coding: utf-8 -*-
'''
Created on Nov 6, 2013

@author: Ricardo Silva
'''
from pagseguro.api.v2.objects.item import item_schema
from pagseguro.api.v2.objects.sender import sender_schema
from pagseguro.api.v2.objects.shipping import shipping_schema
from pagseguro.validators import Email
from voluptuous import Schema, Object, All, Length, Required, Range, Url


class Checkout(object):
    '''
    :param receiver_email: (Opcional) Especifica o e-mail que deve aparecer na tela de pagamento.
    :type receiver_email: String. Precisa ser um email válido com no máximo 60 caracteres.

    :param currency: (Opcional) Indica a moeda na qual o pagamento será feito. No momento, a única opção disponível é BRL (Real).
    :type currency: String. valor precisa ser igual à 'BRL'.

    :param items: (Obrigatório) Lista de itens contidos no pagamento.
    :type items: Objetos do tipo Item

    :param reference: (Opcional) Código de referência. Define um código para fazer referência ao pagamento.
    Este código fica associado à transação criada pelo pagamento e é útil para vincular as transações do
    PagSeguro às vendas registradas no seu sistema.
    :type reference: String, com no máximo 200 caracteres

    :param sender: (Opcional) Dados do comprador.
    :type sender: Objeto do tipo Sender

    :param shipping: (Opcional) Dados do frete.
    :type shipping: Objeto do tipo Shipping

    :param extra_amount: (Opcional) Especifica um valor extra que deve ser adicionado ou
    subtraído ao valor total do pagamento. Esse valor pode representar uma taxa extra a ser
    cobrada no pagamento ou um desconto a ser concedido, caso o valor seja negativo.
    :type extra_amount: Decimal (positivo ou negativo), com duas casas decimais separadas por ponto
    (p.e., 1234.56 ou -1234.56), maior ou igual a -9999999.00 e menor ou igual a 9999999.00.
    Quando negativo, este valor não pode ser maior ou igual à soma dos valores dos produtos.

    :param url_redirect: (Opcional) URL de redirecionamento após o pagamento. Determina a URL para a
    qual o comprador será redirecionado após o final do fluxo de pagamento. Este parâmetro
    permite que seja informado um endereço de específico para cada pagamento realizado.
    :type url_redirect: String com no máximo 255. Precisa ser uma URL válida.

    :param notification_url: (Opcional) Determina a URL para a qual o PagSeguro enviará os
    códigos de notificação relacionados ao pagamento. Toda vez que houver uma mudança no
    status da transação e que demandar sua atenção, uma nova notificação será enviada
    para este endereço.
    :type notification_url: String com no máximo 255. Precisa ser uma URL válida.

    :param max_uses: (Opcional) Determina o número máximo de vezes que o código de pagamento criado
    pela chamada à API de Pagamentos poderá ser usado. Este parâmetro pode ser usado como
    um controle de segurança.
    :type max_uses: Um número inteiro maior que 0 e menor ou igual a 999.

    :param max_ages: (Opcional) Determina o prazo (em segundos) durante o qual o
    código de pagamento criado pela chamada à API de Pagamentos poderá ser usado.
    Este parâmetro pode ser usado como um controle de segurança.
    :type max_ages: Um número inteiro maior ou igual a 30 e menor ou igual a 999999999.

    '''

    def __init__(self,
                 receiver_email=None,
                 currency='BRL',
                 items=None,
                 reference=None,
                 sender=None,
                 shipping=None,
                 extra_amount=None,
                 redirect_url=None,
                 notification_url=None,
                 max_uses=None,
                 max_ages=None):

        self.receiver_email = receiver_email
        self.currency = currency
        self.items = items
        self.reference = reference
        self.sender = sender
        self.shipping = shipping
        self.extra_amount = extra_amount
        self.redirect_url = redirect_url
        self.notification_url = notification_url
        self.max_uses = max_uses
        self.max_ages = max_ages

    def validate(self):
        checkout_schema(self)


checkout_schema = Schema(Object(
    {
        'receiver_email': All(Email(), Length(max=60)),
        'currency': 'BRL',
        Required('items'): [item_schema, ],
        'reference': All(str, Length(max=200)),
        'sender': sender_schema,
        'shipping': shipping_schema,
        'extra_amount': All(float, Range(min=-9999999, max=9999999)),
        'redirect_url': All(Url(), Length(max=255)),
        'notification_url': All(Url(), Length(max=255)),
        'max_uses': All(int, Range(min=1, max=999)),
        'max_ages': All(int, Range(min=30, max=999999999)),
    }, cls=Checkout)
)
