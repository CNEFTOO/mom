class Blueprint:
    def __init__(self, name):
        self.name = name
        self.routes = []

    def route(self, path):
        def decorator(func):
            self.routes.append((path, func))
            return func

        return decorator

    def register(self, app, prefix=""):
        for path, func in self.routes:
            app.router.add_route(prefix + path, func)
