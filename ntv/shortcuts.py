# -*- coding: utf-8 -*-
from .web import fetcher, result_to_dict, filtered


def search(date, **kwargs):
    """
    Search helper function
    """
    return filtered(result_to_dict(fetcher(date)), **kwargs)
