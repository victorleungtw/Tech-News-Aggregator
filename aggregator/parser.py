import urllib.parse

def sanitize_url(url: str) -> str:
    """Validates and sanitizes incoming RSS article URLs."""
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")

    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in ('http', 'https'):
        raise ValueError(f"Invalid URL scheme: {parsed.scheme}")

    if not parsed.netloc:
        raise ValueError("URL must contain a valid domain")

    return urllib.parse.urlunparse(parsed)
