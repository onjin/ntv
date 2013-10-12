===============================
ntv
===============================

.. image:: https://badge.fury.io/py/ntv.png
    :target: http://badge.fury.io/py/ntv
    
.. image:: https://travis-ci.org/onjin/ntv.png?branch=master
        :target: https://travis-ci.org/onjin/ntv

.. image:: https://pypip.in/d/ntv/badge.png
        :target: https://crate.io/packages/ntv?version=latest


Python wrapper over n.pl movies schedule.

* Free software: BSD license

Features
--------

* python wrapper over tv program from n.pl site
* ntv-cli command utility to list and search tv program

Installation
------------

* pip install ntv

CLI usage
---------
List channels from today schedule:

* ntv-cli channels

Find channel by id or by name

* ntv-cli channels film
* ntv-cli channels -c 833

Display all movies from today schedule

* ntv-cli movies

Find movies by channel name or/and movie name

* ntv-cli movies axn
* ntv-cli movies comedy -t madagaskar

Change schedule date by adding `-d` option:

* ntv-cli channels -d 2013-12-24
* ntv-cli movies -d 2013-12-24

API
---

**ntv.shortcuts.search**

Shorcut function to search n.pl schedule and get result as dictionary

Example usage:

.. code-block:: python

    from ntv.shortcuts import search

    print search()
    print search(datetime.today())

    print search(datetime.today(), channel_id=8)
    print search(datetime.today(), channel_name='comedy')
    print search(datetime.today(), movie_title='braindead')
    print search(datetime.today(), channel_name='comedy', movie_title='braindead')

Example result:

.. code-block:: python

    {
        1313: {
            'index': 1313,
            'name': 'First channel',
            'movies': [
                {
                    'title': '1st movie',
                    'start_time': datetime.strptime(
                        '2013-10-12 00:00:00', '%Y-%m-%d %H:%M:%S'
                    ),
                    'end_time': datetime.strptime(
                        '2013-10-12 01:00:00', '%Y-%m-%d %H:%M:%S'
                    ),
                    'inf': False
                },
                {
                    'title': '2nd movie',
                    'start_time': datetime.strptime(
                        '2013-10-12 01:00:00', '%Y-%m-%d %H:%M:%S'
                    ),
                    'end_time': datetime.strptime(
                        '2013-10-12 02:00:00', '%Y-%m-%d %H:%M:%S'
                    ),
                    'inf': False
                },
                {
                    'title': '3rd movie',
                    'start_time': datetime.strptime(
                        '2013-10-12 02:00:00', '%Y-%m-%d %H:%M:%S'
                    ),
                    'end_time': datetime.strptime(
                        '2013-10-12 03:00:00', '%Y-%m-%d %H:%M:%S'
                    ),
                    'inf': False
                },
            ]
        },
        1414: {
            'index': 1414,
            'name': 'Second channel',
            'movies': [
                {
                    'title': '1st movie',
                    'start_time': datetime.strptime(
                        '2013-10-12 00:00:00', '%Y-%m-%d %H:%M:%S'
                    ),
                    'end_time': datetime.strptime(
                        '2013-10-12 01:00:00', '%Y-%m-%d %H:%M:%S'
                    ),
                    'inf': False
                },
                {
                    'title': '2nd movie',
                    'start_time': datetime.strptime(
                        '2013-10-12 01:00:00', '%Y-%m-%d %H:%M:%S'
                    ),
                    'end_time': datetime.strptime(
                        '2013-10-12 02:00:00', '%Y-%m-%d %H:%M:%S'
                    ),
                    'inf': False
                },
                {
                    'title': '3rd movie',
                    'start_time': datetime.strptime(
                        '2013-10-12 02:00:00', '%Y-%m-%d %H:%M:%S'
                    ),
                    'end_time': datetime.strptime(
                        '2013-10-12 03:00:00', '%Y-%m-%d %H:%M:%S'
                    ),
                    'inf': False
                },
            ]
        },
    }

Low-level API
-------------

**ntv.web.fetcher**

Gets raw data from website as

.. code-block:: python

    from ntv.web import fetcher

    print fetcher()
    print fetcher(datetime.today())

**ntv.web.result_to_dict**

Changes raw result from `fetcher` into final dictionary

.. code-block:: python

    from ntv.web import fetcher, result_to_dict

    print result_to_dict(fetcher())

**ntv.web.filtered**

Filters result dict using params: channel_id, channel_name, movie_title

.. code-block:: python

    from ntv.web import fetcher, result_to_dict, filtered

    print filtered(result_to_dict(fetcher()), channel_name='canal')
