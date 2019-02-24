# -*- coding: utf-8 -*-

"""Test cases for Bio2BEL Antibody Registry."""

from bio2bel_antibodyregistry.models import Antibody
from tests.cases import TemporaryCacheClass


class TestPopulate(TemporaryCacheClass):
    """Test the database gets populated."""

    def test_is_populated(self):
        """Test the database reports being populated."""
        self.assertTrue(self.manager.is_populated())
        self.assertEqual(9, self.manager.count_antibodies())

    def test_get_antibody(self):
        """Test looking up an antibody."""
        antibody = self.manager.get_antibody_by_antibodyregistry_id('AB_400666')
        self.assertIsNotNone(antibody)
        self.assertIsInstance(antibody, Antibody)
        self.assertEqual('AB_400666', antibody.antibodyregistry_id)
        self.assertEqual('Rabbit Anti-Human Thrombin Polyclonal Antibody, Unconjugated', antibody.name)
        self.assertEqual('AMERICAN DIAGNOSTICA', antibody.vendor)
