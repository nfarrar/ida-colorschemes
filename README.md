IDA Colors
==========
What in the f*ck?!*$ Yup, it's a dynamic color palette/scheme/configuration generator for IDA Pro 6.4+, written in Python.


About
-----
In IDA Pro 6.4, Hex-Rays introduced .clr colorschemes. The file format and GUI interface is really picky, and after messing around for 15 minutes I could already tell that I was going to spend way too much time tweaking it ... so I decided to spend way more time building a python script to generate dynamic color palettes.

Justification
-------------
The .clr format is extremely picky:
- You can't comment your .clr file, and the variable names are underwhelming in determining what they actually do.
- Any adjustment to the whitespace breaks the file and it won't import. No errors will be reported.
- There's no support for variable bindings, which is essentially if you want to do anything interesting.

To make configuring your IDA colorscheme a little more enjoyable, idacs.py uses [PyYAML](http://pyyaml.org/) to build the colorscheme configuration files. This allows for documenting, proper whitespacing, and dynamic variables in the configuration file. [Jinja2](http://jinja.pocoo.org/docs/) is used to merge the configuration into IDA version dependent .clr files, generating the final output.

There are some interesting command line options available as well, which allow us to perform some transformations on our palette.

Requirements
------------
Idacolors has the following dependencies:

- libyaml
- python 2.7
    - cliff
    - jinja2
    - palette
    - pyyaml

NOTE: If you want to mess with the internals, I recommend installing bpython, then running the script with: `bpython -i idacs.py`.


Installation
------------
The easiest way to install idacolors is to install libyaml, virtualenv & virtualenvwrapper to the OS, then install the dependencies in the virtual environment. On OSX, this looks like:

    # install os dependencies
    brew install libyaml virtualenv virtualenvwrapper

    # create & activate the virtual environment
    mkvirtualenv idacolors && workon idacolors

    # clone the repo & cd into it
    git clone _REPO_ && cd idacolors

    # install the python dependencies from requirements.txt
    pip install -r requirements.txt


Usage
-----
TODO: Add docs.

    ./idacs.py --help

Bookmarks
---------
Misc references utilized while building this junk.

### Colors

- [Generating Color Ranges in Python](http://stackoverflow.com/questions/876853/generating-color-ranges-in-python)
- [Python Palette](https://pypi.python.org/pypi/palette/0.2)

### Templates

- [Templating using Jinja2](http://pycourse.com/posts/2013/Jul/16/Templating%20and%20Jinja2/)
- [Google Cloud Platform - Using Templates](https://cloud.google.com/appengine/docs/python/gettingstartedpython27/templates) [source](https://github.com/GoogleCloudPlatform/appengine-guestbook-python/tree/part5-templates)
- [Network Configuration Templates with Jinja2](http://keepingitclassless.net/2014/03/network-config-templates-jinja2/) [source](https://github.com/Mierdin/jinja2-nxos-config)
- [From spreadsheet to HTML in 15 minutes with python-tablefu, Jinja and Flask](http://blog.apps.chicagotribune.com/2010/12/07/from-spreadsheet-to-html-in-15-minutes-with-python-tablefu-jinja-and-flask/)

### Configuration

- [Using YAML with variables](http://stackoverflow.com/questions/4150782/using-yaml-with-variables) (stackoverflow.com)
- [Variables in YAML Configuration Files](https://gist.github.com/bowsersenior/979804) (gist)
- [YAML AIN'T MARKUP LANGUAGE | COMPLETELY DIFFERENT](http://jessenoller.com/blog/2009/04/13/yaml-aint-markup-language-completely-different)
- [Google Clout Platform - Configuring with app.yaml](https://cloud.google.com/appengine/docs/python/config/appconfig)

### Logging

- [Good logging practice in Python](http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python)
- [Python Logging Best Practices](http://pieces.openpolitics.com/2012/04/python-logging-best-practices/)
- [Adding a logger to your applications](http://drtomstarke.com/index.php/adding-a-logger-to-your-applications/)
- [A example of logging medium complex configuration using YAML on Python 2.7 or 3.2](https://gist.github.com/glenfant/4358668)
