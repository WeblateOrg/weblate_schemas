# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Test schemas loader."""

import pytest
from jsonschema import Draft202012Validator
from jsonschema.validators import validator_for

from weblate_schemas import get_path, load_schema
from weblate_schemas.loader import SCHEMA_BASE


@pytest.mark.parametrize(
    "name", sorted(path.name for path in SCHEMA_BASE.glob("*.schema.json"))
)
def test_schema_dialect(name: str) -> None:
    """Validate every packaged schema using its declared dialect."""
    schema = load_schema(name)
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert validator_for(schema) is Draft202012Validator
    Draft202012Validator.check_schema(schema)


def test_filename() -> None:
    """Test filename calculation."""
    filename = get_path("weblate-memory.schema.json")
    assert "weblate-memory.schema.json" in filename.parts


def test_load() -> None:
    """Test schema loading."""
    schema = load_schema("weblate-memory.schema.json")
    assert isinstance(schema, dict)
