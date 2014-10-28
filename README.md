ida-colorschemes
================
What in the f*ck?!*$ Yup, it's a colorscheme generator for IDA Pro 6.4+, written in Python 2.7, using Jinja2 & PyYAML.

*Note: Not quite done yet, checked it in early, so I have some version control.*

About
-----
In IDA Pro 6.4, Hex-Rays introduced .clr colorschemes. The file format and GUI interface is really picky, and after messing around for 15 minutes I could already tell that I was going to spend way too much time tweaking it ... so I decided to spend way more time building a python script to generate colorscheme files from palettes.

**But whyyyyyyyy?**
The .clr format is extremely picky:
- You can't comment your .clr file, and the variable names are underwhelming as a documentation resource.
- Any adjustment to the whitespace breaks the .clr file and it won't import. No errors will be reported.
- There's no support for variable bindings, which makes the configuration process impossibly tedious (for me).

To make the color configuration process _really_ easy, ida-colorschemes does the following:

- Colorschemes are written in YAML. This allows us to add comments, modify whitespace, and leverage `node anchors` for variable substitution.
- The default.jinja2 template has been commented to provide additional information about variables.
- Version dependent .clr files have been converted into jinja2 templates.
- The colorscheme configuration is merged into the template, and the final .clr file is written.
- Palette can be leveraged to generate highlighting and accent colors from the base palette (soon).

Installation
------------
ida-colorschemes has the following dependencies:

- libyaml
- python 2.7
    - cliff
    - jinja2
    - palette
    - pyyaml

NOTE: If you want to mess with the internals, I recommend installing bpython, then running the script with: `bpython -i idacs.py`.

Example setup on OSX (using homebrew & virtualenv/virtualenvwrapper):

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

    ./idacs.py


TODO
----
- Add dynamic palette generation using python-palette.
- Finish figuring out all the various color settings.
- Build some modular 'color groups' for use in the colorschemes.
- Add CLI options.
