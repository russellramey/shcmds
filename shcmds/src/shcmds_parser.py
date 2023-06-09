import json
from . import shcmds_sys as shcSYS

# Read file as lines
def readFileLines(filepath):
    # if Filepath exists
    if(shcSYS.fileExists(filepath)):
        # Open file
        with open(filepath, "r") as f:
            # Read lines in file
            lines = f.readlines()
            return lines 
    # Return 
    return False

# Search file for specific line
def findLinesFromFile(target, filepath, exact=False):
    # Empty list
    found = []
    # Readlines from file
    lines = readFileLines(filepath)
    # If lines exists
    if lines is not False:
        # Foreach line
        for line in lines:
            # Format line into list
            line = formatLine(line.strip())
            # Check if target is in the list
            if exact:
                if target == line[0]:
                    found = line
            else:
                if target in line[0]:
                    found.append(line)
    # If found, return
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

# Truncate string
# Shorten a string if the max len is longer than desired
# Automatically append elipsis (...)
def truncateString(string, maxLen):
    if len(string) > maxLen:
        string = string[0:maxLen] + '...'
    return string

# Convert file text to json
def textToJson(data=None):
    # Empty list
    jsonData = []
    # Check to make sure data exists
    if data is not None:
        # Loop thorugh data
        for item in data:
            # Convert string to list
            item = formatLine(item.strip())
            # Append dict to list
            jsonData.append({
                'name':item[0],
                'command':item[1],
                'desc':item[2]
            })
        # Return list as json
        return json.dumps(jsonData)
    # Return
    return False

# Convert json to text
def jsonToText(data=None):
    # Empty list
    lines = []
    # Convert dat to json
    data = json.loads(data)
    # Loop thru data and build text lines
    for item in data:
        line = f"alias shc-{item['name']}='{item['command']}' #{item['desc']}"
        # Append line to list
        lines.append(line)
    # Return lines
    return lines