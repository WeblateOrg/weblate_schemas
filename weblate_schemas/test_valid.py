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
"""Test schemas are valid."""

from jsonschema import validate

from weblate_schemas import load_schema


def test_memory():
    """Test memory schema being valid."""
    validate([], load_schema("weblate-memory.schema.json"))


def test_memory_newline():
    """Test memory entry containing newlines."""
    validate(
        [
            {
                "source": "Error reading config file {filename!r}:\n{error_msg}",
                "target": "Fehler der Konfigurationsdatei {filename!r}:\n{error_msg}",
                "source_language": "en",
                "target_language": "de",
                "origin": "myproject/mycomponent",
                "category": 10000004,
            }
        ],
        load_schema("weblate-memory.schema.json"),
    )


def test_userdata():
    """Test user data schema being valid."""
    validate(
        {
            "basic": {
                "username": "nijel",
                "full_name": "Weblate Admin",
                "email": "michal@cihar.com",
                "date_joined": "2019-11-18T18:53:54.862Z",
            },
            "profile": {
                "language": "cs",
                "suggested": 1,
                "translated": 24,
                "uploaded": 1,
                "hide_completed": False,
                "secondary_in_zen": True,
                "hide_source_secondary": False,
                "editor_link": "",
                "translate_mode": 0,
                "zen_mode": 0,
                "special_chars": "\u00a0 ",
                "dashboard_view": 1,
                "dashboard_component_list": None,
                "languages": ["cs", "vi"],
                "secondary_languages": ["sk"],
                "watched": ["weblate"],
            },
            "auditlog": [
                {
                    "address": "127.0.0.1",
                    "user_agent": "PC / Linux / Firefox 70.0",
                    "timestamp": "2019-11-18T18:58:30.845Z",
                    "activity": "login",
                },
            ],
        },
        load_schema("weblate-userdata.schema.json"),
    )
