#!/bin/bash

echo ""
echo "output will be provided in less -X format, so scroll thorugh output using SPACE, b"
echo "press q when done (output displayed will remain in the screen)"
echo ""

# Call the Python application with the arguments
python src/callChatGpt.py "$*" | less -X


