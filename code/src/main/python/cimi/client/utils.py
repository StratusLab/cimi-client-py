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
import urlparse

CFG_SECTION_NAME = 'cimi-client'


def initialize_session(ssl_verify=True, cert=None):
    """
    Creates new requests session that will request JSON representations of
    resources.  By default, the SSL server certificate will be validated.
    A client certificate may be provided (either as a single file name or
    as a tuple with the certificate/key in separate file).
    """
    s = requests.Session()
    s.headers.update({'content-type': 'application/json'})
    s.verify = ssl_verify
    s.allow_redirects = False

    if cert is not None:
        s.cert = cert

    return s


def extract_operations(base_uri, data):

    operations = {}

    try:
        ops = data['operations']
        for op in ops:
            rel = op['rel']
            href = resolve_href(base_uri, op['href'])
            operations[rel] = href
    except Exception:
        pass

    return operations


def resolve_href(base_uri, href):
    return urlparse.urljoin(base_uri, href)


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
    defaults = {'ssl_verify': 'true'}

    if not filename is None:
        cfg_parser = SafeConfigParser(defaults)
        cfg_parser.read(filename)
        if cfg_parser.has_section(CFG_SECTION_NAME):
            return dict(defaults, **dict(cfg_parser.items(CFG_SECTION_NAME)))

    return defaults
