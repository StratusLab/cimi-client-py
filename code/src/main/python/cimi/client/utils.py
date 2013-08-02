#!/usr/bin/env python
#
# Copyright (c) 2013, Centre National de la Recherche Scientifique (CNRS)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from ConfigParser import SafeConfigParser
import requests

CFG_SECTION_NAME = 'cimi-client'

def initialize_session(ssl_verify=True):
    """
    Creates new session that will request JSON representations
    of resources and by default will verify the server's SSL
    certificate.
    """
    s = requests.Session()
    s.headers.update('content-type', 'application/json')
    s.verify = ssl_verify
    
    return s

def read_options(filename=None):
    """
    Reads the CIMI client options from the given configuration
    file.  The file must be in the standard 'ini' format with 
    the parameters located in the [cimi-client] section.  The
    accepted parameters are 'endpoint', and 'ssl_verify'.
    
    The endpoint has no default and must be specified.  The 
    flag ssl_verify defaults to True.  This will need to be 
    set to False if self-signed certificates are used on the
    server.
    """
    defaults = {'ssl_verify': True}
    
    if not filename is None:
        cfg_parser = SafeConfigParser(defaults)
        cfg_parser.read(filename)
        if cfg_parser.has_section(CFG_SECTION_NAME):
            return dict(defaults, **dict(cfg_parser.items(CFG_SECTION_NAME)))

    return defaults