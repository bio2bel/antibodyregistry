# -*- coding: utf-8 -*-

"""Parsers and downloaders for Bio2BEL Antibody Registry."""

from bio2bel.downloading import make_df_getter
from .constants import HEADER, PATH, URL

__all__ = [
    'df_getter',
]

df_getter = make_df_getter(
    URL,
    PATH,
    names=HEADER[:3],
    skiprows=1,
    usecols=[0, 1, 2],
    chunksize=250_000,
)
