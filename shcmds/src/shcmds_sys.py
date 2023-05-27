#
# Dependencies
#
import os

#
# Datastor path
# Returns file path to datastore file for this module:
# default: /usr/local/lib/ptyhonX.X/site-packages/shcmds/src/.shcdata
#
def getDatastorePath():
    # Return path to data file
    return os.path.abspath(os.path.join(__file__, os.pardir)) + "/.shcdata"

#
# Shell type
# Returns current shell environment type
#
def getShellType():
    return os.environ['SHELL']

#
# Current Directory
# Returns current working directory form shell
#
def getCurrentDir():
    return os.getcwd()

#
# File Exists
# simply checks to see if a filepath exists
#
def fileExists(filepath):
    if(os.path.exists(filepath) is not False):
        return True
    return False

#
# Shell file path
# Try to get the current shell profile filepath
#
def getShellProfilePath():
    try:
        # Get shell type
        shell = getShellType()
        # User home dir
        home = os.path.expanduser('~')
        # Default profile
        filepath = home + '/.profile'
        # Zsh Shell
        if 'zsh' in shell:
            filepath = home + '/.zprofile'
            if fileExists(filepath) is False:
                filepath = home + '/.zshrc'
        # Bash Shell
        if 'bash' in shell:
            filepath = home + '/.bash_profile'
            if fileExists(filepath) is False:
                filepath = home + '/.profile'
        # Return path
        return filepath
    except Exception as e:
        print('Shell profile error:')
        print(e)
        return False