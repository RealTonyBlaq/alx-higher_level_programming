#!/bin/bash
# Check if a URL is provided as an argument

if [ "$#" -eq 1 ]; then
    url="$1"
    # Send a request using curl and display the size of the response body
    body_size=$(curl -sI "$url" | grep -i '^Content-Length:' | awk '{print $2}' | tr -d '\r')
    echo "$body_size"
fi
