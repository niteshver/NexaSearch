import hashlib
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from src.config.settings import settings


def sha256(text: str) -> str:

    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


TRACKING_PARAMS = {
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "gclid",
    "fbclid",
}


def canonicalize_url(url: str) -> str:
    """
    Normalize URLs so equivalent URLs map to one canonical form.
    """
    parts = urlsplit(url)

    scheme = parts.scheme.lower()
    netloc = parts.netloc.lower()

    if netloc.endswith(":80") and scheme == "http":
        netloc = netloc[:-3]

    if netloc.endswith(":443") and scheme == "https":
        netloc = netloc[:-4]

    path = parts.path or "/"

    if path != "/" and path.endswith("/"):
        path = path[:-1]

    query = urlencode(
        sorted(
            (k, v)
            for k, v in parse_qsl(parts.query, keep_blank_values=True)
            if k not in TRACKING_PARAMS
        )
    )

    return urlunsplit((scheme, netloc, path, query, ""))

# Create directory paths
data_dir = settings.absolute_db_path.parent
index_dir = settings.absolute_index_dir

for directory in [
    data_dir,
    data_dir / "raw",
    data_dir / "raw/markdown",
    data_dir / "raw/json",
    data_dir / "raw/sitemap",
    index_dir,
]:
    directory.mkdir(parents=True, exist_ok=True)
