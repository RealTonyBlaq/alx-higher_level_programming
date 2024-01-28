#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Send a request using curl and display the size of the response body
body_size=$(curl -sI "$url" | grep -i '^Content-Length:' | awk '{print $2}' | tr -d '\r')


