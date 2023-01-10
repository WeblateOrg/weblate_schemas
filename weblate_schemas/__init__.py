#
# Copyright © Michal Čihař <michal@weblate.org>
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
"""Schemas used by Weblate."""

import json
from pathlib import Path
from typing import Dict

from jsonschema import FormatChecker, validate

SCHEMA_BASE = Path(__file__).resolve().parent.joinpath("schemas")

SCHEMA_CACHE = {}


def get_path(name: str):
    """Build filename for a schema."""
    return SCHEMA_BASE.joinpath(name)


def load_schema(name: str):
    """Load schema from a disk."""
    if name not in SCHEMA_CACHE:
        with get_path(name).open("r") as handle:
            SCHEMA_CACHE[name] = json.load(handle)
    return SCHEMA_CACHE[name]


def validate_schema(data: Dict, name: str):
    """Validate data to match schema."""
    schema = load_schema(name)
    validate(data, schema, format_checker=FormatChecker())
