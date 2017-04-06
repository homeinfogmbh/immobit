#! /usr/bin/env python3
"""HIS core handler"""

from wsgilib import RestApp
from immobit import HANDLERS

application = RestApp({'immobit': HANDLERS}, cors=True, debug=True)
