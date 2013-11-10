# PagSeguro-Python


[![Build Status](https://api.travis-ci.org/ricardosasilva/pagseguro-python.png)](https://api.travis-ci.org/ricardosasilva)



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
