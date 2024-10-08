# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Message class implementation for Weblate Fedora Messaging."""

from datetime import datetime

from weblate_schemas import load_schema
from fedora_messaging import message


class BaseMessage(message.Message):
    """Inherit the Message class from fedora_messaging."""

    def __init__(self, **kwargs) -> None:
        """Initialize BaseMessage class."""
        super().__init__(**kwargs)

    @property
    def app_name(self) -> str:
        """Return the app name."""
        return "Weblate"

    @property
    def app_icon(self) -> str:
        """Return the App icon URL."""
        return "https://weblate.org/static/weblate-128.png"


class WeblateMessage(BaseMessage):
    """Actual Weblate message class which uses the Messaging schema."""

    def __init__(self, **kwargs) -> None:
        """Initialize the WeblateMessage class with loading of the body_schema."""
        super().__init__(**kwargs)
        self.body_schema = load_schema("weblate-messaging.schema.json")

    @property
    def agent_name(self) -> str:
        """The username who cause the action."""
        return self.body["user"]

    @property
    def id(self) -> int:
        """Return the change ID."""
        return self.body["id"]

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
        return self.body["target"]

    @property
    def old(self) -> str | list[str]:
        """Return the old value of the change."""
        return self.body["old"]

    @property
    def source(self) -> str | list[str]:
        """Return the source string."""
        return self.body["source"]

    @property
    def url(self) -> str:
        """Return the URL to the related object."""
        return self.body["url"]

    @property
    def author(self) -> str:
        """Return the author username."""
        return self.body["author"]

    @property
    def user(self) -> str:
        """Return the acting username."""
        return self.body["user"]

    @property
    def project(self) -> str:
        """Return the project slug."""
        return self.body["project"]

    @property
    def component(self) -> str:
        """Return the component slug."""
        return self.body["component"]

    @property
    def translation(self) -> str:
        """Return the translation language code."""
        return self.body["translation"]

    def __str__(self) -> str:
        """Return a human-readable representation of the message."""
        return f"{self.action} {self.timestamp}"
