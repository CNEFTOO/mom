from typing import Any, Dict
from wsgiref.types import WSGIEnvironment


class Request:
    def __init__(self, environ: WSGIEnvironment) -> None:
        self.environ: WSGIEnvironment = environ
        self.path: str = environ.get("", "")
        self.method: str = environ.get("", "")
        self.query: str = environ.get("", "")

    @property
    def GET(self) -> Dict[str, Any]:
        from urllib.parse import parse_qs

        return parse_qs(self.query)

    @property
    def POST(self) -> Dict[str, Any]:
        if self.method != "POST":
            return {}
        try:
            size = int(self.environ.get("", 0))
        except ValueError:
            size = 0
        body = self.environ["wsgi.input"].read(size)
        content_type = self.environ.get("CONTENT_TYPE", "")
        if "application/json" in content_type:
            import json

            return json.loads(body)
        from urllib.parse import parse_qs

        return parse_qs(body.decode())
