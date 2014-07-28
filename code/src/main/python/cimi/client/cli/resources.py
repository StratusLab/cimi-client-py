
import logging

from cliff.command import Command
from cliff.lister import Lister

import cimi.client.cli.utils as utils

class Collections(Lister):
    """Lists the resource collections available from the CIMI server"""

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        cep = utils.get_cloud_entry_point(self.app.cfg)
        return (('collection_uri'), (sorted(cep.keys())))

class Show(Command):
    """Show the given resource"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Show, self).get_parser(prog_name)
        parser.add_argument('resource_uri')
        return parser

    def take_action(self, parsed_args):
        cep = utils.get_cloud_entry_point(self.app.cfg)
        base_uri = cep.base_uri

class List(Command):
    """List the resources for the given collection"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(List, self).get_parser(prog_name)
        parser.add_argument('collection_uri')
        return parser

    def take_action(self, parsed_args):
        cep = utils.get_cloud_entry_point(self.app.cfg)
        base_uri = cep.base_uri

