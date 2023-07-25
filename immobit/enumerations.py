"""Common enumerations."""

from enum import Enum


__all__ = ["Action"]


class Action(Enum):
    """Possible openimmo actions."""

    CREATE = "CREATE"
    REPLACE = "REPLACE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
