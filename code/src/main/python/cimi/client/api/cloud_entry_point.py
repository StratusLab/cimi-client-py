# -*- coding: utf-8 -*-
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

import cimi.client.api.utils as utils
from cimi.client.api.resource import Resource


class CloudEntryPoint(Resource):

    resourceURI = 'http://schemas.dmtf.org/cimi/1/CloudEntryPoint'

    def __init__(self, endpoint, session):
        super(CloudEntryPoint, self).__init__(session, None, endpoint)

    def validate_data(self):
        if self.data is None:
            raise ValueError('CloudEntryPoint cannot be None')

        try:
            t = self.data['resourceURI']
            if t != CloudEntryPoint.resourceURI:
                raise ValueError('expected URI %s but got %s' % (CloudEntryPoint.resourceURI, t))
        except KeyError:
            raise ValueError('key resourceURI is not defined in CloudEntryPoint')

        try:
            self.base_uri = self.data['baseURI']
        except KeyError:
            raise ValueError('key baseURI is not defined in CloudEntryPoint')

    def extract_items(self):

        collections = {}

        for key in self.data:
            try:
                href = self.data[key]['href']
                collections[key] = utils.resolve_href(self.base_uri, href)
            except Exception:
                pass

        return collections

    def _clean_data(self):

        for item in self.items:
            del(self.data[item])
        try:
            del(self.data['operations'])
        except Exception:
            pass
