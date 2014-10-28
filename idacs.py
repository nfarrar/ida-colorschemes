#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: nfarrar
# @Date:   2014-10-27 18:23:41
# @Last Modified by:   Nathan Farrar
# @Last Modified time: 2014-10-28 13:26:30

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
TEMPLATE_FILE = 'ida66.j2'
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

def normalize_color(str):
    """ A jinja filter for normalizing our color output.
    If the first character of the string is a # symbol, strip it. """

    if str[0] == '#':
        str = str[1:]
    return str


class ColorScheme:
    def __init__(self, colorscheme_name='default',
        template_directory=TEMPLATES_DIRECTORY, template_file=TEMPLATE_FILE,
        colorscheme_directory=COLORSCHEMES_DIRECTORY, colorscheme_file=COLORSCHEME_FILE):
        """ Initialize a new colorscheme object. Initialize the object with the
        configuration defaults. We can specify these here if we want - or by passing arguments
        directly into the methods.
        """

        # Initialize our optional arguments.
        self.colorscheme_name = colorscheme_name
        self.template_directory = template_directory
        self.template_file = template_file
        self.colorscheme_path = os.path.join(colorscheme_directory, colorscheme_file)

        # ... and write out some debugging information.
        logging.debug('Set colorscheme name \'' + self.colorscheme_name + '\'.')
        logging.debug('Set template_directory to \'' + self.template_directory + '\'.')
        logging.debug('Set template_file to \'' + self.template_file + '\'.')
        logging.debug('Set colorscheme_path to \'' + self.colorscheme_path + '\'.')

        # self.load_template()
        # self.load_colorscheme()
        # self.build_config()

    def load_template(self, template_directory=None, template_file=None):
        """ Load our template file into our object. We can override the existing values
        by calling this method and passing in arguments.
        """

        # Check for arguments and set the values in our object if they exist.
        if template_directory != None:
            self.template_directory = template_directory
            logging.debug('Set template_directory to \'' + self.template_directory + '\'.')

        if template_file != None:
            self.template_file == template_file
            logging.debug('Set template_file to \'' + self.template_file + '\'.')

        # Initialize the Jinaj2 template environment.
        try:
            self.template_env = Environment(loader=FileSystemLoader(self.template_directory))
            logging.debug('Initialized template environment using \'' + self.template_directory + '\'.' )
        except Exception, e:
            logging.error('Failed to initialize template environment using \'' + self.template_directory + '\'.')
            sys.exit(1)

        # Load our template.
        try:
            self.template = self.template_env.get_template(self.template_file)
            logging.debug('Loaded template from \'' + self.template_file + '\'.')
        except Exception, e:
            logging.error('Failed to load template from \'' + self.template_file + '\'.')
            sys.exit(1)

        # Inject our normalize_color function as a filter into the template environment.
        #self.template_env.filters['nc'] = normalize_color
        self.template_env.globals['nc'] = normalize_color

    def load_colorscheme(self, colorscheme_path = None):
        """ Load our colorscheme configuration from a YAML file. We can provide the path
        to the file as an argument to this function if we want to override the existing
        configuration.
        """

        if colorscheme_path != None:
            self.colorscheme_path = colorscheme_path
            logging.debug('Set colorscheme_path to \'' + self.colorscheme_path + '\'.')

        # Open the colorscheme configuration file for reading.
        try:
            self.colorscheme_file = open(self.colorscheme_path, 'r')
            logging.debug('Opened colorscheme configuration file from \'' + self.colorscheme_path + '\'.')
        except Exception, e:
            logging.error('Failed to open colorscheme configuration file from \'' + self.colorscheme_path + '\'.', exc_info=True)
            cfg_file.close()
            sys.exit(1)

        # Read the contents of the colorscheme configuration file as YAML.
        try:
            self.colorscheme_cfg = yaml.load(self.colorscheme_file)
            self.colorscheme_file.close()
            logging.debug('Loaded colorscheme configuration from \'' + self.colorscheme_path + ' as yaml.')
        except Exception, e:
            logging.error('Failed to load colorscheme configuration from \'' + self.colorscheme_path + 'as yaml.', exc_info=True)
            cfg_file.close()
            sys.exit(1)

    def build_clr(self):
        """ Generate the CLR content from the colorscheme and template. """

        # Merge the colorscheme configuration and jinja template.
        try:
            self.clr_data = self.template.render(self.colorscheme_cfg)
            logging.debug('Successfully merged colorscheme into template.')
        except Exception, e:
            logging.error('Failed to merge colorscheme into template.', exc_info=True)
            sys.exit(1)

    def write_clr(self, clr_path=None):
        """ Write the clr configuration to a file. Fails if the file already exists. If no file path
        is specified, the colorscheme + '.clr' is used.
        """

        if clr_path == None:
            clr_path = self.colorscheme_name + '.clr'

        # Create a handle to a new file for writing. If it already exists, throw an error.
        try:
            if os.path.exists(clr_path):
                # raise IOError('File \'' + clr_path + '\' already exists.')

                # For testing purposes, remove these eventually.
                logging.debug('File \'' + clr_path + '\' already exists, overwriting.')
                clr_file = open(clr_path, 'w+')
                logging.debug('Opened file \'' + clr_path + '\' for writing.')
            else:
                clr_file = open(clr_path, 'w+')
                logging.debug('Opened file \'' + clr_path + '\' for writing.')
        except Exception, e:
            logging.error(e, exc_info=True)
            sys.exit(1)

        try:
            clr_file.write(self.clr_data)
            logging.debug('Wrote clr configuration to \'' + clr_path + '\'.')
        except Exception, e:
            logging.error('Failed to write clr configuration to \'' + clr_path + '\'.', exc_info=True)
            sys.exit(1)


if __name__ == '__main__':
    # Initialize the logging & configuration for our application.
    init_logging()
    init_config()

    # Create a new ColorScheme object using the defaults.
    cs = ColorScheme()

    # Load the files & generate the config. We could overwrite the paths
    # here, if we wanted.
    cs.load_template()
    cs.load_colorscheme()
    cs.build_clr()
    cs.write_clr()




