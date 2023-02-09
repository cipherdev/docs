# -*- coding: utf-8 -*-

import sys
import os
import re

# Prefer to use the version of the theme in this repo
# and not the installed version of the theme.
sys.path.insert(0, os.path.abspath('..'))

templates_path = ['_templates']
html_context = {
    "display_github": False,
    "last_updated": True,
    "commit": False,
}
