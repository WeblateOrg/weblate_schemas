#!/usr/bin/env python
#
# Copyright © 2012 - 2021 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate weblate_schemas
# <https://github.com/WeblateOrg/weblate_schemas>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
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
    license="MIT",
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
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Localization",
        "Topic :: Utilities",
    ],
)
