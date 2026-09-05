import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from blog import app  # noqa: E402

# Vercel's Python runtime looks for a WSGI-compatible `app` object.
