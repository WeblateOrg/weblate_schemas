# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Message class implementation for Weblate Fedora Messaging."""

from __future__ import annotations

from __future__ import annotations
from datetime import datetime

from . import load_schema
from fedora_messaging import message


class BaseMessage(message.Message):
    """Inherit the Message class from fedora_messaging."""

    @property
    def app_name(self) -> str:
        """Return the app name."""
        return "Weblate"

    @property
    def app_icon(self) -> str:
        """Return the App icon URL."""
        return "https://weblate.org/static/weblate-128.png"


class WeblateV1Message(BaseMessage):
    """Actual Weblate message class which uses the Messaging schema."""

    def __init__(self, **kwargs) -> None:
        """Initialize the WeblateMessage class with loading of the body_schema."""
        super().__init__(**kwargs)
        self.body_schema = load_schema("weblate-messaging.schema.json")

    @property
    def agent_name(self) -> str:
        """The username who cause the action."""
        return self.body.get("user")

    @property
    def change_id(self) -> int:
        """Return the change ID."""
        return self.body["change_id"]

    @property
    def action(self) -> str:
        """Return the change verbose name."""
        return self.body["action"]

    @property
    def timestamp(self) -> datetime:
        """Return the timestamp of the change."""
        return self.body["timestamp"]

    @property
    def target(self) -> str | list[str]:
        """Return the new value of the change."""
        return self.body.get("target")

    @property
    def old(self) -> str | list[str]:
        """Return the old value of the change."""
        return self.body.get("old")

    @property
    def source(self) -> str | list[str]:
        """Return the source string."""
        return self.body.get("source")

    @property
    def url(self) -> str:
        """Return the URL to the related object."""
        return self.body.get("url")

    @property
    def author(self) -> str:
        """Return the author username."""
        return self.body.get("author")

    @property
    def user(self) -> str:
        """Return the acting username."""
        return self.body.get("user")

    @property
    def project(self) -> str:
        """Return the project slug."""
        return self.body.get("project")

    @property
    def component(self) -> str:
        """Return the component slug."""
        return self.body.get("component")

    @property
    def translation(self) -> str:
        """Return the translation language code."""
        return self.body.get("translation")

    @property
    def summary(self) -> str:
        """Return the message summary."""
        user = f" done by {self.user}" if self.user else ""
        return f"{self.action} event{user} occurred in {self.timestamp}."

    @property
    def usernames(self) -> list[str]:
        """Return the usernames involved."""
        return sorted({name for name in (self.author, self.user) if name})

    def __str__(self) -> str:
        """Return a human-readable representation of the message."""
        return f"{self.summary}"
