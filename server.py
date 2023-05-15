#!/bin/python 

import argparse

from http.server import HTTPServer, SimpleHTTPRequestHandler
from files import getFiles, getDirs
from html import ulify, nestedUlify

parser = argparse.ArgumentParser(
                    prog = 'Server',
                    description = 'Starts and Manages the python server',
                    epilog = 'u')

parser.add_argument('-a', '--addr')     # server host

parser.add_argument('-p', '--port')     # server port


args = parser.parse_args()


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

    try:
        print(f'Sharing On http://{server_address[0]}:{server_address[1]}')
        httpd.serve_forever()
    except:
        print(sys.exc_info())
        exit()


context = {
    "directories": nestedUlify(getDirs()),
    "files": ulify(getFiles())
}

def generate(filename, context):
    with open(f'./templates/{filename}.tmp', "r") as file:
        html = file.read().format(**context)

    with open(f'{filename}.html', "w") as file:
        file.write(html)

generate('index', context)
run()
#ip=$(ip addr show scope global up | grep -E inet | cut -c 10-24)

#echo python3 -m http.server -b ${ip} 55555

