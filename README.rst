===============================
ntv
===============================

.. image:: https://badge.fury.io/py/ntv.png
    :target: http://badge.fury.io/py/ntv
    
.. image:: https://travis-ci.org/onjin/ntv.png?branch=master
        :target: https://travis-ci.org/onjin/ntv

.. image:: https://pypip.in/d/ntv/badge.png
        :target: https://crate.io/packages/ntv?version=latest


n.tv api

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
