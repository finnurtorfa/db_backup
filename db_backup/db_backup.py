#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, getopt, logging

from os.path import expanduser

def init_logging(**kwargs):
  logging.basicConfig(**kwargs)
  logging.info('Started running %s', __file__)

if __name__ == '__main__':
  log_args = {'filename':'db_backup.log', 
              'format': '[%(levelname)s: %(name)s: %(asctime)s] \t %(message)s', 
              'datefmt':'%d-%m-%Y %H:%M:%S',
              'level': 'DEBUG'}  
  init_logging(**log_args)
  main(sys.argv[1:])
