import tornado.web
import tornado.ioloop


class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World, this is a python command exectued from the backend")


class ListRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class QueryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if num.isdigit():
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer{num} is {r}")
        else:
            self.write(f"{num} is not a number")


class ResourceRaramRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseId):
        self.write(f"Welcome {studentName} the course you are viewing is {courseId}")


if __name__ == "__main__":
    app = tornado.web.Application(
        [
            (r"/", BasicRequestHandler),
            (r"/animal", ListRequestHandler),
            (r"/isEven", QueryParamRequestHandler),
            (r"/students/([a-z]+)/([0-9]+)", ResourceRaramRequestHandler),
        ]
    )

    port = 8882
    app.listen(port)
    print(f"Application is ready listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
