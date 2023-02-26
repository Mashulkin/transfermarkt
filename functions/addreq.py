# -*- coding: utf-8 -*-
"""
Additional requests
"""
from simple_settings import settings
from common_modules.parser import Parser


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '26.02.2023'


def add_html(url):
    playerInfo = Parser(url)
    html = playerInfo.parser_resultHtml()

    return html
