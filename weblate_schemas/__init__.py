# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Schemas used by Weblate."""

from __future__ import annotations

from .loader import get_path, load_schema
from .validator import validate_schema

__all__ = [
    "get_path",
    "load_schema",
    "validate_schema",
]
