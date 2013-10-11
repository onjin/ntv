# -*- coding: utf-8 -*-
from datetime import datetime

import requests

URL_PATTERN = 'http://n.pl/~/epgjson/%s.ejson'


def fetcher(date=datetime.today(), url_pattern=URL_PATTERN):
    """
    Fetch json data from n.pl

    Args:
        date (date) - default today
        url_patter (string) - default URL_PATTERN

    Returns:
        dict - data from api
    """
    api_url = url_pattern % date.strftime('%Y-%m-%d')

    raw_result = requests.get(api_url).json()
    return raw_result


def result_to_dict(raw_result):
    """
    Parse raw result from fetcher into readable dictionary

    Args:
        raw_result (dict) - raw data from `fetcher`

    Returns:
        dict - readable dictionary
    """

    result = {}

    for channel_index, channel in enumerate(raw_result):
        channel_id, channel_name = channel[0], channel[1]
        channel_result = {
            'id': channel_id,
            'name': channel_name,
            'movies': []
        }
        for movie in channel[2]:
            channel_result['movies'].append({
                'title': movie[1],
                'start_time': datetime.fromtimestamp(movie[2]),
                'end_time': datetime.fromtimestamp(movie[2] + movie[3]),
                'inf': True if movie[3] else False,
            })
        result[channel_id] = channel_result

    return result


def filtered(data, **kwargs):
    channel_id = kwargs.get('channel_id', None)
    channel_name = kwargs.get('channel_name', None)
    movie_title = kwargs.get('movie_title', None)

    if channel_id:
        if int(channel_id) in data.keys():
            return {channel_id: data.get(channel_id)}
        else:
            return {}

    # default
    result = data

    if channel_name:
        result = {}
        for index, channel in data.items():
            if channel_name.lower() in channel['name'].lower():
                result.update({index: channel})

    if movie_title:
        result = {}
        for index, channel in data.items():
            for movie in channel['movies']:
                if movie_title.lower() in movie['title'].lower():
                    if not index in result.keys():
                        result[index] = {
                            'id': index,
                            'name': channel['name'],
                            'movies': []
                        }
                    result[index]['movies'].append(movie)
    return result
