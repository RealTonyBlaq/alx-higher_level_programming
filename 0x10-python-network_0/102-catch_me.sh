#!/bin/bash
# Force a server's hand to respond with "You got me!"
curl -X POST -s -H "X-Custom-Header: You got me!" 0.0.0.0:5000/catch_me
