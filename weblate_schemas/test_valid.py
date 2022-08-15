#
# Copyright © 2012–2022 Michal Čihař <michal@cihar.com>
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

from weblate_schemas import load_schema, validate_schema


def test_validate_manual():
    """Test memory schema being valid."""
    validate([], load_schema("weblate-memory.schema.json"))


def test_memory():
    """Test validate schema API."""
    validate_schema([], "weblate-memory.schema.json")


def test_memory_newline():
    """Test memory entry containing newlines."""
    validate_schema(
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
        "weblate-memory.schema.json",
    )


def test_userdata():
    """Test user data schema being valid."""
    validate_schema(
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
        "weblate-userdata.schema.json",
    )


def test_backup():
    """Test memory schema being valid."""
    validate_schema(
        {
            "metadata": {
                "version": "4.13",
                "server": "Weblate",
                "domain": "weblate.example.com",
                "timestamp": "2021-11-18T18:53:54.862Z",
            },
            "project": {
                "name": "Hello",
                "slug": "hello",
                "web": "https://weblate.org/",
                "instructions": "",
                "set_language_team": False,
                "use_shared_tm": False,
                "contribute_shared_tm": False,
                "access_control": 0,
                "translation_review": False,
                "source_review": False,
                "enable_hooks": False,
                "language_aliases": "",
            },
            "labels": [],
        },
        "weblate-backup.schema.json",
    )


def test_component():
    """Test memory schema being valid."""
    validate_schema(
        {
            "component": {
                "name": "Demo",
                "slug": "demo",
                "vcs": "git",
                "repo": "https://github.com/WeblateOrg/demo.git",
                "push": "",
                "repoweb": "",
                "report_source_bugs": "",
                "branch": "main",
                "push_branch": "",
                "filemask": "po/*.po",
                "template": "",
                "edit_template": False,
                "intermediate": "",
                "new_base": "",
                "file_format": "po",
                "locked": False,
                "allow_translation_propagation": True,
                "enable_suggestions": True,
                "suggestion_voting": True,
                "suggestion_autoaccept": 2,
                "check_flags": "",
                "enforced_checks": [],
                "license": "",
                "agreement": "",
                "new_lang": "contact",
                "language_code_style": "",
                "manage_units": True,
                "merge_style": "rebase",
                "commit_message": "",
                "add_message": "",
                "delete_message": "",
                "merge_message": "",
                "addon_message": "",
                "pull_message": "",
                "push_on_commit": False,
                "commit_pending_age": 24,
                "auto_lock_error": False,
                "source_language": "en",
                "language_regex": "^[^.]+$",
                "variant_regex": "",
                "priority": 100,
                "restricted": False,
                "is_glossary": False,
                "glossary_color": "",
                "remote_revision": "",
                "local_revision": "",
            },
            "translations": [
                {
                    "pk": 1,
                    "language_code": "cs",
                    "plural": {
                        "source": 1,
                        "number": 3,
                        "formula": "(n==1) ? 0 : (n>=2 && n<=4) ? 1 : 2",
                        "type": 2,
                    },
                    "revision": "abcdef",
                    "filename": "po/cs.po",
                },
            ],
            "units": [],
            "screenshots": [],
        },
        "weblate-component.schema.json",
    )
