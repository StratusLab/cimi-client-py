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

import ConfigParser
import unittest
import os
import tempfile

import cimi.client.api.utils as utils

class UtilsTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReadOptionsNone(self):
        options = utils.read_options()
        self.assertEqual(len(options), 1)
        self.assertEqual(options['ssl_verify'], 'true')

    def testEmptyConfigFile(self):
        _, fname = tempfile.mkstemp()
        try:
            options = utils.read_options(fname)
            self.assertEqual(len(options), 1)
            self.assertEqual(options['ssl_verify'], 'true')
        except:
            os.unlink(fname)

    def testReadEndpoint(self):
        endpoint_value = 'https://localhost:8080/'
        _, fname = tempfile.mkstemp()
        parser = ConfigParser.SafeConfigParser()
        parser.add_section(utils.CFG_SECTION_NAME)
        parser.set(utils.CFG_SECTION_NAME, 'endpoint', endpoint_value)

        with open(fname, 'w') as fp:
            parser.write(fp)

        try:
            options = utils.read_options(fname)
            self.assertEqual(len(options), 2)
            self.assertEqual(options['ssl_verify'], 'true')
            self.assertEqual(options['endpoint'], endpoint_value)

        finally:
            os.unlink(fname)

    def testReadEndpointAndSSLVerify(self):
        endpoint_value = 'https://localhost:8080/'
        _, fname = tempfile.mkstemp()
        parser = ConfigParser.SafeConfigParser()
        parser.add_section(utils.CFG_SECTION_NAME)
        parser.set(utils.CFG_SECTION_NAME, 'endpoint', endpoint_value)
        parser.set(utils.CFG_SECTION_NAME, 'ssl_verify', 'false')

        with open(fname, 'w') as fp:
            parser.write(fp)

        try:
            options = utils.read_options(fname)
            self.assertEqual(len(options), 2)
            self.assertEqual(options['ssl_verify'], 'false')
            self.assertEqual(options['endpoint'], endpoint_value)

        finally:
            os.unlink(fname)

    def testSessionInitialization(self):
        s = utils.initialize_session()
        self.assertEqual(s.headers['content-type'], 'application/json')
        self.assertTrue(s.verify)

    def testSessionInitializationWithoutSSLVerify(self):
        s = utils.initialize_session(ssl_verify=False)
        self.assertEqual(s.headers['content-type'], 'application/json')
        self.assertFalse(s.verify)

if __name__ == "__main__":
    unittest.main()
