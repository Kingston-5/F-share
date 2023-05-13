#!/bin/python 

import argparse

from http.server import HTTPServer, SimpleHTTPRequestHandler

parser = argparse.ArgumentParser(
                    prog = 'Server',
                    description = 'Starts and Manages the python server',
                    epilog = 'u')

parser.add_argument('-a', '--addr')     # server host

parser.add_argument('-p', '--port')     # server port


args = parser.parse_args()
print(args.addr, args.port)

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    if args.addr is None and args.port is not None:     # only port was specified
        server_address = ('', int(args.port))
    if args.addr is not None and args.port is None:     # only addr was specified
        server_address = (args.addr, '')
    if args.addr is not None and args.port is not None:     # both addr and port were specified
        server_address = (args.addr, int(args.port))
    else:
        server_address = ('', 8000)     #neither addr or port were specified
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

from functools import partial


class ExampleHandler(SimpleHTTPRequestHandler):
    def __init__(self, foo, bar, qux, *args, **kwargs):
        self.foo = foo
        self.bar = bar
        self.qux = qux
        # BaseHTTPRequestHandler calls do_GET **inside** __init__ !!!
        # So we have to call super().__init__ after setting attributes.
        super().__init__(*args, **kwargs)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        self.do_HEAD()
        self.wfile.write('<h1>{!r} {!r} {!r}<h1>\n'
                         .format(self.foo, self.bar, self.qux)
                         .encode('utf8'))



context = {
    "invoice_number": "12345",
    "date": "2023-04-25",
    "customer_name": "John Doe",
    "total": 85,
}

with open("index.tmp.html", "r") as file:
    html = file.read().format(**context)

with open("index.html", "w") as file:
    file.write(html)

# We "partially apply" the first three arguments to the ExampleHandler
#handler = partial(ExampleHandler, args.addr, args.port, 'hey')
# .. then pass it to HTTPHandler as normal:
#server = HTTPServer(('', 8000), handler)
#server.serve_forever()

run()
#ip=$(ip addr show scope global up | grep -E inet | cut -c 10-24)

#echo python3 -m http.server -b ${ip} 55555

