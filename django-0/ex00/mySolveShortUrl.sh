#!/bin/bash

output=$(curl -sI $1 | grep Location | cut -d ' ' -f 2)

echo "$output"
