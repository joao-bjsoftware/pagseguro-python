#!/usr/bin/env python
#-*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='pagseguro-python',
    version='0.9',
    description='Uma biblioteca para a API do PagSeguro versão 2.0',
    author='Ricardo Silva',
    author_email='rsas79@gmail.com',
    url='https://github.com/ricardosasilva/pagseguro-python',
    packages=find_packages(),
    install_requires=[
        'voluptuous>=0.8.3',
        'requests>=2.0.1',
        'xmltodict>=0.8.3',
        'python-dateutil>=2.2'
    ],
)