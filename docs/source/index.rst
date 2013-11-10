.. PagSeguro-Python documentation master file, created by
   sphinx-quickstart on Sat Nov  9 23:08:45 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bem-vindo à documentação do PagSeguro-Python
============================================


O que é
=======

 Uma biblioteca Python para acesso à API versão 2.0 do PagSeguro. 


Instalação
==========

  Utilize o pip::

    $ pip install py-pagseguro

  Ou você pode acessar os fontes através do GitHub em::
  
    https://github.com/ricardosasilva/py-pagseguro/



Guia rápido 
===========

  Para os impacientes:

    >>> from py_pagseguro import Payment
    >>> pagamento = Payment(email='emaildasuaconta@dominio.tld', token='seutokendeaacessocom32caracteres')
    # Adicionar um item ao pedido, com 2 produtos e custo total de R$ 12,30  
    >>> pagamento.add_item(item_id='id-do-seu-item', description='Descricao do item', amount=12.3, quantity=2)
    # Enviar a solicitação ao PagSeguro 
    >>> pagamento.request()
    # Em caso de sucesso você pode obter a url para direcionar o usuário com:
    >>> url =  pagamento.payment_url()


Indices e Tabelas
=================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
