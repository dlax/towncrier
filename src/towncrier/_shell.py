# Copyright (c) Stephen Finucane, 2019
# See LICENSE for details.

"""
towncrier, a builder for your news files.
"""

import click
from click_default_group import DefaultGroup

from .build import _main as _build_cmd
from .check import _main as _check_cmd


@click.group(cls=DefaultGroup, default="build", default_if_no_args=True)
def cli():
    pass


cli.add_command(_build_cmd)
cli.add_command(_check_cmd)
