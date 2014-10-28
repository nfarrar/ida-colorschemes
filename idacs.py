#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: nfarrar
# @Date:   2014-10-27 18:23:41
# @Last Modified by:   nfarrar
# @Last Modified time: 2014-10-28 11:05:57

import cliff
import logging
import logging.config
import os
import sys
import yaml

from jinja2 import Environment, FileSystemLoader, Template
from pprint import pprint

# GLOBALS
TEMPLATES_DIRECTORY = 'templates/'
COLORSCHEMES_DIRECTORY = 'colorschemes/'
TEMPLATE_FILE = 'ida66.clr'
COLORSCHEME_FILE = 'default.yml'


def init_logging(cfg_path='_log.yml', default_level=logging.INFO, env_key='LOG_CFG'):
    """ Setup module logging """

    value = os.getenv(env_key, None)

    if value:
        cfg_path = value
    if os.path.exists(cfg_path):
        with open(cfg_path, 'rt') as f:
            cfg = yaml.load(f.read())
        logging.config.dictConfig(cfg)
    else:
        logging.basicConfig(level=default_level)

def init_config(cfg_path='_app.yml'):
    """ Initialize the application configuration """

    global TEMPLATES_DIRECTORY
    global COLORSCHEMES_DIRECTORY
    global TEMPLATE_FILE
    global PALETTE_FILE

    # Open the configuration file.
    try:
        cfg_file = open(cfg_path, 'r')
        logging.debug('Opened ' + cfg_path + ' as configuration file.')
    except Exception, e:
        logging.error('Failed to open ' + cfg_path + ' as configuration file.', exc_info=True)
        cfg_file.close()
        sys.exit(1)

    # Read yaml content from the configuration file.
    try:
        cfg = yaml.load(cfg_file)
        cfg_file.close()
        logging.debug('Read configuration from \'' + cfg_path + '\' as yaml.')
    except Exception, e:
        logging.error('Failed to read configuration from \'' + cfg_path + '\' as yaml.', exc_info=True)
        cfg_file.close()
        sys.exit(1)

    try:
        TEMPLATES_DIRECTORY = cfg['defaults']['templates_directory']
        logging.debug('Set the default value for templates_directory to ' + TEMPLATES_DIRECTORY + '.')
    except Exception, e:
        logging.error('The configuration file ' + cfg_path + ' did not contain a default value for templates_directory.', exc_info=True)
        sys.exit(1)

    try:
        COLORSCHEMES_DIRECTORY = cfg['defaults']['colorschemes_directory']
        logging.debug('Set the default value for colorschemes_directory to ' + COLORSCHEMES_DIRECTORY + '.')
    except Exception, e:
        logging.error('The configuration file ' + cfg_path + ' did not contain a default value for colorschemes_directory.', exc_info=True)
        sys.exit(1)

    try:
        TEMPLATE_FILE = cfg['defaults']['template_file']
        logging.debug('Set the default value for template_file to ' + TEMPLATE_FILE + '.')
    except Exception, e:
        logging.error('The configuration file ' + cfg_path + ' did not contain a default value for template_file.', exc_info=True)
        sys.exit(1)

    try:
        COLORSCHEME_FILE = cfg['defaults']['colorscheme_file']
        logging.debug('Set the default value for colorscheme_file to ' + COLORSCHEME_FILE + '.')
    except Exception, e:
        logging.error('The configuration file ' + cfg_path + ' did not contain a default value for colorscheme_file.', exc_info=True)
        sys.exit(1)

class ColorScheme:
    def __init__(self, colorscheme_name='default',
                 template_directory=TEMPLATES_DIRECTORY, template_file=TEMPLATE_FILE,
                 colorscheme_directory=COLORSCHEMES_DIRECTORY, colorscheme_file=COLORSCHEME_FILE):
        """ Initialize the colorscheme. """

        self.colorscheme_name = colorscheme_name
        logging.debug('Initializing colorscheme \'' + self.colorscheme_name + '\'.')

        self.template_directory = template_directory
        logging.debug('Set template_directory to \'' + self.template_directory + '\'.')

        self.template_file = template_file
        logging.debug('Set template_file to \'' + self.template_file + '\'.')

        self.colorscheme_path = os.path.join(colorscheme_directory, colorscheme_file)
        logging.debug('Set colorscheme_path to \'' + self.colorscheme_path + '\'.')

        try:
            self.template_env = Environment(loader=FileSystemLoader(self.template_directory))
            logging.debug('Initialized template environment using \'' + self.template_directory + '\'.' )
        except Exception, e:
            logging.error('Failed to initialize template environment using \'' + self.template_directory + '\'.')
            sys.exit(1)

        try:
            self.template = self.template_env.get_template(self.template_file)
            logging.debug('Loaded template from \'' + self.template_file + '\'.')
        except Exception, e:
            logging.error('Failed to load template from \'' + self.template_file + '\'.')
            sys.exit(1)

        # Open the colorscheme configuration file.
        try:
            self.colorscheme_file = open(self.colorscheme_path, 'r')
            logging.debug('Opened colorscheme configuration file from \'' + self.colorscheme_path + '\'.')
        except Exception, e:
            logging.error('Failed to open colorscheme configuration file from \'' + self.colorscheme_path + '\'.', exc_info=True)
            cfg_file.close()
            sys.exit(1)

        # Read the colorscheme configuration from the configuration file.
        try:
            self.colorscheme_config = yaml.load(self.colorscheme_file)
            self.colorscheme_file.close()
            logging.debug('Loaded colorscheme configuration from \'' + self.colorscheme_path + ' as yaml.')
        except Exception, e:
            logging.error('Failed to load colorscheme configuration from \'' + self.colorscheme_path + 'as yaml.', exc_info=True)
            cfg_file.close()
            sys.exit(1)

        # pprint(self.colorscheme_config)
        print self.template.render(self.colorscheme_config)


if __name__ == '__main__':
    init_logging()
    init_config()
    cs = ColorScheme()



