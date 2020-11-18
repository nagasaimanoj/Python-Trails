from abc import ABC # no idea why, but tornado warns if we dont inherit this
from json import dumps # to convert dict obj to json

from tornado.escape import json_decode # to convert request into dict or easy access
from tornado.gen import coroutine # not clear, but i think this is to make parallel processing with each request
from tornado.httpserver import HTTPServer # to start server, obviously
from tornado.ioloop import IOLoop # not clear
from tornado.web import Application, RequestHandler # these are the main things. App and the base class with remaining functions we wont see


class DimExtractServer(RequestHandler, ABC):
    @coroutine
    def post(self):
        # reading the resuest
        data_json = json_decode(self.request.body)
        url = data_json['url']

        # actual logic
        data_to_return = dict(url=url)

        # returning the response
        self.write(dumps(data_to_return))
        self.finish()


def start_server(server_route, server_port):
    # tornado can start multiple routes. so we have to map each class with its route. see the list we are sending to Application()
    app = Application([
        (server_route, DimExtractServer)
    ])

    # once all the classes are mapped, we will start HTTP server and expose a port
    http_server = HTTPServer(app)
    http_server.listen(server_port)
    print('server started at port = {}'.format(server_port))

    # I really want to know what this is, I will add this to my todo list
    ioloop = IOLoop.instance()
    ioloop.start()

if __name__ == '__main__':
    # I wanted to run the server on demand and automatic. so i made it as a function. usually we wont write as function
    start_server(server_route='/', server_port=1234)
