import tornado.web
import tornado.ioloop
import json

# --- Handlers ---


class BasicRequestHandler(tornado.web.RequestHandler):
    """Handles the root URL ('/') and sends a simple text response."""

    def get(self):
        self.write("Hello World, this is a python command executed from the backend")


class AnimalPageHandler(tornado.web.RequestHandler):
    """Renders the index.html template."""

    def get(self):
        # This will look for an index.html file in the same directory.
        self.render("index.html")


class QueryParamRequestHandler(tornado.web.RequestHandler):
    """Handles query parameters to check if a number is even or odd."""

    def get(self):
        num = self.get_argument("num", None)  # Use a default value to avoid errors
        if num and num.isdigit():
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}")
        elif num is None:
            self.set_status(400)  # Bad Request
            self.write("Error: 'num' parameter is missing.")
        else:
            self.set_status(400)  # Bad Request
            self.write(f"Error: '{num}' is not a valid integer.")


class ResourceParamRequestHandler(tornado.web.RequestHandler):
    """Handles URL path parameters for student and course IDs."""

    def get(self, studentName, courseId):
        self.write(f"Welcome {studentName}, the course you are viewing is {courseId}")


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


if __name__ == "__main__":
    # The application routes map URLs to their respective handler classes.
    app = tornado.web.Application(
        [
            (r"/", BasicRequestHandler),
            (r"/animal", AnimalPageHandler),
            (r"/isEven", QueryParamRequestHandler),
            (r"/students/([a-z]+)/([0-9]+)", ResourceParamRequestHandler),
            (r"/list", FruitListApiHandler),
        ],
    )

    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on http://localhost:{port}")
    tornado.ioloop.IOLoop.current().start()
