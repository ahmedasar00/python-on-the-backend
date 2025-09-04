import tornado.web
import tornado.ioloop


class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World, this is a python command exectued from the backend")


class ListRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


if __name__ == "__main__":
    app = tornado.web.Application(
        [
            (r"/", BasicRequestHandler),
            (r"/animal", ListRequestHandler),
        ]
    )

    port = 8882
    app.listen(port)
    print(f"Application is ready listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
