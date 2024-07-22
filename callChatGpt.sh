#!/bin/bash

echo ""
echo "Output will be piped through 'less -X'. Scroll through output using SPACE(forward), b(backward)"
echo "Press 'q' to return to the command prompt.  The current output will remain on the screen."
echo ""

script_location="/home/bschilke/Documents/development/LLMs/openai/cli-client/chatgpt-virtualenv/"

# Call the Python application with the arguments
python "${script_location}"src/callChatGpt.py "$*" | less -X

