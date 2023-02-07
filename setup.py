#!/usr/bin/env python

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Setup file for easy installation."""

from setuptools import setup

REQUIRES = list(open("requirements.txt").read().splitlines())

setup(install_requires=REQUIRES)
