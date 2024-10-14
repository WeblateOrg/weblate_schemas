# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Test the Message classes."""

from weblate_schemas.messages import WeblateV1Message
from weblate_schemas.tests.test_valid import (
    merge_body,
    new_string_body,
    new_translation_body,
)


def test_base_message() -> None:
    """Test Message class."""
    base_message = WeblateV1Message(topic="test.topic", body=merge_body)
    assert base_message.app_name == "Weblate"
    assert base_message.app_icon == "https://weblate.org/static/weblate-128.png"


def test_weblate_merge_message() -> None:
    """Test WeblateV1Message class with a merge event message body."""
    weblate_message = WeblateV1Message(topic="test.topic", body=merge_body)
    assert weblate_message.app_name == "Weblate"
    assert weblate_message.app_icon == "https://weblate.org/static/weblate-128.png"
    assert weblate_message.change_id == merge_body["change_id"]
    assert weblate_message.action == merge_body["action"]
    assert weblate_message.timestamp == merge_body["timestamp"]
    assert weblate_message.url == merge_body["url"]
    assert weblate_message.component == merge_body["component"]
    assert (
        weblate_message.summary
        == "Merged repository event occurred in 2017-06-15T11:30:47.325000+00:00."
    )


def test_weblate_new_string_message() -> None:
    """Test WeblateV1Message class with a new string event message body."""
    weblate_message = WeblateV1Message(topic="test.topic", body=new_string_body)
    assert weblate_message.change_id == new_string_body["change_id"]
    assert weblate_message.action == new_string_body["action"]
    assert weblate_message.timestamp == new_string_body["timestamp"]
    assert weblate_message.url == new_string_body["url"]
    assert weblate_message.component == new_string_body["component"]
    assert weblate_message.translation == new_string_body["translation"]
    assert weblate_message.source == new_string_body["source"]
    assert (
        weblate_message.summary
        == "New source string event occurred in 2017-06-15T11:30:47.372000+00:00."
    )


def test_weblate_new_translation_message() -> None:
    """Test WeblateV1Message class with a new translation event message body."""
    weblate_message = WeblateV1Message(topic="test.topic", body=new_translation_body)
    assert weblate_message.change_id == new_translation_body["change_id"]
    assert weblate_message.action == new_translation_body["action"]
    assert weblate_message.timestamp == new_translation_body["timestamp"]
    assert weblate_message.url == new_translation_body["url"]
    assert weblate_message.target == new_translation_body["target"]
    assert weblate_message.author == new_translation_body["author"]
    assert weblate_message.user == new_translation_body["user"]
    assert weblate_message.project == new_translation_body["project"]
    assert weblate_message.component == new_translation_body["component"]
    assert weblate_message.translation == new_translation_body["translation"]
    assert weblate_message.source == new_translation_body["source"]
    assert weblate_message.usernames == ["testuser"]
    assert (
        weblate_message.summary == "New translation event done by testuser occurred "
        "in 2019-10-17T15:57:08.772591+00:00."
    )
