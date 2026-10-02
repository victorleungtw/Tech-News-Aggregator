import pytest
from hypothesis import given, strategies as st
from hypothesis.provisional import urls
from aggregator.parser import sanitize_url

@given(st.text())
def test_sanitize_url_rejects_invalid_text(random_text):
    """Ensure arbitrary non-URL text is rejected."""
    # Skip randomly generated text that accidentally starts with valid HTTP schemes
    if random_text.startswith("http://") or random_text.startswith("https://"):
        return

    with pytest.raises(ValueError):
        sanitize_url(random_text)

@given(urls())
def test_sanitize_url_handles_valid_urls(url):
    """Ensure valid HTTP/HTTPS URLs are processed, and others are rejected."""
    # Hypothesis generates many schemes (ftp, mailto, wss, etc.)
    # Our function is strictly designed for HTTP and HTTPS
    if url.startswith("http://") or url.startswith("https://"):
        assert sanitize_url(url) == url
    else:
        # Non-HTTP URLs must raise our custom ValueError
        with pytest.raises(ValueError):
            sanitize_url(url)
