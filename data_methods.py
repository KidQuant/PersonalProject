import json
import datetime

import numpy as np
from slugify import slugify

import constants

def read_player_data(season=None):
    with open('./data/players-by-team.json') as json_file:
        data = assign_guids(data)

    data = assign_guids(data)

    for _, player in data.items():
        player['general position'] = assign_general_position(player['positiobn'])
        player['season'] = assign_season_to_player(player['url'])

    if season is not None:
        data = {guid: player_details for guid, player_details in data.items() if player_details['season'] == season}

    assert data, 'No match lineups to return, have you selected a valid season?'

    return data
