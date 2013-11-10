# PagSeguro-Python


[![Build Status](https://api.travis-ci.org/ricardosasilva/pagseguro-python.png)](https://travis-ci.org/ricardosasilva/pagseguro-python) [![Coverage Status](https://coveralls.io/repos/ricardosasilva/pagseguro-python/badge.png?branch=master)](https://coveralls.io/r/ricardosasilva/pagseguro-python?branch=master)


## Quick Start

```
>>> from pagseguro import Payment
>>> pagamento = Payment(email='emaildasuaconta@dominio.tld', token='seutokendeaacessocom32caracteres')
>>> pagamento.add_item(item_id='id-do-seu-item', description='Descricao do item', amount=12.3, quantity=1)
>>> resultado = pagament.request()
```

## Install

```
$ pip install pagseguro-python

```

## Documentação

[http://pagseguro-python.readthedocs.org](http://pagseguro-python.readthedocs.org/en/latest/)
