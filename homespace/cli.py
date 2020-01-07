# -*- coding: utf-8 -*-

"""
===
CLI
===

Console script.
"""

from __future__ import absolute_import, division, print_function

import re

import click

from typical import (
    anything,
    checks,
    iterable,
    numeric)

#####################################################################
# TRANSLATE TEXT VALUES INTO URL ARGS
#####################################################################

@checks
def translate_into_referential(
        value: str,
        referential: iterable) -> str:
    """
    Translate a random string into an item from a given referential.
    In particular this is meant to translate user input into url argument
    meaningful for the target website.

    The referential itself can either be:
    - a list
    - a dictionary

    The input value is matched with the closest item in the referential. 
    The distance used depends on the kind of data compared.
    """
    return value

#####################################################################
# CLI
#####################################################################

@click.command()
def main(args=None):
    """Console script for homespace."""
    click.echo("Replace this message by putting your code into "
               "homespace.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")

if __name__ == "__main__":
    main()
