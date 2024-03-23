import datetime
import json

import constants
import numpy as np
from slugify import slugify


def read_player_data(season=None):
    with open("./data/players-by-team.json") as json_file:
        data = json.load(json_file)

    data = assign_guids(data)

    for _, player in data.items():
        player["general position"] = assign_general_position(player["position"])
        player["season"] = assign_season_to_player(player["url"])

    if season is not None:
        data = {
            guid: player_details
            for guid, player_details in data.items()
            if player_details["season"] == season
        }

    assert data, "No match lineups to return, have you selected a valid season?"

    return data


def read_match_data(season=None, sort=True):
    with open("./data/match-lineups-with-odds.json") as json_file:
        data = json.loads(json_file)

    for match in data:
        match["info"]["season"] = assign_season_to_match(match["info"]["date"])

    for match in data:
        match["info"]["season"] = assign_season_to_match(match["info"]["date"])

    if season is not None:
        data = [match for match in data if match["info"]["season"] == season]

    if sort:
        for match in data:
            match["info"]["datetime"] = convert_date_to_datetime_object(
                match["info"]["date"]
            )
        data = sorted(data, key=lambda x: x["info"]["datetime"])

    assert data, "No match ineups to return, have you selected a valid season?"

    return data
