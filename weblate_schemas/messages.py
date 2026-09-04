# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Message class implementation for Weblate Fedora Messaging."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeAlias

from fedora_messaging import message

from . import load_schema

MessageData: TypeAlias = dict[str, Any]

if TYPE_CHECKING:
    from pika import BasicProperties


class BaseMessage(message.Message):
    """Inherit the Message class from fedora_messaging."""

    @property
    def app_name(self) -> str:
        """Application name."""
        return "Weblate"

    @property
    def app_icon(self) -> str:
        """Application icon URL."""
        return "https://weblate.org/static/weblate-128.png"


class WeblateV1Message(BaseMessage):
    """Actual Weblate message class which uses the Messaging schema."""

    def __init__(
        self,
        body: MessageData | None = None,
        headers: MessageData | None = None,
        topic: str | None = None,
        properties: BasicProperties | None = None,
        severity: int | None = None,
    ) -> None:
        """Initialize the WeblateMessage class with loading of the body_schema."""
        super().__init__(
            body=body,
            headers=headers,
            topic=topic,
            properties=properties,
            severity=severity,
        )
        # Assign through the class to satisfy Fedora Messaging's ClassVar annotation
        # while keeping schema loading lazy until a message is instantiated.
        type(self).body_schema = load_schema("weblate-messaging.schema.json")

    @property
    def agent_name(self) -> str | None:
        """The username who caused the action."""
        return self.body.get("user")

    @property
    def change_id(self) -> int:
        """Change ID."""
        return self.body["change_id"]

    @property
    def action(self) -> str:
        """Change verbose name."""
        return self.body["action"]

    @property
    def timestamp(self) -> str:
        """Timestamp of the change."""
        return self.body["timestamp"]

    @property
    def target(self) -> str | list[str] | None:
        """New value of the change."""
        return self.body.get("target")

    @property
    def old(self) -> str | list[str] | None:
        """Old value of the change."""
        return self.body.get("old")

    @property
    def source(self) -> str | list[str] | None:
        """Source string."""
        return self.body.get("source")

    @property
    def url(self) -> str | None:
        """URL to the related object."""
        return self.body.get("url")

    @property
    def author(self) -> str | None:
        """Author username."""
        return self.body.get("author")

    @property
    def user(self) -> str | None:
        """Acting username."""
        return self.body.get("user")

    @property
    def project(self) -> str | None:
        """Project slug."""
        return self.body.get("project")

    @property
    def component(self) -> str | None:
        """Component slug."""
        return self.body.get("component")

    @property
    def translation(self) -> str | None:
        """Translation language code."""
        return self.body.get("translation")

    @property
    def summary(self) -> str:
        """Message summary."""
        user = f" done by {self.user}" if self.user else ""
        return f"{self.action} event{user} occurred in {self.timestamp}."

    @property
    def usernames(self) -> list[str]:
        """Usernames involved."""
        return sorted({name for name in (self.author, self.user) if name})

    @property
    def context(self) -> str | None:
        """Context of the translation."""
        return self.body.get("context")

    def __str__(self) -> str:
        """Return a human-readable representation of the message."""
        return f"{self.summary}"
