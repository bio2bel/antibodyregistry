# -*- coding: utf-8 -*-

"""Test constants for Bio2BEL Antibody Registry."""

import logging
import os

__all__ = [
    'HERE',
    'TEST_RESULTS_PATH'
]

logger = logging.getLogger(__name__)

HERE = os.path.dirname(os.path.realpath(__file__))
TEST_RESULTS_PATH = os.path.join(HERE, 'test.results.csv')
