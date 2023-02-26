# -*- coding: utf-8 -*-
"""
Getting price players on gaffr
"""
import addpath
from simple_settings import settings

from common_modules.csv_w import write_csv
from common_modules.txt_r import read_txt
from common_modules.headline import print_headline
from common_modules.my_remove import remove_file

from functions.players import get_teams, get_players
from functions.format import formatPosition
from functions.addreq import add_html

from bs4 import BeautifulSoup


__author__ = 'Vadim Arsenev'
__version__ = '1.1.0'
__data__ = '26.02.2023'


ORDER = list(map(lambda x: x.split(':')[0].strip(), \
    read_txt(settings.COLUMNS).split('\n')))


def addPlayerInfo(url):
    html = add_html(url)
    soup = BeautifulSoup(html, 'lxml')

    box1 = soup.find_all('div', class_='data-header__club-info')
    spans = box1[0].find_all('span')
    league = spans[1].find('a').text.strip()
    contractExpires = spans[7].text.strip()

    box2 = soup.find_all('div', class_='data-header__details')
    lis = box2[0].find_all('li')
    age = lis[0].find('span').text.strip().split('(')[1][:-1]
    citizenship = lis[2].find('span').text.strip()
    positionOnField = lis[4].find('span').text.strip()

    box3 = soup.find_all('div', class_='data-header__box--small')
    try:
        playerCost = box3[0].find('a').text.strip().split(' ')[0]
    except IndexError:
        playerCost = ''

    return league, contractExpires, age, citizenship, \
        positionOnField, playerCost


def realPlayers(players, teamName):
    """
    The main module for performing all operations of a request
       and writing to a file
    """
    print_headline(settings.RESULT_FILE[0], settings.COLUMNS, ORDER)
    for player in players:
        # ***** Main query *****
        playerId = player['id']
        playerName = player['name']
        positionId = player['positionId']
        position = formatPosition(positionId)
        linkName = player['link'].split('/')[1]
        fullLink = f'https://www.transfermarkt.co.uk/{linkName}' \
            f'/leistungsdaten/spieler/{playerId}/saison/{settings.SEASON}/plus/1'
        
        league, contractExpires, age, citizenship, \
        positionOnField, playerCost = addPlayerInfo(fullLink)

        # Data generation and writing to file
        data = {
            'playerId': playerId,
            'playerName': playerName,
            'position': position,
            'fullLink': fullLink,
            'teamName': teamName,
            'league': league,
            'contractExpires': contractExpires,
            'age': age,
            'citizenship': citizenship,
            'positionOnField': positionOnField,
            'playerCost': playerCost,
        }

        write_csv(settings.RESULT_FILE[0], data, ORDER)


def mrktPlayers(teams):
    for team in teams:
        teamId = team['id']
        teamName = team['name']
        teamPlayers = get_players(teamId)
        print(teamName)
        realPlayers(teamPlayers, teamName)


def mrktTeams():
    allTeams = []
    for league in settings.LEAGUE:
        teams = get_teams(league)
        allTeams.extend(teams)
    
    return allTeams
        

def main():
    """
    Request information about the players. General request
    """
    allTeams = mrktTeams()
    mrktPlayers(allTeams)


if __name__ == '__main__':
    remove_file(settings.RESULT_FILE[0])
    main()
