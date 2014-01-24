#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, logging

from sqlalchemy import create_engine

class ArgumentError(ValueError):
  pass

class DBManager(object):
  def __init__(self, **kwargs):
    self.logger = logging.getLogger(__name__)
    self.url = self._set_url(**kwargs)
    self.engine = create_engine(self.url)

  def _set_url(self, **kwargs):
    """ Returns a string with the database url.

    Keyword argument: 
    dialect  -- string representing the database system to use. 
    dbapi    -- The dialects DBAPI
    username -- The database user
    password -- The password of the user
    address  -- The IP address to use
    port     -- The port to use
    database -- Name of the database to use
    """
    url = ''

    try:
      if 'dialect' not in kwargs:
        raise ArgumentError()

      url = kwargs['dialect'] 
    except ArgumentError:
      self.logger.exception("You must specify a dialect. Exiting!")  
      sys.exit(-1)

    if 'dbapi' in kwargs:
      if kwargs['dbapi'] != 'None':
        url = '+'.join([url, kwargs['dbapi']])
        self.logger.info("Appending to url: %s", url)

    url = '://'.join([url, ''])

    if 'username' in kwargs:
      if kwargs['username'] != 'None':
        url = ''.join([url, kwargs['username']])
        self.logger.info("Appending to url: %s", url)

    if 'password' in kwargs:
      if kwargs['password'] != 'None':
        url = ':'.join([url, kwargs['password']])
        self.logger.info("Appending to url: %s", url)

    if 'address' in kwargs:
      if kwargs['address'] != 'None':
        url = '@'.join([url, kwargs['address']])
        self.logger.info("Appending to url: %s", url)

    if 'port' in kwargs:
      if kwargs['port'] != 'None':
        url = ':'.join([url, kwargs['port']])
        self.logger.info("Appending to url: %s", url)

    if 'database' in kwargs:
      if kwargs['database'] != 'None':
        url = '/'.join([url, kwargs['database']])
        self.logger.info("Appending to url: %s", url)

    return url

__version__ = '0.1'
