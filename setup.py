#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2020 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate weblate_schemas
# <https://github.com/WeblateOrg/weblate_schemas>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""Setup file for easy installation."""

import os

from setuptools import find_packages, setup

VERSION = __import__("weblate_schemas").__version__

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    LONG_DESCRIPTION = readme.read()

REQUIRES = list(open("requirements.txt").read().splitlines())

setup(
    name="weblate_schemas",
    version=VERSION,
    author="Michal Čihař",
    author_email="michal@cihar.com",
    description="A collection of schemas used by Weblate",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    license="GPLv3+",
    keywords="i18n l10n gettext translate weblate",
    url="https://weblate.org/",
    download_url="https://github.com/WeblateOrg/weblate_schemas",
    project_urls={
        "Issue Tracker": "https://github.com/WeblateOrg/weblate_schemas/issues",
        "Documentation": "https://docs.weblate.org/",
        "Source Code": "https://github.com/WeblateOrg/weblate_schemas",
        "Twitter": "https://twitter.com/WeblateOrg",
    },
    platforms=["any"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIRES,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Localization",
        "Topic :: Utilities",
    ],
)
