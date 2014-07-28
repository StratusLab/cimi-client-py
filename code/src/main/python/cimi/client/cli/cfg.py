
import logging

from cliff.command import Command


class Set(Command):
    """Set a configuration parameter"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Set, self).get_parser(prog_name)
        parser.add_argument('key')
        parser.add_argument('value')
        return parser

    def take_action(self, parsed_args):
        self.app.cfg[parsed_args.key] = parsed_args.value

class Get(Command):
    """Get the value of a configuration parameter"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Get, self).get_parser(prog_name)
        parser.add_argument('key')
        return parser

    def take_action(self, parsed_args):
        key = parsed_args.key
        value = self.app.cfg.get(key, None)
        self.app.stdout.write('%s = %s\n' % (key, str(value)))

class Delete(Command):
    """Delete a configuration parameter"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Delete, self).get_parser(prog_name)
        parser.add_argument('key')
        return parser

    def take_action(self, parsed_args):
        self.app.cfg.pop(parsed_args.key, None)

class Show(Command):
    """Show the configuration parameters"""

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        for key in sorted(self.app.cfg.keys()):
            self.app.stdout.write('%s = %s\n' % (key, str(self.app.cfg[key])))

