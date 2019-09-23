from __future__ import absolute_import

import os

__version__='0.0.1'

# Requred for a application-breaking bug in requests-oauthlib/oauthlib
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = 'workaround'

from gtasks2.gtasks2 import Gtasks
