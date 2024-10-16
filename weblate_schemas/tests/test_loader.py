# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Test schemas loader."""

from weblate_schemas import get_path, load_schema


def test_filename():
    """Test filename calculation."""
    filename = get_path("weblate-memory.schema.json")
    assert "weblate-memory.schema.json" in filename.parts


def test_load():
    """Test schema loading."""
    schema = load_schema("weblate-memory.schema.json")
    assert isinstance(schema, dict)
