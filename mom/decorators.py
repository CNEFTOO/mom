from typing import Callable

from .response import Response


def methods(*alloweds: str):
    allowed = [m.upper() for m in alloweds]

    def decorator(func: Callable):
        def wrapper(req, *args, **kwargs):
            if req.method not in allowed:
                return Response(f"Method {req.method} not allowed")
            return func(req, *args, **kwargs)

        return wrapper

    return decorator
