# -*- coding: utf-8 -*-

"""
==============
Data Wrangling
==============

Make the data exploitable.
"""

from __future__ import absolute_import, division, print_function

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
