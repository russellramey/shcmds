import os

def getDatastorePath():
    return os.path.abspath(os.path.join(__file__, os.pardir)) + "/.shcdata"
        
def getShellProfilePath():
    shell = getShellType()
    try:
        if 'zsh' in shell:
            file = os.path.expanduser( '~' ) + '/.zshrc'
        if 'bash' in shell:
            file = os.path.expanduser( '~' ) + '/.bashrc'
        return file
    except Exception as e:
        print('Shell Profile error:')
        print(e)
        return False

def getShellType():
    return os.environ['SHELL']

def getCurrentDir():
    return os.getcwd()

def fileExists(filepath):
    if(os.path.exists(filepath) is not False):
        return True
    return False