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

import unittest
import os
import tempfile

import cimi.client.utils as utils

class UtilsTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReadOptionsNone(self):
        options = utils.read_options()
        self.assertEqual(len(options), 1)
        self.assertTrue(options['ssl_verify'])

if __name__ == "__main__":
    unittest.main()
