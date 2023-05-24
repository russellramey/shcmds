import json
import shcmds_sys as shcSYS

# Read file as lines
def readFileLines(file):
    if(os.path.exists(file) is False):
        with open(file, "r") as f:
            lines = f.readlines()
            return lines 
    return False

# Search file for specific line
def findLinesFromFile(target, file, exact=False):
    found = []
    lines = readFileLines(file)
    if lines is not False:
        for line in enumerate(lines):
            if target in line:
                found.append(formatLine(line))
        return found
    return False
        
# Parse line from test to object
# Line format: alias aliasname="command string" #Comment text here
def formatLine(line: str=None):
    return line

# Convert file text to json
def textToJson(data: str=None):
    return

# Convert json to text
def jsonToText(data: list=None):
    return