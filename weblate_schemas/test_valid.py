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
"""Test schemas are valid."""

from jsonschema import validate

from weblate_schemas import load_schema


def test_memory():
    """Test memory schema being valid."""
    validate([], load_schema("weblate-memory.schema.json"))


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
