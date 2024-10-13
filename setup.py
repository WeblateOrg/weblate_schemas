#!/usr/bin/env python

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Setup file for easy installation."""

from setuptools import setup

with open("requirements.txt") as handle:
    REQUIRES = list(handle.read().splitlines())

setup(
    name="weblate_schemas",
    entry_points={
        "fedora.messages": [
            "base.message=weblate_schemas.messages:BaseMessage",
            "weblate.message=weblate_schemas.messages:WeblateV1Message",
        ]
    },
    install_requires=REQUIRES,
)
