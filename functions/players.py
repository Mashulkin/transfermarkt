# -*- coding: utf-8 -*-
"""
Getting player information from the database
"""
from simple_settings import settings
from common_modules.parser import Parser
from common_modules.json_rw import json_write


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '25.02.2023'


def get_teams(league_id):
    url = f'{settings.API_URL}/teams/{league_id}'
    requests_players = Parser(url)
    players = requests_players.parser_result()
    return players


def get_players(team_id):
    url = f'{settings.API_URL}/players/{team_id}'
    requests_players = Parser(url)
    players = requests_players.parser_result()
    return players
