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

import json
import cimi.client.utils as utils
from urlparse import urljoin

class CloudEntryPoint(object):

    resourceURI = 'http://schemas.dmtf.org/cimi/1/CloudEntryPoint'

    def __init__(self, endpoint, ssl_verify=True):
        self.endpoint = endpoint
        self.session = utils.initialize_session(ssl_verify)
        self.data = None
        self.reload()

    def reload(self):
        resp = self.session.get(self.endpoint)
        data = resp.json()

        self._validate_cep(data)
        self.data = data

        self._extract_collections()
        self._extract_operations()

        self._clean_data()

    def show(self):
        return self.__repr__()

    def _validate_cep(self, data):
        if data is None:
            raise ValueError('CloudEntryPoint cannot be None')

        try:
            t = data['resourceURI']
            if t != CloudEntryPoint.resourceURI:
                raise ValueError('expected URI %s but got %s' % (CloudEntryPoint.resourceURI, t))
        except KeyError:
            raise ValueError('key resourceURI is not defined in CloudEntryPoint')

        try:
            self.base_uri = data['baseURI']
        except KeyError:
            raise ValueError('key baseURI is not defined in CloudEntryPoint')

    def _extract_collections(self):

        collections = {}

        for key in self.data:
            try:
                href = self.data[key]['href']
                collections[key] = self._convert_href(href)
            except Exception:
                pass

        self.collections = collections

    def _extract_operations(self):

        operations = {}

        try:
            ops = self.data['operations']
            for op in ops:
                rel = op['rel']
                href = self._convert_href(op['href'])
                operations[rel] = href
        except Exception:
            pass

        self.operations = operations

    def _convert_href(self, href):
        if href == '/':
            return self.base_uri
        elif href.startswith('/'):
            return urljoin(self.endpoint, href)
        else:
            return urljoin(self.base_uri, href)

    def _clean_data(self):

        for collection in self.collections:
            del(self.data[collection])
        try:
            del(self.data['operations'])
        except Exception:
            pass

    def __repr__(self):
        d = json.dumps(self.data, sort_keys=True, indent=4)
        c = json.dumps(self.collections, sort_keys=True, indent=4)
        o = json.dumps(self.operations, sort_keys=True, indent=4)

        return "CloudEntryPoint (%s)\n%s\nCollections:\n%s\nOperations:\n%s\n" % (self.endpoint, d, c, o)
