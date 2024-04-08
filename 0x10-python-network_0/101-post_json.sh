#!/bin/bash
# Script sends a POST request
curl -X POST "$1" -d "$(cat $2)"
