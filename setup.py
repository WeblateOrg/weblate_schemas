#!/usr/bin/env python

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Setup file for easy installation."""

from setuptools import setup

with open("requirements.txt") as handle:
    REQUIRES = list(handle.read().splitlines())

setup(install_requires=REQUIRES)
