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
# CLI
#####################################################################

@click.command()
def main(args=None):
    """
    An alternative to the scrapy shell / scrapy crawl.
    Allows to launch several scraping jobs at once.

    Parameters
    ----------
    args: None.
    
    Returns
    -------
    out: None.
    """
    click.echo("Replace this message by putting your code into "
               "homespace.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")

if __name__ == "__main__":
    main()
