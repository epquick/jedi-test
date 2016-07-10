#! /usr/bin/env python2.7
"""
Cascading settings.

* default.py contains settings that every deployment of this site will use. 
  It should be checked in to version control.

* local.py contains settings that vary from one deployment to the next, such 
  as DEBUG values. It should not be shared, though sample values can be 
  checked in as local.tmpl.py
"""

from settings.default import *

try:
    from settings.local import * 
except ImportError:
    pass
    
