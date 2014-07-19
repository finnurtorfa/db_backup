#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, logging

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.serializer import Serializer

class ArgumentError(ValueError):
  pass

class DBManager(object):
  def __init__(self, filename=None, **kwargs):
    self.logger = logging.getLogger(__name__)
    self.url = self._set_url(**kwargs)
    self.filename = filename
    self.engine = create_engine(self.url)
    self.connection = self.engine.connect()

    self.metadata = MetaData(bind=self.engine)
    self.metadata.reflect()

    Session = sessionmaker(bind=self.engine)
    self.session = Session()

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

  def serialize(self):
    """ Serializes data from tables in a database and writes them to a file
    """
    with open(self.filename, 'wb') as filename:
      serializer = Serializer(file=filename)
      for t in self.metadata.sorted_tables:
        q = self.session.query(t)
        serializer.dump(q.all())

__version__ = '0.1'
