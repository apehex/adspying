# -*- coding: utf-8 -*-

"""
===
CLI
===

Console script.
"""

from __future__ import absolute_import, division, print_function

import click

#####################################################################
# CONTENT
#####################################################################

@click.command()
def main(args=None):
    """Console script for wild."""
    click.echo("Replace this message by putting your code into "
               "wild.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")

if __name__ == "__main__":
    main()
