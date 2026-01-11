# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Schema loading helpers."""

import json
from pathlib import Path

SCHEMA_BASE = Path(__file__).resolve().parent.joinpath("schemas")

SCHEMA_CACHE: dict[str, dict] = {}


def get_path(name: str) -> Path:
    """Build filename for a schema."""
    return SCHEMA_BASE.joinpath(name)


def load_schema(name: str) -> dict:
    """Load schema from a disk."""
    if name not in SCHEMA_CACHE:
        with get_path(name).open("r") as handle:
            SCHEMA_CACHE[name] = json.load(handle)
    return SCHEMA_CACHE[name]
