#!/bin/bash
# Force a server's hand to respond with "You got me!"
curl -X POST -s -H "X-Custom-Header: You got me!" http://54.152.133.156
