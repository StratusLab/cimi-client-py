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

import string

import cimi.client.api.utils as utils
from cimi.client.api.cloud_entry_point import CloudEntryPoint


class Connector:

    session = None
    cloud_entry_point = None
    username = None
    password = None

    login_url = None
    logout_url = None

    def __init__(self, endpoint, ssl_verify=True, cert=None, username=None, password=None):

        self.username = username
        self.password = password

        self.session = utils.initialize_session(ssl_verify, cert=cert)

        endpoint = string.rstrip(endpoint, '/ ') + '/'
        self.login_url = endpoint + 'login'
        self.logout_url = endpoint + 'logout'

        self.cloud_entry_point = CloudEntryPoint(endpoint, session=self.session)

    def login(self):
        data = None
        if self.username is not None and self.password is not None:
            data = {'username': self.username, 'password': self.password}

        self.session.post(self.login_url, data=data)

    def logout(self):
        self.session.get(self.logout_url)
