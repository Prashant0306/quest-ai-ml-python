# utils/strings.py  ->  a module inside the 'utils' package

def format_box(text):
    """Wrap text in a decorative box of '=' lines."""
    line = "=" * 10
    return f"{line}\n{text}\n{line}"


def shout(text):
    return text.upper() + "!"
