#!/bin/bash

# Instap Box Runner Script
# This script sets up the environment and runs the Instap Box application

echo "Starting Instap Box application..."

# Check if a command line argument was provided
if [ $# -eq 1 ]; then
    # Use the provided argument as INSTAP_BOX value
    echo "Using provided argument as INSTAP_BOX value: $1"
    python3 main.py --instap-box "$1"
elif [ $# -gt 1 ]; then
    echo "Error: Too many arguments. Usage: ./run.sh [INSTAP_BOX_VALUE]"
    echo "Or set environment variable: export INSTAP_BOX=VALUE"
    exit 1
else
    # No argument provided, check environment variable
    if [ -z "$INSTAP_BOX" ]; then
        echo "Error: No INSTAP_BOX value provided"
        echo "Usage: ./run.sh INSTAP_BOX_VALUE"
        echo "Or set environment variable: export INSTAP_BOX=VALUE"
        echo "Or run: INSTAP_BOX=VALUE ./run.sh"
        exit 1
    fi
    
    # Use environment variable as INSTAP_BOX value
    echo "Using environment variable as INSTAP_BOX value: $INSTAP_BOX"
    python3 main.py --instap-box "$INSTAP_BOX"
fi 