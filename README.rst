Bio2BEL Antibody Registry |build|
==================================================
The Antibody Registry provides identifiers for antibodies used in publications

Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
``bio2bel_antibodyregistry`` can be installed easily from
`PyPI <https://pypi.python.org/pypi/bio2bel_antibodyregistry>`_
with the following code in your favorite terminal:

.. code-block:: sh

    $ python3 -m pip install bio2bel_antibodyregistry

or from the latest code on `GitHub <https://github.com/bio2bel/antibodyregistry>`_ with:

.. code-block:: sh

    $ python3 -m pip install git+https://github.com/bio2bel/antibodyregistry.git

Setup
-----
Antibody Registry can be downloaded and populated from either the
Python REPL or the automatically installed command line utility.

Python REPL
~~~~~~~~~~~
.. code-block:: python

    >>> import bio2bel_antibodyregistry
    >>> antibodyregistry_manager = bio2bel_antibodyregistry.Manager()
    >>> antibodyregistry_manager.populate()

Command Line Utility
~~~~~~~~~~~~~~~~~~~~
.. code-block:: sh

    bio2bel_antibodyregistry populate


.. |build| image:: https://travis-ci.com/bio2bel/antibodyregistry.svg?branch=master
    :target: https://travis-ci.com/bio2bel/antibodyregistry
    :alt: Build Status

.. |documentation| image:: http://readthedocs.org/projects/bio2bel-antibodyregistry/badge/?version=latest
    :target: http://bio2bel.readthedocs.io/projects/antibodyregistry/en/latest/?badge=latest
    :alt: Documentation Status

.. |pypi_version| image:: https://img.shields.io/pypi/v/bio2bel_antibodyregistry.svg
    :alt: Current version on PyPI

.. |coverage| image:: https://codecov.io/gh/bio2bel/antibodyregistry/coverage.svg?branch=master
    :target: https://codecov.io/gh/bio2bel/antibodyregistry?branch=master
    :alt: Coverage Status

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/bio2bel_antibodyregistry.svg
    :alt: Stable Supported Python Versions

.. |pypi_license| image:: https://img.shields.io/pypi/l/bio2bel_antibodyregistry.svg
    :alt: MIT License
