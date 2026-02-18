import os
import sys

sys.path.append(os.path.abspath(".."))
from mom import MomApp, json_response, logger_middleware, methods

app = MomApp()
app.add_middleware(logger_middleware)


@app.route("/hello")
def hello(req):
    return "Hello, World!"


# 动态路由
@app.route("/user/<uid>")
def user(req, uid):
    return f"User ID: {uid}"


# JSON API
@app.route("/api/data")
@json_response
def api_data(req):
    return {"status": "ok", "items": [1, 2, 3]}


# POST 方法限制
@app.route("/submit")
@methods("POST")
def submit(req):
    return f"Received: {req.POST}"


if __name__ == "__main__":
    app.run(port=9527)
