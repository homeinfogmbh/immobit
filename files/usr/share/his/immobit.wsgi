#! /usr/bin/env python3
"""HIS core handler"""

from homeinfo.lib.rest import RestApp
from immobit import HANDLERS

application = RestApp({'immobit': HANDLERS}, cors=True, debug=True)
