from typing import Callable, Iterable, List
from wsgiref.simple_server import make_server
from wsgiref.types import StartResponse, WSGIEnvironment

from .request import Request
from .response import Response
from .router import Router
from .static import serve_static

WSGIApp = Callable[[WSGIEnvironment, StartResponse], Iterable[bytes]]


class MomApp:
    def __init__(self) -> None:
        self.router: Router = Router()
        self.middlewares: List[Callable[[WSGIApp], WSGIApp]] = []

    def route(self, path: str) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.router.add_route(path, func)
            return func

        return decorator

    def add_middleware(self, middlewares: Callable[[WSGIApp], WSGIApp]) -> None:
        self.middlewares.append(middlewares)

    def wsgi_app(
        self, environ: WSGIEnvironment, start_response: StartResponse
    ) -> Iterable[bytes]:

        req = Request(environ)

        if req.path.startswith("/static/"):
            return serve_static(req, start_response)

        func, kwargs = self.router.match_routers(req.path)

        if func:
            result = func(req, **kwargs)
            if isinstance(result, Response):
                response = result
            else:
                response = Response(result)
        else:
            response = Response("404 Not Found", status="404 Not Found")

        return response(start_response)

    def __call__(
        self, environ: WSGIEnvironment, start_response: StartResponse
    ) -> Iterable[bytes]:

        app: WSGIApp = self.wsgi_app
        for middleware in reversed(self.middlewares):
            app = middleware(app)

        return app(environ, start_response)

    def run(self, host: str = "127.0.0.1", port: int = 9527) -> None:
        print(f"Running on http://{host}:{port}")
        server = make_server(host, port, self)
        server.serve_forever()
