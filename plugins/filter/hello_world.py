"""A hello-world filter plugin in EwenBara.krb5."""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


def _hello_world(name):
    """Returns Hello message."""
    return "Hello, " + name


class FilterModule:
    """filter plugin."""

    def filters(self):
        """filter plugin."""
        return {"hello_world": _hello_world}
