# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Schemas used by Weblate."""

import json
from pathlib import Path


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


def validate_schema(data: dict, name: str):
    """Validate data to match schema."""
    # Import this lazily as it is expensive
    from jsonschema import FormatChecker, validate

    schema = load_schema(name)
    validate(data, schema, format_checker=FormatChecker())
