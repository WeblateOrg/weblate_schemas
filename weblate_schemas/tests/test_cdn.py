# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Validate CDN and Kotlin SDK contracts against publisher examples."""

from typing import Any

import pytest
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError

from weblate_schemas import load_schema, validate_schema

CDN = "weblate-cdn-manifest.schema.json"
BUILD = "weblate-kotlin-sdk-build.schema.json"
KOTLIN = "weblate-kotlin-sdk-manifest.schema.json"
DIGEST = "a" * 64


@pytest.fixture(params=[CDN, BUILD, KOTLIN])
def schema_name(request: pytest.FixtureRequest) -> str:
    """Select each published contract."""
    return request.param


@pytest.fixture
def data(schema_name: str) -> dict[str, Any]:
    """Provide representative valid publisher or registration data."""
    if schema_name == BUILD:
        return {
            "packageName": "org.weblate.sample",
            "versionCode": 1,
            "strings": {"hello": "0x7f090003"},
        }
    descriptor = {
        "url": "cs.json" if schema_name == CDN else f"../../artifacts/{DIGEST}.arsc",
        "sha256": DIGEST,
        "size": 123,
    }
    result: dict[str, Any] = {
        "schemaVersion": 1,
        "locales": {"cs": [descriptor] if schema_name == CDN else descriptor},
    }
    if schema_name == KOTLIN:
        result.update(packageName="org.weblate.sample", versionCode=1)
    return result


def test_schema(schema_name: str, data: dict[str, Any]) -> None:
    """Check schemas themselves and representative valid documents."""
    Draft202012Validator.check_schema(load_schema(schema_name))
    validate_schema(data, schema_name)


def test_required_fields(schema_name: str, data: dict[str, Any]) -> None:
    """Reject documents missing each required field."""
    for field in load_schema(schema_name)["required"]:
        with pytest.raises(ValidationError):
            validate_schema(
                {key: value for key, value in data.items() if key != field}, schema_name
            )


@pytest.mark.parametrize("change", [{"schemaVersion": 2}, {"unknown": True}])
def test_unknown_fields_and_versions(
    schema_name: str, data: dict[str, Any], change: dict[str, Any]
) -> None:
    """Reject unsupported contract versions and extra fields."""
    with pytest.raises(ValidationError):
        validate_schema(data | change, schema_name)


@pytest.mark.parametrize("schema_name", [BUILD, KOTLIN])
@pytest.mark.parametrize(
    "change",
    [
        {"packageName": "org." + "a" * 123, "versionCode": 2100000000},
        {"packageName": "a.b", "versionCode": 1},
    ],
)
def test_android_boundaries(
    schema_name: str, data: dict[str, Any], change: dict[str, Any]
) -> None:
    """Accept Android package and version boundaries."""
    validate_schema(data | change, schema_name)


@pytest.mark.parametrize("schema_name", [BUILD, KOTLIN])
@pytest.mark.parametrize(
    "change",
    [
        {"packageName": "org." + "a" * 124},
        {"packageName": "sample"},
        {"packageName": "1org.sample"},
        {"packageName": "org.sample\n"},
        {"versionCode": 0},
        {"versionCode": 2100000001},
        {"versionCode": 1.5},
        {"versionCode": "1"},
        {"versionCode": True},
    ],
)
def test_invalid_android_metadata(
    schema_name: str, data: dict[str, Any], change: dict[str, Any]
) -> None:
    """Reject invalid Android package names and version codes."""
    with pytest.raises(ValidationError):
        validate_schema(data | change, schema_name)


@pytest.mark.parametrize("kind", ["strings", "plurals"])
def test_build_optional_fields(kind: str) -> None:
    """Accept either resource kind and omitted optional metadata."""
    data = {
        "packageName": "org.weblate.sample",
        "versionCode": 1,
        kind: {"_hello.world": "0x7FAb0001"},
    }
    validate_schema(data, BUILD)
    validate_schema(data | {"schemaVersion": 1}, BUILD)
    other = "plurals" if kind == "strings" else "strings"
    validate_schema(data | {other: {}}, BUILD)


