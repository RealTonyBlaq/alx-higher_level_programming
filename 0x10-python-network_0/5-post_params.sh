#!/bin/bash
# Script takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -X POST "email=test@gmail.com&" -s "$1"
