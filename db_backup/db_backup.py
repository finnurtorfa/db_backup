#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, getopt, logging

from os import makedirs
from os.path import expanduser, dirname, exists

from manager import DBManager

def main(argv):
  home = expanduser('~')
  input_file = home + '/.db_backup.yml'

  try:
    stream = open(input_file, 'r')
  except FileNotFoundError:
    logger.exception('File not found... Exiting!')
    sys.exit(-1)

def init_logging(dirname='log', **kwargs):
  try:
    makedirs(dirname, exist_ok=True)
  except OSError as e:
    logging.exception('OSError: ')
    sys.exit(-1)

  logging.basicConfig(**kwargs)
  logger = logging.getLogger(__name__)
  logger.info('Started running %s', __file__)
  return logger

if __name__ == '__main__':
  log_args = {'filename':'log/db_backup.log', 
              'format': '[%(levelname)s: %(name)s: %(asctime)s] \t %(message)s', 
              'datefmt':'%d-%m-%Y %H:%M:%S',
              'level': 'DEBUG'}  
  logger = init_logging(**log_args)
  
  bak = DBManager(dialect='postgresql', username='username', password='password',
          db='db')
  main(sys.argv[1:])
