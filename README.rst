================
 python-package-poetry
================

:Author: caerulescens <caerulescens.github@proton.me>
:Description:

==============
 dependencies
==============


+------------+--------------------------------------------+
| dependency | description                                |
+============+============================================+
| `cpython`_ | programming language                       |
+------------+--------------------------------------------+
| `pyenv`_   | python version management                  |
+------------+--------------------------------------------+
| `poetry`_  | python package and dependency management   |
+------------+--------------------------------------------+
| `make`_    | generates executables from source files    |
+------------+--------------------------------------------+

=========
 install
=========

#. install `cpython`_, `pyenv`_, `poetry`_, and `make`_
#. initialize poetry project::

    poetry install

#. initialize pre-commit hooks::

    pre-commit install

=======
 usage
=======

run::

    python main.py

test::

    pytest .

coverage::

    coverage run -m pytest
    coverage report -m

tox::

    todo

docs::

    make -C docs html

pre-commit::

    pre-commit run --all-files

black::

    black .

isort::

    isort --profile black --filter-files

ruff::

    ruff .

mypy::

    mypy .


.. _cpython: https://www.python.org/
.. _pyenv: https://github.com/pyenv/pyenv
.. _poetry: https://python-poetry.org/
.. _make: https://www.gnu.org/software/make/