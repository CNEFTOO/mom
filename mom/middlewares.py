from typing import Callable, Iterable
from wsgiref.types import StartResponse, WSGIEnvironment

WSGIApp = Callable[[WSGIEnvironment, StartResponse], Iterable[bytes]]


def logger_middleware(app: WSGIApp) -> WSGIApp:
    def wrapper(environ: WSGIEnvironment, start_response: StartResponse):
        return app(environ, start_response)

    return wrapper
