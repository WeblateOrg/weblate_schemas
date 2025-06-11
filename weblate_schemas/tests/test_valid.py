# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Test schemas are valid."""

from jsonschema import validate
from jsonschema.exceptions import ValidationError

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
    backup_without_teams = {
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
        "categories": [
            {
                "name": "My category",
                "slug": "my-category",
                "categories": [
                    {
                        "name": "My Subcategory",
                        "slug": "my-subcategory",
                        "categories": [],
                    }
                ],
            }
        ],
    }
    validate_schema(
        backup_without_teams,
        "weblate-backup.schema.json",
    )
    backup_with_teams = backup_without_teams.copy()
    backup_with_teams["teams"] = [
        {
            "name": "English Translation Team",
            "roles": ["Translate"],
            "components": ["my-category/test-component", "glossary"],
            "language_selection": 0,
            "languages": ["en", "en_CA", "ang", "en_IN", "en_GB"],
            "admins": [],
            "enforced_2fa": False,
            "members": [],
            "autogroups": ["^.*$"],
        },
        {
            "name": "Administration",
            "roles": ["Administration", "Manage languages"],
            "components": [],
            "language_selection": 1,
            "languages": [],
            "admins": [],
            "enforced_2fa": True,
            "members": ["admin"],
            "autogroups": ["^$"],
        },
    ]
    validate_schema(
        backup_with_teams,
        "weblate-backup.schema.json",
    )


def test_backup_blank_url():
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
                "web": "",
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


def test_backup_unicode_url():
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
                "web": "https://example.com/Tradução%20Divine%20Divinity",
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
    data = {
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
                "id": 1,
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
        "units": [
            {
                "translation_id": 10,
                "id_hash": "1234567890abcdef",
                "location": "",
                "context": "",
                "note": "",
                "flags": "",
                "source": "Source",
                "previous_source": "",
                "target": "Source",
                "state": 100,
                "original_state": 100,
                "details": {},
                "position": 1,
                "num_words": 1,
                "priority": 100,
                "pending": False,
                "timestamp": "2019-11-18T18:58:30.845Z",
                "extra_flags": "",
                "explanation": "",
                "labels": ["demo"],
                "comments": [
                    {
                        "comment": "Comment",
                        "user": "nijel",
                        "timestamp": "2019-11-18T18:58:30.845Z",
                        "resolved": False,
                    }
                ],
                "checks": [
                    {
                        "name": "end_stop",
                        "dismissed": False,
                    }
                ],
                "suggestions": [
                    {
                        "user": "nijel",
                        "target": "Sources",
                        "timestamp": "2019-11-18T18:58:30.845Z",
                        "votes": [{"user": "nijel", "value": 1}],
                    }
                ],
            }
        ],
        "screenshots": [
            {
                "name": "Test",
                "image": "test.png",
                "translation_id": 10,
                "units": ["1234567890abcdef"],
                "timestamp": "2019-11-18T18:58:30.845Z",
                "user": "nijel",
            }
        ],
    }
    validate_schema(
        data,
        "weblate-component.schema.json",
    )
    data["component"]["category"] = "my-category"
    validate_schema(
        data,
        "weblate-component.schema.json",
    )


merge_body = {
    "change_id": 1,
    "action": "Merged repository",
    "timestamp": "2017-06-15T11:30:47.325000+00:00",
    "url": "https://example.com/projects/test/test/",
    "component": "test",
}

new_string_body = {
    "change_id": 2,
    "action": "New source string",
    "timestamp": "2017-06-15T11:30:47.372000+00:00",
    "url": "https://example.com/translate/test/test/cs/?checksum=6412684aaf018e8e",
    "component": "test",
    "translation": "cs",
    "source": ["Hello, world!\n"],
}

new_translation_body = {
    "change_id": 12,
    "action": "New translation",
    "timestamp": "2019-10-17T15:57:08.772591+00:00",
    "url": "https://example.com/translate/test/test/cs/?checksum=6412684aaf018e8e",
    "target": ["Ahoj svete!\n"],
    "author": "testuser",
    "user": "testuser",
    "project": "test",
    "component": "test",
    "translation": "cs",
    "source": ["Hello, world!\n"],
}

resource_update_body = {
    "change_id": 6,
    "action": "Resource update",
    "timestamp": "2017-06-15T11:30:47.410000+00:00",
    "url": "https://example.com/projects/test/test/cs/",
    "project": "test",
    "component": "test",
    "translation": "cs",
}

removal_body = {
    "change_id": 9,
    "action": "Removed project",
    "timestamp": "2019-10-17T15:57:08.559420+00:00",
    "target": "test",
    "user": "testuser",
}

new_contributor_body = {
    "change_id": 11,
    "action": "New contributor",
    "timestamp": "2019-10-17T15:57:08.759960+00:00",
    "url": "https://example.com/translate/test/test/cs/?checksum=6412684aaf018e8e",
    "author": "testuser",
    "user": "testuser",
    "project": "test",
    "component": "test",
    "translation": "cs",
    "source": ["Hello, world!\n"],
}

invalid_body = {
    "change_id": 1,
    "action": "Merged repository",
    "timestamp": "invalid datetime",
    "url": "https://example.com/projects/test/test/",
    "component": "test",
}


def test_weblate_messaging_merge() -> None:
    """Test Weblate Messaging schema to validate a repository merge event."""
    validate_schema(merge_body, "weblate-messaging.schema.json")


def test_weblate_messaging_new_string() -> None:
    """Test Weblate Messaging schema to validate a new source string event."""
    validate_schema(new_string_body, "weblate-messaging.schema.json")


def test_weblate_messaging_resource_update() -> None:
    """Test Weblate Messaging schema to validate a resource update event."""
    validate_schema(resource_update_body, "weblate-messaging.schema.json")


def test_weblate_messaging_removal() -> None:
    """Test Weblate Messaging schema to validate a project removal event."""
    validate_schema(removal_body, "weblate-messaging.schema.json")


def test_weblate_messaging_new_contributor() -> None:
    """Test Weblate Messaging schema to validate a new contributor event."""
    validate_schema(new_contributor_body, "weblate-messaging.schema.json")


def test_weblate_messaging_new_translation() -> None:
    """Test Weblate Messaging schema to validate a new translation event."""
    validate_schema(new_translation_body, "weblate-messaging.schema.json")


def test_weblate_messaging_with_category() -> None:
    """Test Weblate Messaging schema to validate body with category field."""
    body = new_string_body.copy()
    body["category"] = ["category-1", "subcategory-1"]
    validate_schema(body, "weblate-messaging.schema.json")


def test_weblate_invalid_body() -> None:
    """Test Weblate Messaging schema to validate an invalid body."""
    is_invalid = False
    try:
        validate_schema(invalid_body, "weblate-messaging.schema.json")
    except ValidationError:
        is_invalid = True

    assert is_invalid
