import pytest
from hypothesis import given, strategies as st
from aggregator.parser import sanitize_url

@given(st.text())
def test_sanitize_url_rejects_invalid_text(random_text):
    """Ensure arbitrary non-URL text is rejected."""
    # If the random text happens to be a valid HTTP/HTTPS url, skip
    if random_text.startswith("http://") or random_text.startswith("https://"):
        return

    with pytest.raises(ValueError):
        sanitize_url(random_text)

@given(st.urls())
def test_sanitize_url_handles_valid_urls(url):
    """Ensure valid URLs are processed successfully."""
    if url.startswith("http://") or url.startswith("https://"):
        assert sanitize_url(url) == url
