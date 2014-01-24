#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, logging
import logging.config

from os.path import expanduser 

import yaml

from yaml import load
try:
  from yaml import CLoader as Loader
except ImportError:
  from yaml import Loader

from manager import DBManager

def main(argv):
  home = os.path.expanduser('~')
  input_file = home + '/.db_backup.yml'

  try:
    stream = open(input_file, 'r')
    data = load(stream, Loader=Loader)

    bak = DBManager(**data['db_setup'])

  except FileNotFoundError:
    logger.exception('File not found... Exiting!')
    sys.exit(-1)

def init_logging(default_dir='log', default_path='logger.yml',
                 default_level=logging.INFO, env_key='LOG_CFG'):
  try:
    os.makedirs(default_dir, exist_ok=True)
  except OSError as e:
    logging.exception('OSError: ')
    sys.exit(-1)
    
  path = default_path
  value = os.getenv(env_key, None)
  
  if value:
    path = value

  if os.path.exists(path):
    with open(path, 'rt') as f:
      config = yaml.load(f.read())
      
    logging.config.dictConfig(config)
  else:
    logging.basicConfig(level=default_level)
  
  logger = logging.getLogger(__name__)
  logger.info('Started running %s', __file__)

  return logger

if __name__ == '__main__':
  logger = init_logging()
  
  main(sys.argv[1:])
