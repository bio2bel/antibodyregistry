# -*- coding: utf-8 -*-

"""SQLAlchemy models for Bio2BEL Antibody Registry."""

import logging

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from .constants import MODULE_NAME

__all__ = [
    'Base',
    'Antibody',
]

logger = logging.getLogger(__name__)

Base: DeclarativeMeta = declarative_base()

ANTIBODY_TABLE_NAME = f'{MODULE_NAME}_antibody'


class Antibody(Base):
    """Represents an antibody."""

    __tablename__ = ANTIBODY_TABLE_NAME

    id = Column(Integer, primary_key=True)
    antibodyregistry_id = Column(String(16), unique=True, nullable=False)
    name = Column(String(1023), nullable=False)
    vendor = Column(String(255), nullable=False)
