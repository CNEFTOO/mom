import json
from typing import Iterable, List, Tuple
from wsgiref.types import StartResponse


class Response:
    def __init__(
        self,
        body: str | bytes,
        status: str = "200 OK",
        headers: List[Tuple[str, str]] | None = None,
    ) -> None:

        if isinstance(body, str):
            self.body: bytes = body.encode("utf-8")
        else:
            self.body = body

        self.status = status
        self.headers = headers or [("Content-Type", "text/plain")]

    def __call__(self, start_response: StartResponse) -> Iterable[bytes]:
        start_response(self.status, self.headers)
        return [self.body]


def json_response(func):
    def wrapper(*args, **kwargs) -> Response:
        result = func(*args, **kwargs)
        body = json.dumps(result)
        return Response(body, headers=[("Content-Type", "application/json")])

    return wrapper
