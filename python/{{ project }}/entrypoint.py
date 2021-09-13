#! /usr/local/bin/python
"""The main entrypoint for {{ project }}."""


def tonumber(x: str) -> float:
    return float(x)


def main() -> None:
    print(f"Hello from {{ project }}! Here's a number: { tonumber(22) }")  # fails mypy linting!


if __name__ == "__main__":
    main()
