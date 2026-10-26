# Repository Guidelines

## Project Structure & Module Organization

`weblate_schemas/` contains the Python schema-loading, validation, and messaging APIs. Packaged JSON schemas live in `weblate_schemas/schemas/`; pytest tests live in `weblate_schemas/tests/`. Packaging and tool configuration are in `pyproject.toml`. `README.rst` introduces the package, `CHANGES.rst` records releases, and `scripts/` contains release tooling.

## Build, Test, and Development Commands

- `uv sync --dev`: install the package and development dependencies; Python 3.10 or newer is required.
- `uv run pytest`: run tests with coverage enabled by default.
- `uv run pytest weblate_schemas/tests/test_valid.py`: run schema-validation tests.
- `uv run prek run --all-files`: run configured formatting, linting, licensing, and file checks.
- `uv run ty check`: check Python types.
- `uv build`: build source and wheel distributions.

This is a library; no application server or database setup is required.

## Coding Style & Naming Conventions

Use four spaces for Python and two for JSON/YAML, with UTF-8, LF endings, and final newlines. Follow configured Ruff formatting and linting. Prefer `prek` for Ruff checks because Ruff is provided through hook environments.

Use descriptive `snake_case` functions, `PascalCase` classes, type hints, and `from __future__ import annotations` in new Python modules. Use `TYPE_CHECKING` imports when appropriate. Prefer human-readable Ruff rule names in overrides. Name schemas `weblate-<purpose>.schema.json`. Preserve existing copyright and MIT SPDX headers in Python files.

## Testing Guidelines

Name test modules `test_*.py` and functions `test_<behavior>`. Cover accepted payloads and malformed inputs when changing schemas; use `pytest.raises(ValidationError)` for rejection cases. Keep schema changes consistent with Weblate exports and consumers. User-data schemas should cover exported profile fields while excluding internal database identifiers and user relations.

CI tests Python 3.10–3.15 and reports coverage; no minimum coverage percentage is configured.

## Commit & Pull Request Guidelines

Use Conventional Commits: `<type>(<optional scope>): <description>`, such as `fix(validation): reject malformed timestamps`. Explain motivation in the body and add `Fixes #123` when applicable.

Keep pull requests focused. Describe changed behavior, link relevant issues, add regression tests, and update documentation when behavior changes. Ensure tests, type checks, and pre-commit checks pass.
