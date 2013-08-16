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
import re
import requests


class Resource(object):

    def __init__(self, session, base_uri, uri):
        self.session = session
        self.base_uri = base_uri
        self.uri = uri
        self.reload()

    def reload(self):
        r = self.session.get(self.uri)
        if r.status_code == requests.codes.ok:
            self.data = r.json()
            self.validate_data()
            self.operations = utils.extract_operations(self.base_uri, self.data)
            self.items = self.extract_items()
        else:
            self.data = None
            self.operations = {}
            self.items = {}

    def show(self):
        print(self.__repr__())

    def allowed_actions(self):
        return self.operations.keys()

    def delete(self):
        return self.do('delete')

    def edit(self, data):
        return self.do('edit', data)

    def add(self, data):
        return self.do('add', data)

    def do(self, cmd, data=None):
        uri = self.operations[cmd]
        if cmd == 'add':
            return self._do_add(uri, data)
        elif cmd == 'edit':
            return self._do_edit(uri, data)
        elif cmd == 'delete':
            return self._do_delete(uri)
        else:
            return self._do_other(uri, data)

    def _do_add(self, uri, body=None):
        r = self.session.post(uri, data=json.dumps(body))
        if r.status_code == requests.codes.ok:
            location = r.headers['Location']
            uri = utils.resolve_href(self.base_uri, location)
            self.reload()
            return r.status_code, uri
        else:
            return r.status_code, None

    def _do_edit(self, uri, body=None):
        r = self.session.put(uri, data=json.dumps(body))
        if r.status_code == requests.codes.ok:
            self.reload()
        return r.status_code

    def _do_delete(self, uri):
        r = self.session.delete(uri)
        if r.status_code == requests.codes.ok:
            self.reload()
        return r.status_code

    def _do_other(self, uri, body=None):
        r = self.session.post(uri, data=json.dumps(body))
        if r.status_code == requests.codes.ok:
            self.reload()
        return r.status_code

    def __getitem__(self, key):
        resource_uri = self.items[key]
        return Resource(self.session, self.base_uri, resource_uri)

    def __setitem__(self, key):
        raise NotImplementedError()

    def __delitem__(self, key):
        raise NotImplementedError()

    def keys(self):
        return self.items.keys()

    def __repr__(self):
        return json.dumps(self.data, sort_keys=True, indent=4)

    def validate_data(self):
        pass

    def extract_items(self):

        resource_uri = self.data['resourceURI']

        items = {}

        if resource_uri.endswith('Collection'):
            item_resource_uri = re.match(r"(.*)Collection$", resource_uri).group(1)

            item_key = None

            for key in self.data:
                try:
                    test_uri = self.data[key][0]['resourceURI']
                    if test_uri == item_resource_uri:
                        item_key = key
                        break
                except Exception:
                    pass

            if item_key:
                sequence = self.data[item_key]
                for i in sequence:
                    resource_id = i['id']
                    items[resource_id] = utils.resolve_href(self.base_uri, resource_id)

        return items


