# -*- coding: utf-8 -*-
from datetime import datetime

import requests
import requests_cache


requests_cache.install_cache(expire_after=3600)

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

    headers = {'Referer': 'http://n.pl/program-tv'}
    raw_result = requests.get(api_url, headers=headers).json()
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
    start_time = kwargs.get('start_time', None)
    end_time = kwargs.get('end_time', None)

    # default
    result = data

    if channel_id:
        if int(channel_id) in data.keys():
            result = {channel_id: data.get(channel_id)}
        else:
            return {}

    if channel_name:
        filtered_result = {}
        for index, channel in result.items():
            if channel_name.lower() in channel['name'].lower():
                filtered_result.update({index: channel})
        result = filtered_result

    if movie_title:
        filtered_result = {}
        for index, channel in result.items():
            for movie in channel['movies']:
                if movie_title.lower() in movie['title'].lower():
                    if index not in filtered_result.keys():
                        filtered_result[index] = {
                            'id': index,
                            'name': channel['name'],
                            'movies': []
                        }
                    filtered_result[index]['movies'].append(movie)
        result = filtered_result

    if start_time:
        filtered_result = {}
        for index, channel in result.items():
            for movie in channel['movies']:
                if start_time >= movie['start_time']:
                    if index not in filtered_result.keys():
                        filtered_result[index] = {
                            'id': index,
                            'name': channel['name'],
                            'movies': []
                        }
                    filtered_result[index]['movies'].append(movie)
        result = filtered_result

    if end_time:
        filtered_result = {}
        for index, channel in result.items():
            for movie in channel['movies']:
                if end_time <= movie['end_time']:
                    if index not in filtered_result.keys():
                        filtered_result[index] = {
                            'id': index,
                            'name': channel['name'],
                            'movies': []
                        }
                    filtered_result[index]['movies'].append(movie)
        result = filtered_result

    return result
