import json
import os

# Read file as lines
def readFileLines(filepath):
    found = []
    if(os.path.exists(filepath) is not False):
        with open(filepath, "r") as f:
            lines = f.readlines()
            return lines 
    return False

# Search file for specific line
def findLinesFromFile(target, filepath, exact=False):
    found = []
    lines = readFileLines(filepath)
    if lines is not False:
        for line in lines:
            line = formatLine(line)
            if target in line[0]:
                found.append(line)
    if found and found is not None:
        return found 
    else:
        return False
        
# Parse line from test to object
# Line format: alias shc-aliasname="command string here" #Comment text here
def formatLine(line: str=None):
    # Split at 'alias'
    line = line.split('alias ')[1]
    # Split at # to isolate alias=command from comment
    line = line.split(' #')
    # Split at first found = sign to isolate aliasname from command
    line[0] = line[0].split('=', 1)
    # Set new attributes
    alias = line[0][0]
    command = line[0][1]
    comment = line[1]
    # Return list
    return [alias.replace('shc-', ''), command[1:-1], comment]

# Convert file text to json
def textToJson(data: str=None):
    return

# Convert json to text
def jsonToText(data: list=None):
    return