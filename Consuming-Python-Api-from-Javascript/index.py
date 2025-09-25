import tornado.web
import tornado.ioloop
import json


class MainRequestHandler(tornado.web.RequestHandler):
    """Handles the root URL ('/') and sends a simple text response."""

    def get(self):
        self.render("index.html")


class FruitListApiHandler(tornado.web.RequestHandler):
    """
    Reads a list of fruits from 'list.txt' and returns them as a array.
    This version includes error handling for the missing file.
    """

    def get(self):
        fh = open("list.txt", "r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))

    def post(self):
        fh = open("list.txt", "a")
        fruit = self.get_argument("fruit", None)
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added successfully"}))


class uploadImgHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files["imgFile"]
        for f in files:
            fh = open(f"img/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
            self.write(f"http://localhost:8080/img/{f.filename}")

    def get(self):
        self.render("index.html")


if __name__ == "__main__":
    # The application routes map URLs to their respective handler classes.
    app = tornado.web.Application(
        [
            (r"/", MainRequestHandler),
            (r"/list", FruitListApiHandler),
            ("/", uploadImgHandler),
            ("/img/(.*)", tornado.web.StaticFileHandler, {"path": "img"}),
        ],
    )

    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on http://localhost:{port}")
    tornado.ioloop.IOLoop.current().start()
