# -*- coding: utf-8 -*-

"""
==============
Data Wrangling
==============

Clean the raw data on vehicles, insurance, etc.
"""

from __future__ import absolute_import, division, print_function

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
