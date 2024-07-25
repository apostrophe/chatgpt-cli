## chatgpt-cli
A simple python script, called from the command line, avoiding the extra effort to open a new browser tab to query an LLM.

Features
* No quotes are required, you can just enter something like `c whats the command to update pacman`
* I copy the bash script to /usr/local/bin as the command `c`, to keep the command as simple as possible
* Response is piped to `less -X` so that you can scroll through the longer responses, and also keep the output in the terminal as you enter the next command

### to run
```
[general,chatgpt in python] $ c what are the largest 3 lakes in canada?
--------------------------------------------------------------------------------
The largest three lakes in Canada are:

1. Lake Superior
2. Lake Huron
3. Great Bear Lake
--------------------------------------------------------------------------------
```

### to deploy
```
sudo cp callChatGpt.sh /usr/local/bin/c
sudo chown bschilke /usr/local/bin/c
```

### test deployment
```
pushd ~
c test
```
