#!/usr/bin/env bash
name=$1
if [ -n "$name" ]; then
    echo "One for $name, one for me."
else
    echo "One for you, one for me."
fi