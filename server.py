#!/bin/python 

import argparse
import sys

from http.server import HTTPServer, SimpleHTTPRequestHandler
from files import getFiles, getDirs
from html import ulify, nestedUlify

parser = argparse.ArgumentParser(
                    prog = 'Server',
                    description = 'Starts and Manages the python server',
                    epilog = 'u')

parser.add_argument('-a', '--addr', type=str, default='127.0.0.1')     # server host

parser.add_argument('-p', '--port', type=int, default=8000)     # server port


args = parser.parse_args()

def bindAddress(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):        
    global server_address
    server_address = (args.addr, int(args.port))

    global httpd
    try:
        httpd = server_class(server_address, handler_class)
    except OSError as e:
        print(f'error: {e}')
        exit()

def run():
    try:
        print(f'Sharing On http://{server_address[0]}:{server_address[1]}')
        httpd.serve_forever()
    except:
        print(sys.exc_info())
        exit()


bindAddress()

context = {
        "address": f'{server_address[0]}:{server_address[1]}',
        "directories": nestedUlify(getDirs(), parentClass='dirs', childClass='dir'),
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

