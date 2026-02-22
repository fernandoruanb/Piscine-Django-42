#!/bin/sh

'''
	That script receives an URL from BitLy and identify the real target consulting
	directly the BitLy server and get the Location header
'''

output=$(curl -sI $1 | grep Location | cut -d ' ' -f 2)

echo "$output"
