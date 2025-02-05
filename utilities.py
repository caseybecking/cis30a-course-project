# pylint: disable=missing-docstring
# custom module

def sanitize_input(text):
    """Clean and validate user input"""
    return ''.join(char for char in text if char.isprintable())
