# -*- coding: utf-8 -*-

"""Test cases for Bio2BEL Antibody Registry."""

from bio2bel.testing import AbstractTemporaryCacheClassMixin
from bio2bel_antibodyregistry import Manager
from tests.constants import TEST_RESULTS_PATH

__all__ = [
    'TemporaryCacheClass',
]


class TemporaryCacheClass(AbstractTemporaryCacheClassMixin):
    """A test case containing a temporary database and a Bio2BEL Antibody Registry manager."""

    Manager = Manager
    manager: Manager

    @classmethod
    def populate(cls):
        """Populate the Bio2BEL Antibody Registry database with test data."""
        cls.manager.populate(url=TEST_RESULTS_PATH)
