#!/bin/bash
# Script sends a POST request
curl -X POST -s "$1" -H "Content-Type: application/"-d @$2
