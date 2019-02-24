# -*- coding: utf-8 -*-

"""The Antibody Registry provides identifiers for antibodies used in publications."""

from .constants import get_version
from .manager import Manager

__all__ = [
    'Manager',
    'get_version',
]
