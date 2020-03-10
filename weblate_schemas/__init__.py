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
"""Schemas used by Weblate."""

__version__ = "0.4"

import json
from pathlib import Path

SCHEMA_BASE = Path(__file__).resolve().parent.joinpath("schemas")


def get_path(name):
    """Build filename for a schema."""
    return SCHEMA_BASE.joinpath(name)


def load_schema(name):
    """Load schema from a disk."""
    with get_path(name).open("r") as handle:
        return json.load(handle)
