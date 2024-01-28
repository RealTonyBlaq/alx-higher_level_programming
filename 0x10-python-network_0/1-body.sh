#!/bin/bash
# Script takes in a URL, sends a GET request to the URL, and displays the body of the response
if [ "$(curl -sI "$1" | head -n 1 | cut -d ' ' -f2)" -eq 200 ]; then curl -s -L "$1"; fi
