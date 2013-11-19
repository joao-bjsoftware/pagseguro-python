# PagSeguro-Python


[![Build Status](https://api.travis-ci.org/ricardosasilva/pagseguro-python.png)](https://travis-ci.org/ricardosasilva/pagseguro-python) [![Coverage Status](https://coveralls.io/repos/ricardosasilva/pagseguro-python/badge.png?branch=master)](https://coveralls.io/r/ricardosasilva/pagseguro-python?branch=master)


## Quick Start

```
>>> from pagseguro import Payment
>>> pagamento = Payment(email='emaildasuaconta@dominio.tld', token='seutokendeaacessocom32caracteres')
>>> pagamento.add_item(item_id='id-do-item-1', description='Desc. do produto', amount=7, quantity=2)
>>> pagamento.set_client(name='Adam Yauch', phone_area_code=11, phone_number=12341234, cpf='93537621701')
>>> pagamento.set_shipping(cost=1.2)
>>> pagamento.request()
>>> url = pagamento.payment_url

```

## Install

```
$ pip install pagseguro-python

```

## Documentação

[http://pagseguro-python.readthedocs.org](http://pagseguro-python.readthedocs.org/en/latest/)
