import re
from typing import Any, Callable, Dict, List, Pattern, Tuple


class Router:
    def __init__(self) -> None:
        self.routers: List[Tuple[Pattern[str], Callable]] = []

    def add_route(self, path: str, func: Callable) -> None:
        """添加路由
        path: str -> 路由路径
        func: Callable -> 具体的请求处理方法
        return: None
        """
        pattern_str = re.sub(r"<(\w+)>", r"(?P<\1>[^/]+)", path)
        pattern_str = f"^{pattern_str}$"
        pattern = re.compile(pattern_str)
        self.routers.append((pattern, func))

    def match_routers(self, path: str) -> Tuple[Callable | None, Dict[str, Any]]:
        """匹配路由
        path: str -> 匹配路径
        return: 元组对象
        """
        for pattern, func in self.routers:
            match = pattern.match(path)
            if match:
                return func, match.groupdict()
        return None, {}
