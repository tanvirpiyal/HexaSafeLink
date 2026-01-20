from urllib.parse import urlparse

def parse_url(url: str):
    try:
        if not url.startswith(("http://", "https://")):
            return None

        parsed = urlparse(url)

        return {
            "scheme": parsed.scheme,
            "domain": parsed.netloc,
            "path": parsed.path or "/"
        }

    except Exception:
        return None
