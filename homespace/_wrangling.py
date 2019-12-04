# -*- coding: utf-8 -*-

"""
==============
Data Wrangling
==============

Clean the raw data scraped from the web.
"""

from __future__ import absolute_import, division, print_function

from bs4 import BeautifulSoup
from nltk.metrics.distance import edit_distance
import numpy as np
import re

from typical import checks

#####################################################################
# ENCODING & FORMAT
#####################################################################

@checks
def convert_unicode_to_lower_string(
        unicode_bytes: str) -> str:
    """Convert a unicode byte object to a standard string.

    Args:
        unicode_bytes (unicode): text, as a byte string.

    Returns:
        str: text in lower case, as a standard python str type.
    """
    return unicode_bytes.encode('utf-8', 'ignore').lower()

def format_text(unicode_bytes):
    formatted_text = unicode_bytes.encode('utf-8', 'ignore')
    formatted_text = formatted_text.strip()
    formatted_text = formatted_text.lower()
    return formatted_text

def format_number(unicode_bytes):
    formatted_number = format_text(unicode_bytes)
    number_matches = re.search('([-+]?[0-9]*\.?[0-9]+).*', formatted_number)
    if number_matches:
        formatted_number = number_matches.group(1)
    else:
        formatted_number = np.nan
    formatted_number = np.float64(formatted_number)
    return formatted_number

#####################################################################
# TRANSLATION
#####################################################################

def string_distance(s1, s2):
    distance = edit_distance(s1, s2)
    distance -= abs(len(s1) - len(s2))
    return distance

def find_closest_reference(value, references):
    distances = [
        edit_distance(
            s1=value,
            s2=ref,
            substitution_cost=2)
        for ref in references]
    min_index = np.argmin(distances)
    closest_reference = references[min_index]
    return closest_reference

#####################################################################
# TEXT
#####################################################################

@checks
def remove_extra_spacing(
        text: str) -> str:
    """
    Replace any spacing by a single whitspace.
    """
    return ' '.join(text.split())

#####################################################################
# HTML
#####################################################################

@checks
def extract_text_from_html_markup(
        html:str) -> str:
    """
    Extract the text *visible* to a user on an internet browser,
    from a string of html markup.
    The chunks of text are separated by newlines.

    Parameters
    ----------
    html: str.
        A string of html markup soup.
    Returns
    -------
    out: str.
        The visible text.
    """
    __soup = BeautifulSoup(markup=html, features="lxml")

    # kill all script and style elements
    for script in __soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    __text = __soup.get_text(separator='.')

    # break into lines and remove leading and trailing space on each
    __lines = (
        __line.strip()
        for __line in __text.splitlines())
    # break multi-headlines into a line each
    __chunks = (
        __phrase.strip()
        for __line in __lines
        for __phrase in __line.split("."))
    # drop blank lines
    return '\n'.join(
        __chunk
        for __chunk in __chunks if __chunk)

@checks
def prettify_html(
        html: str) -> str:
    """
    Expand the html markup formatting:
    - break lines on opening tags
    - indent lines

    Parameters
    ----------
    html: str.
        A string of html markup soup.
    Returns
    -------
    out: str.
        The beautified html.
    """
    return BeautifulSoup(
        markup=html,
        features="lxml").prettify().encode('utf-8')
