#!/bin/bash
# Script sends a POST request
curl -X POST -s "$1" -d "$(cat $2)"
