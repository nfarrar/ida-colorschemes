IDA Colorschemes
================
What in the f*ck?!*$ Yup, it's a dynamic color palette/scheme/configuration generator for IDA Pro 6.4+, written in Python 2.7, using Jinja2 & PyYAML.
Note: Not quite done yet, checked it in early, so I have some version control.

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


TODO
----
- Add dynamic palette generation using python-palette.
- Finish figuring out all the various color settings.
- Build some generic 'color groups' for use in the colorschemes.
- Add CLI options.
