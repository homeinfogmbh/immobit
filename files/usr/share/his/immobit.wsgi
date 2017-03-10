#! /usr/bin/env python3
"""HIS core handler"""

from homeinfo.lib.rest import RestApp
from immobit import HANDLERS

application = RestApp(HANDLERS, cors=True, debug=True)
