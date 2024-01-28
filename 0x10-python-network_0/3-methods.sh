#!/bin/bash
# Script takes in a URL and displays all HTTP methods the server will accept.
curl -I  "$1"
