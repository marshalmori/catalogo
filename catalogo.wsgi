activate_this = '/var/www/catalogo/catalogo/venv/bin/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
# exec(open(activate_this).read())

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/catalogo/")

from catalogo import app as application
application.secret_key = '12345'
