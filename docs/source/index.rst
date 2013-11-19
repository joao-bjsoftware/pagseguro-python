.. PagSeguro-Python documentation master file, created by
   sphinx-quickstart on Sat Nov  9 23:08:45 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==========================================
Documentação do PagSeguro-Python |version|
==========================================


O que é
-------

 Uma biblioteca Python para acesso à API versão 2.0 do PagSeguro. 


Instalação
----------

  Utilize o pip::

    $ pip install pagseguro-python

  Ou você pode acessar os fontes através do GitHub em::
  
    https://github.com/ricardosasilva/pagseguro-python



Guia rápido 
-----------

    Para os impacientes:

	>>> from pagseguro import Payment
	>>> pagamento = Payment(email='emaildasuaconta@dominio.tld', token='seutokendeaacessocom32caracteres')
	# Adicionar um item ao pedido, com 2 produtos e custo total de R$ 7,00
	>>> pagamento.add_item(item_id='id-do-item-', description='Desc. do produto', amount=7, quantity=2)
	# Adiciona informações sobre o comprador
	>>> pagamento.set_client(name='Adam Yauch', phone_area_code=11, phone_number=12341234, cpf='93537621701')
	# E um custo para o frete
	>>> pagamento.set_shipping(cost=1.2)
	# Enviar a solicitação ao PagSeguro
	>>> pagamento.request()
	# Em caso de sucesso você pode obter a url para direcionar o usuário com:
	>>> url = pagamento.payment_url


Indices e Tabelas
-----------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
