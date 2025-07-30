#!/bin/bash

# Instap Box Download and Run Script
# This script downloads the project from GitHub as ZIP, extracts it, and runs the application

set -e  # Exit on any error

echo "=== Instap Box Download and Run Script ==="
echo ""

# Configuration
GITHUB_REPO="Instap7/instap-box"
GITHUB_TOKEN="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"  # GitHub Personal Access Token
GITHUB_URL="https://github.com/$GITHUB_REPO/archive/main.zip"
TEMP_DIR="/tmp/instap-box-download"
EXTRACT_DIR="$TEMP_DIR/instap-box-main"

# Check if a custom URL or local file was provided
if [ $# -ge 1 ] && [ "$1" = "--url" ] && [ $# -ge 2 ]; then
    GITHUB_URL="$2"
    shift 2
    echo "Using custom URL: $GITHUB_URL"
elif [ $# -ge 1 ] && [ "$1" = "--file" ] && [ $# -ge 2 ]; then
    LOCAL_FILE="$2"
    shift 2
    echo "Using local file: $LOCAL_FILE"
    if [ ! -f "$LOCAL_FILE" ]; then
        echo "Error: Local file '$LOCAL_FILE' not found"
        exit 1
    fi
fi

echo "Repository: $GITHUB_REPO"
echo "Download URL: $GITHUB_URL"
echo ""

# Create temporary directory
echo "Creating temporary directory..."
rm -rf "$TEMP_DIR"
mkdir -p "$TEMP_DIR"
cd "$TEMP_DIR"

# Download the ZIP file
echo "Downloading project from GitHub..."
DOWNLOAD_SUCCESS=false

if command -v curl >/dev/null 2>&1; then
    echo "Trying to download with curl..."
    if [ -n "$GITHUB_TOKEN" ]; then
        echo "Using GitHub token for authentication..."
        if curl -H "Authorization: token $GITHUB_TOKEN" -L -o instap-box.zip "$GITHUB_URL" 2>/dev/null; then
            DOWNLOAD_SUCCESS=true
        fi
    else
        if curl -L -o instap-box.zip "$GITHUB_URL" 2>/dev/null; then
            DOWNLOAD_SUCCESS=true
        fi
    fi
elif command -v wget >/dev/null 2>&1; then
    echo "Trying to download with wget..."
    if [ -n "$GITHUB_TOKEN" ]; then
        echo "Using GitHub token for authentication..."
        if wget --header="Authorization: token $GITHUB_TOKEN" -O instap-box.zip "$GITHUB_URL" 2>/dev/null; then
            DOWNLOAD_SUCCESS=true
        fi
    else
        if wget -O instap-box.zip "$GITHUB_URL" 2>/dev/null; then
            DOWNLOAD_SUCCESS=true
        fi
    fi
else
    echo "Error: Neither curl nor wget is available. Please install one of them."
    exit 1
fi

# Check if download was successful
if [ "$DOWNLOAD_SUCCESS" = false ] || [ ! -f instap-box.zip ] || [ ! -s instap-box.zip ]; then
    echo "Error: Failed to download the ZIP file from GitHub"
    echo ""
    echo "Possible reasons:"
    echo "1. The repository is private and requires authentication"
    echo "2. The repository doesn't exist publicly"
    echo "3. Network connectivity issues"
    echo ""
    echo "To fix authentication issues:"
    echo "1. Create a GitHub Personal Access Token:"
    echo "   - Go to GitHub.com -> Settings -> Developer settings -> Personal access tokens"
    echo "   - Generate new token with 'repo' permissions"
    echo "2. Set the token as environment variable:"
    echo "   export GITHUB_TOKEN=your_token_here"
    echo "3. Or run the script with token:"
    echo "   GITHUB_TOKEN=your_token_here ./run_download.sh"
    exit 1
fi

echo "Download completed successfully!"
echo ""

# Extract the ZIP file
echo "Extracting ZIP file..."
if command -v unzip >/dev/null 2>&1; then
    unzip -q instap-box.zip
elif command -v bsdtar >/dev/null 2>&1; then
    bsdtar -xf instap-box.zip
else
    echo "Error: Neither unzip nor bsdtar is available. Please install one of them."
    exit 1
fi

# Check if extraction was successful
if [ ! -d "$EXTRACT_DIR" ]; then
    echo "Error: Failed to extract the ZIP file"
    exit 1
fi

echo "Extraction completed successfully!"
echo ""

# Navigate to the extracted directory
echo "Navigating to project directory..."
cd "$EXTRACT_DIR"

# Check if run.sh exists
if [ ! -f run.sh ]; then
    echo "Error: run.sh not found in the extracted project"
    echo "Contents of current directory:"
    ls -la
    exit 1
fi

# Make run.sh executable
echo "Making run.sh executable..."
chmod +x run.sh

echo "=== Ready to run Instap Box ==="
echo "Current directory: $(pwd)"
echo ""

# Check if any arguments were provided
if [ $# -ge 1 ]; then
    echo "Running with arguments: $@"
    ./run.sh "$@"
else
    echo "No arguments provided. run.sh will check for INSTAP_BOX environment variable."
    echo "You can run with arguments like: ./run_download.sh --instap-box my-box"
    echo ""
    ./run.sh
fi

echo ""
echo "=== Script completed ===" 