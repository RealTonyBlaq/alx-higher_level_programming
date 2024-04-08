#!/bin/bash
# Force a server's hand to respond with "You got me!"
curl -s -L 0.0.0.0:5000/catch_me -H "Origin:HolbertonSchool"