@pytest.mark.parametrize(
    "resources",
    [
        {},
        {"strings": {}, "plurals": {}},
        {"strings": []},
        {"strings": {"": "0x7f090003"}},
        {"strings": {"bad/name": "0x7f090003"}},
        {"plurals": {"hello\n": "0x7f090003"}},
        {"strings": {"hello": "0x80090003"}},
        {"strings": {"hello": "0x7f000003"}},
        {"strings": {"hello": "0x7f090003\n"}},
        {"plurals": {"hello": 2131296259}},
    ],
)
def test_invalid_build_resources(resources: dict[str, Any]) -> None:
    """Require resources with valid Android names and app resource IDs."""
    with pytest.raises(ValidationError):
        validate_schema(
            {"packageName": "org.weblate.sample", "versionCode": 1} | resources,
            BUILD,
        )


def test_cdn_multifile() -> None:
    """Accept nested and encoded file URLs, including empty published files."""
    validate_schema(
        {
            "schemaVersion": 1,
            "locales": {
                "cs": [
                    {"url": "cs/messages.json", "sha256": DIGEST, "size": 123},
                    {"url": "cs/nested/empty%20file.json", "sha256": DIGEST, "size": 0},
                ],
                "pt_BR": [{"url": "pt_BR.json", "sha256": DIGEST, "size": 12}],
            },
        },
        CDN,
    )


@pytest.mark.parametrize("schema_name", [CDN, KOTLIN])
def test_empty_locales(schema_name: str, data: dict[str, Any]) -> None:
    """Allow publications with no translation files."""
    validate_schema(data | {"locales": {}}, schema_name)


@pytest.mark.parametrize("schema_name", [CDN, KOTLIN])
@pytest.mark.parametrize("locales", [[], None, {"": []}, {"cs": []}, {"cs": "file"}])
def test_invalid_locales(
    schema_name: str, data: dict[str, Any], locales: object
) -> None:
    """Reject invalid language mappings and empty file lists."""
    with pytest.raises(ValidationError):
        validate_schema(data | {"locales": locales}, schema_name)


@pytest.mark.parametrize("schema_name", [CDN, KOTLIN])
@pytest.mark.parametrize(
    "change",
    [
        {"url": ""},
        {"url": None},
        {"sha256": "a" * 63},
        {"sha256": "a" * 65},
        {"sha256": "A" * 64},
        {"sha256": DIGEST + "\n"},
        {"size": -1},
        {"size": 1.5},
        {"size": True},
        {"size": "123"},
        {"unknown": True},
    ],
)
def test_invalid_descriptors(
    schema_name: str, data: dict[str, Any], change: dict[str, Any]
) -> None:
    """Reject malformed file descriptors for both publication formats."""
    descriptor = data["locales"]["cs"]
    if schema_name == CDN:
        descriptor = descriptor[0]
    invalid = descriptor | change
    with pytest.raises(ValidationError):
        validate_schema(
            data | {"locales": {"cs": [invalid] if schema_name == CDN else invalid}},
            schema_name,
        )


@pytest.mark.parametrize("schema_name", [CDN, KOTLIN])
def test_descriptor_fields_and_shape(schema_name: str, data: dict[str, Any]) -> None:
    """Require descriptor fields and distinguish lists from single artifacts."""
    descriptor = data["locales"]["cs"]
    wrong_shape = descriptor[0] if schema_name == CDN else [descriptor]
    with pytest.raises(ValidationError):
        validate_schema(data | {"locales": {"cs": wrong_shape}}, schema_name)
    if schema_name == CDN:
        descriptor = descriptor[0]
    for field in ("url", "sha256", "size"):
        invalid = {key: value for key, value in descriptor.items() if key != field}
        with pytest.raises(ValidationError):
            validate_schema(
                data
                | {"locales": {"cs": [invalid] if schema_name == CDN else invalid}},
                schema_name,
            )
