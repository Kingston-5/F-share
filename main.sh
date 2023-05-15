#!/bin/bash

echo "[1] - Run Setup"
echo "[2] - Start Server"


while true; do
    read -p "> " choice
    case $choice in
        1 ) ./scripts/setup.sh;;
        2 ) ./scripts/run.sh;;
    esac
done

exit

