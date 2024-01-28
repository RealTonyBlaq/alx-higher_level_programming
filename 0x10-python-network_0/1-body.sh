#!/bin/bash
# Script takes in a URL, sends a GET request to the URL, and displays the body of the response
status_code="$(curl -sI "$1" | head -n 1 | awk '{print $2}')"