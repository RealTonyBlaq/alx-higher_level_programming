#!/usr/bin/env bash
# Script takes in a URL, sends a request to that URL,
#+ and displays the size of the body of the response

if [ "$#" -eq 1 ]; then
    curl -i -X GET "$1" | grep "Content-Length: "
fi
