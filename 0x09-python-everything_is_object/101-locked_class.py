#!/usr/bin/python3
"""Defines a class LockedClass"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes

    Attributes:
        first_name (str): first name
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creating a new instances of Locked Class."""

        self.first_name = "first_name"
