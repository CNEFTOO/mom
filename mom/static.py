import os

from .response import Response


def serve_static(request, start_response):
    file_path = "." + request.path
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            content = f.read()
        start_response("200 OK", [("Content-Type", "text/css")])
        return [content]
    else:
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"File not found"]
