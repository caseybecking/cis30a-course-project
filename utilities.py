import random
import string

def generate_unique_id(length=8):
    """Generate a random unique identifier"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def sanitize_input(text):
    """Clean and validate user input"""
    return ''.join(char for char in text if char.isprintable())