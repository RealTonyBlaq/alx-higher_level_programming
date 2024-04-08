#!/bin/bash
# Force a server's hand to respond with "You got me!"
curl -X PUT -sL 0.0.0.0:5000/catch_me -H "Origin:HolbertonSchool"
