#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine

class DBManager(object):
  def __init__(self, dialect, dbapi=None, username=None, password=None, addr='localhost',
               port=None, db=None, echo=False):
    self.url = self._set_url(dialect=dialect,
                             dbapi=dbapi,
                             username=username, 
                             password=password, 
                             addr=addr, 
                             port=port,
                             db=db)
    self.engine = create_engine(self.url, echo=echo)

  def _set_url(self, **kwargs):
    """ Returns a string with the database url.

    Keyword argument: 
    dialect     -- string representing the database system to use. 
    dbapi       -- The dialects DBAPI
    username    -- The database user
    password    -- The password of the user
    addr        -- The IP address to use
    port        -- The port to use
    db          -- Name of the database to use
    """
    url = kwargs['dialect'] 
    if kwargs['dbapi']:
      url = '+'.join([url, kwargs['dbapi']])

    if kwargs['username']:
      url = '://'.join([url, kwargs['username']])

    if kwargs['password']:
      url = ':'.join([url, kwargs['password']])

    if kwargs['addr']:
      url = '@'.join([url, kwargs['addr']])

    if kwargs['port']:
      url = ':'.join([url, kwargs['port']])

    if kwargs['db']:
      url = '/'.join([url, kwargs['db']])

    return url

if __name__ == "__main__":
  bak = DBManager(dialect='postgresql', username='username', password='password',
          db='db')

__version__ = '0.1'
