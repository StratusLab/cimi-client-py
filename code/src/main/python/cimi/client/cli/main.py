# -*- coding: utf-8 -*-
#
# Copyright (c) 2014, Centre National de la Recherche Scientifique (CNRS)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging
import sys

import os.path

import ConfigParser

from cliff.app import App
from cliff.commandmanager import CommandManager


class CimiClientApp(App):

    log = logging.getLogger(__name__)

    cfg_file = os.path.join(os.path.expanduser('~'), '.cimi.cfg')

    cfg_defaults = {'ssl_verify': False}

    cfg = None

    def __init__(self):
        super(CimiClientApp, self).__init__(
            description='CIMI client',
            version='0.1',
            command_manager=CommandManager('cimi.client'),
        )

    def initialize_app(self, argv):
        self.log.debug('initialize_app')
        self.cfg = self._read_cfg()

    def prepare_to_run_command(self, cmd):
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.log.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.log.debug('got an error: %s', err)

    def _cfg_to_dict(self):
        pass

    def _read_cfg(self):
        if os.path.exists(self.cfg_file):
            self.log.info('reading configuration file: %s' % self.cfg_file)
            parser = ConfigParser.SafeConfigParser()
            parser.read(self.cfg_file)
            return dict(parser.items('cimi') + parser.items('DEFAULT') + self.cfg_defaults.items())
        else:
            self.log.warn('configuration file (%s) does not exist' % self.cfg_file)
            return self.cfg_defaults.copy()


def main(argv=sys.argv[1:]):
    app = CimiClientApp()
    return app.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
