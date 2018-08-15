#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/srv/projeto-web/catalogo/catalog')

from catalogo import app as application



application.secret_key = 'marshalmori'  # This needs changing in production env
application.config['DATABASE_URL'] = 'postgresql://catalog:601077@localhost/catalog'
