#! /usr/bin/env python3
"""HIS core handler"""

from wsgilib import RestApp
from immobit import HANDLERS

application = RestApp(HANDLERS, cors=True, debug=True)
