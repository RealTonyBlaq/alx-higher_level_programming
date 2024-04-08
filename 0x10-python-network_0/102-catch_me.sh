#!/bin/bash
# Force a server's hand to respond with "You got me!"
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
