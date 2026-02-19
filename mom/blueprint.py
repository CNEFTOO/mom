from typing import Any, Callable, List, TypeVar

from .app import MomApp

F = TypeVar("F", bound=Callable[..., Any])


class Blueprint:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.routes: List = []

    def route(self, path: str) -> Callable[[F], F]:
        """路由装饰器
        path: str -> 路由请求路径
        return: Callable[[F], F] -> 一个可调用个的函数对象

        示例:
            @app.route("/hello")
            def send(req):
                return "hello"
        """

        def decorator(func) -> F:
            self.routes.append((path, func))
            return func

        return decorator

    def register(self, app: MomApp, prefix: str = "") -> None:
        """注册路由
        app: MomApp -> MomApp实例
        prefix: str -> 路由前缀
        return: None
        """
        for path, func in self.routes:
            app.router.add_route(prefix + path, func)
