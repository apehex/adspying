from __future__ import absolute_import, division, print_function

"""Data cleaning tools."""

#####################################################################
# ENCODING & FORMAT
#####################################################################

def convert_unicode_to_lower_string(unicode_bytes):
    """Convert a unicode byte object to a standard string.

    Args:
        unicode_bytes (unicode): text, as a byte string.

    Returns:
        str: text in lower case, as a standard python str type.
    """
    return unicode_bytes.encode('utf-8', 'ignore').lower()
