# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Schema validation helpers."""

from __future__ import annotations

from .loader import load_schema


def validate_schema(data: dict | list, name: str) -> None:
    """Validate data to match schema."""
    # Import this lazily as it is expensive
    from jsonschema import FormatChecker, validate  # noqa: PLC0415

    schema = load_schema(name)
    validate(data, schema, format_checker=FormatChecker())
