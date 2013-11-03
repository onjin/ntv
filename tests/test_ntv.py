#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ntv
----------------------------------

Tests for `ntv` module.
"""

import unittest
from datetime import datetime

from ntv.web import filtered

TEST_DATA = {
    1313: {
        'index': 1313,
        'name': 'First channel',
        'movies': [
            {
                'title': '1st movie AA',
                'start_time': datetime.strptime(
                    '2013-10-12 00:00:00', '%Y-%m-%d %H:%M:%S'
                ),
                'end_time': datetime.strptime(
                    '2013-10-12 01:00:00', '%Y-%m-%d %H:%M:%S'
                ),
                'inf': False
            },
            {
                'title': '2nd movie AA',
                'start_time': datetime.strptime(
                    '2013-10-12 01:00:00', '%Y-%m-%d %H:%M:%S'
                ),
                'end_time': datetime.strptime(
                    '2013-10-12 02:00:00', '%Y-%m-%d %H:%M:%S'
                ),
                'inf': False
            },
            {
                'title': '3rd movie AA',
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
                'title': '1st movie BB',
                'start_time': datetime.strptime(
                    '2013-10-12 00:00:00', '%Y-%m-%d %H:%M:%S'
                ),
                'end_time': datetime.strptime(
                    '2013-10-12 01:00:00', '%Y-%m-%d %H:%M:%S'
                ),
                'inf': False
            },
            {
                'title': '2nd movie BB',
                'start_time': datetime.strptime(
                    '2013-10-12 01:00:00', '%Y-%m-%d %H:%M:%S'
                ),
                'end_time': datetime.strptime(
                    '2013-10-12 02:00:00', '%Y-%m-%d %H:%M:%S'
                ),
                'inf': False
            },
            {
                'title': '3rd movie BB',
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


class TestFiltered(unittest.TestCase):

    def setUp(self):
        pass

    def test_no_search(self):
        self.assertEquals(TEST_DATA, filtered(TEST_DATA))

    def test_channel_id(self):
        self.assertEquals(
            {1313: TEST_DATA[1313]},
            filtered(TEST_DATA, channel_id=1313)
        )
        self.assertEquals(
            {},
            filtered(TEST_DATA, channel_id=1111)
        )

    def test_channel_name(self):
        self.assertEquals(
            TEST_DATA,
            filtered(TEST_DATA, channel_name='channel')
        )
        self.assertEquals(
            {1313: TEST_DATA[1313]},
            filtered(TEST_DATA, channel_name='first')
        )
        self.assertEquals(
            {1414: TEST_DATA[1414]},
            filtered(TEST_DATA, channel_name='Second')
        )
        self.assertEquals(
            {},
            filtered(TEST_DATA, channel_name='Unknown')
        )

    def test_movie_title(self):
        result = filtered(TEST_DATA, movie_title='1st')
        self.assertEquals(len(result), 2)
        self.assertEquals(len(result[1313]['movies']), 1)
        self.assertEquals(len(result[1414]['movies']), 1)
        self.assertEquals(result[1313]['movies'][0]['title'], '1st movie AA')
        self.assertEquals(result[1414]['movies'][0]['title'], '1st movie BB')

    def test_channel_and_title(self):
        result = filtered(TEST_DATA, channel_name='Second channel',
                          movie_title='1st')
        self.assertEquals(len(result), 1)
        self.assertEquals(len(result[1414]['movies']), 1)
        self.assertEquals(result[1414]['movies'][0]['title'], '1st movie BB')

    def test_start_time(self):
        result = filtered(TEST_DATA, start_time=datetime.strptime(
            '2013-10-12 00:00:00', '%Y-%m-%d %H:%M:%S'
        ))
        self.assertEquals(sum([len(c['movies']) for c in result.values()]), 2)

        result = filtered(TEST_DATA, start_time=datetime.strptime(
            '2013-10-12 01:00:00', '%Y-%m-%d %H:%M:%S'
        ))
        self.assertEquals(sum([len(c['movies']) for c in result.values()]), 4)

        result = filtered(TEST_DATA, start_time=datetime.strptime(
            '2013-10-12 02:00:00', '%Y-%m-%d %H:%M:%S'
        ))
        self.assertEquals(sum([len(c['movies']) for c in result.values()]), 6)

        result = filtered(TEST_DATA, start_time=datetime.strptime(
            '2013-10-12 03:00:00', '%Y-%m-%d %H:%M:%S'
        ))
        self.assertEquals(sum([len(c['movies']) for c in result.values()]), 6)

    def test_end_time(self):
        result = filtered(TEST_DATA, end_time=datetime.strptime(
            '2013-10-12 00:00:00', '%Y-%m-%d %H:%M:%S'
        ))
        self.assertEquals(sum([len(c['movies']) for c in result.values()]), 6)

        result = filtered(TEST_DATA, end_time=datetime.strptime(
            '2013-10-12 01:00:00', '%Y-%m-%d %H:%M:%S'
        ))
        self.assertEquals(sum([len(c['movies']) for c in result.values()]), 6)

        result = filtered(TEST_DATA, end_time=datetime.strptime(
            '2013-10-12 02:00:00', '%Y-%m-%d %H:%M:%S'
        ))
        self.assertEquals(sum([len(c['movies']) for c in result.values()]), 4)

        result = filtered(TEST_DATA, end_time=datetime.strptime(
            '2013-10-12 03:00:00', '%Y-%m-%d %H:%M:%S'
        ))
        self.assertEquals(sum([len(c['movies']) for c in result.values()]), 2)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
