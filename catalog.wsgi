#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/srv/projeto-web/catalogo/catalog')

from catalogo import app as application
from catalogo.database_setup import create_db
from catalogo.seed_database import populate_database


application.secret_key = 'marshalmori'  # This needs changing in production env
application.config['DATABASE_URL'] = 'postgresql://catalog:601077@localhost/catalog'


# Create database and populate it, if not already done so.
create_db(application.config['DATABASE_URL'])
populate_database(application.config['DATABASE_URL'])
