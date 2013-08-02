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

import stratuslab_cimi.utils as utils

class Shell(Object):

    @staticmethod
    def initialize(endpoint=None, ssl_verify=None, filename=None):

        options = utils.read_options(filename)

        if not endpoint is None:
            options['endpoint'] = endpoint

        if not ssl_verify is None:
            options['ssl_verify'] = ssl_verify

        s = utils.initialize_session(ssl_verify)
        options['session'] = s

        self.options = options
