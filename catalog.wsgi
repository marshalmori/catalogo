#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/projeto-web/')

from catalog import app as application

application.secret_key = 'marshalmori'  # This needs changing in production env
