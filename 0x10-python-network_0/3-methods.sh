#!/bin/bash
# curl
curl -sI  "$1" | sed -n '/Allow: /s/Allow: //p'
