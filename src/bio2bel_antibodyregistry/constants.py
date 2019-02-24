# -*- coding: utf-8 -*-

"""Constants for Bio2BEL Antibody Registry."""

import os

from bio2bel import get_data_dir

__all__ = [
    'VERSION',
    'MODULE_NAME',
    'DATA_DIR',
    'get_version',
    'URL',
    'PATH',
    'HEADER',
]

VERSION = '0.0.1-dev'
MODULE_NAME = 'antibodyregistry'
DATA_DIR = get_data_dir(MODULE_NAME)


def get_version() -> str:
    """Get the software version."""
    return VERSION


URL = 'http://antibodyregistry.org/php/fileHandler.php'
PATH = os.path.join(DATA_DIR, 'results.csv')
HEADER = ['antibodyregistry_id', 'name', 'vendor', 'catalog_num', 'proper_citation', 'defining_citation']
