"""
Imports the system and the 
theme the project is using to the project.
"""

import sys, os
import sphinx_bootstrap_theme

"""
Adds path to the folder ext, where extensions are stored.
"""

sys.path.append(os.path.abspath('ext'))
sys.path.append('.')

"""
Tells Sphinx which extensions to use.
"""

extensions = ['xref', 
              'youtube', 
              'sphinx.ext.autosectionlabel',
              'sphinxcontrib.osexample']

"""
Imports all link files into project.
"""

from links.link import *
from links import *

"""
Tells the project where to look for theme templates and css overrides.
"""
templates_path = ['_templates']
html_static_path = ["_static"]
"""
Tells the project the name of the home page.
"""

master_doc = 'index'

"""
The project name, copyright, and author.
"""
html_show_sourcelink = False
project = u'Docs & Notes'
copyright = u'2023, HuyLe'
author = u'HuyLe'
