#!/bin/bash


ip=$(ip addr show scope global up | grep -E inet | cut -c 10-24)

echo python3 -m http.server -b ${ip} 55555
