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
# ARG CLEANING & STANDARDIZING
#####################################################################

@checks
def remove_special_characters(
        value: str) -> str:
    """
    Replace all the special characters in the argument by '_'. 
    """
    return re.sub(
        '\W+',
        '_',
        value)

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
    """Console script for wild."""
    click.echo("Replace this message by putting your code into "
               "wild.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")

if __name__ == "__main__":
    main()
