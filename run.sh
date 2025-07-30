#!/bin/bash

# Instap Box Runner Script
# This script sets up the environment and runs the Instap Box application

echo "Starting Instap Box application..."

# Check if any arguments were provided
if [ $# -ge 1 ]; then
    # Pass all arguments to the Python script
    echo "Running with arguments: $@"
    python3 main.py "$@"
else
    # No argument provided, check environment variable
    if [ -z "$INSTAP_BOX" ]; then
        echo "Error: No INSTAP_BOX value provided"
        echo "Usage: ./run.sh [OPTIONS] --instap-box INSTAP_BOX_VALUE"
        echo "Or set environment variable: export INSTAP_BOX=VALUE"
        echo "Or run: INSTAP_BOX=VALUE ./run.sh"
        exit 1
    fi
    
    # Use environment variable as INSTAP_BOX value
    echo "Using environment variable as INSTAP_BOX value: $INSTAP_BOX"
    python3 main.py --instap-box "$INSTAP_BOX"
fi 