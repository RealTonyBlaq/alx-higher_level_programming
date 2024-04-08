#!/bin/bash
# Script shows only the status code from an HTTP response
curl -s -o /dev/null -w "%{http_code}" "$1"
