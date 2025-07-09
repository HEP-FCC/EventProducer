#!/bin/bash

# This script authenticates the user, then uploads a single JSON dictionary
# to the FCC Physics Events API.
# Usage: ./upload_fcc_dicts.sh /path/to/your/file.json

# --- Configuration ---
API_ENDPOINT="https://fcc-physics-events-backend.web.cern.ch/authorized/upload-fcc-dict"

# --- Argument Validation ---
if [ "$#" -ne 1 ]; then
    echo "❌ Error: Incorrect number of arguments."
    echo "Usage: $0 /path/to/your/file.json"
    exit 1
fi

JSON_FILE="$1"

if [ ! -f "$JSON_FILE" ]; then
    echo "❌ Error: File not found at '$JSON_FILE'"
    exit 1
fi

# --- Authentication ---
echo "▶️  Requesting authentication token..."
auth-get-user-token -c fcc-physics-events-web -a webframeworks-paas-fcc-physics-events -o token.txt -x

if [ ! -f "token.txt" ]; then
    echo "❌ Authentication failed. Token file not created."
    exit 1
fi

token=$(<token.txt)
rm token.txt

if [ -z "$token" ]; then
    echo "❌ Failed to read token from file."
    exit 1
fi

echo "✅ Authentication successful."

# --- File Upload ---
echo "▶️  Uploading file: '$JSON_FILE' to $API_ENDPOINT"

response=$(curl -s -w "\nHTTP_STATUS:%{http_code}" \
     -X POST \
     -H "Authorization: Bearer $token" \
     -F "file=@$JSON_FILE;type=application/json" \
     "$API_ENDPOINT")

# Extract the body and status code from the response
http_body=$(echo "$response" | sed '$d')
http_status=$(echo "$response" | tail -n1 | cut -d: -f2)

if [ "$http_status" -ge 200 ] && [ "$http_status" -lt 300 ]; then
    echo "✅ SUCCESS: Server responded with status $http_status."
    echo "   Response: $http_body"
else
    echo "❌ FAILURE: Server responded with status $http_status."
    echo "   Response: $http_body"
fi

echo "✅ Script finished."
