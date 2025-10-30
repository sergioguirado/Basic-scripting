#!/bin/bash

FOLDER="data"
OUTPUT="python-exercises/cleaned.csv"

python3 process-data.py "$FOLDER" "$OUTPUT"
