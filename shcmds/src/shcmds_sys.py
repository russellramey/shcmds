import os
import subprocess

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
        print('Shell Profile error: ' + e)
        return False

def reloadShell():
    shell = getShellType()
    if 'zsh' in shell:
        subprocess.run(shell + '; source ~/.zshrc', shell=True)
    if 'bash' in shell:
        subprocess.run(shell + '; source ~/.bashrc', shell=True)
    return True

def getShellType():
    return os.environ['SHELL']

def saveToDatastore(data):
    line = f"alias shc-{data['name']}='{data['command']}' #{data['desc']}"
    with open(getDatastorePath(), 'a') as f:
        f.write(line + '\n')
        f.close()

def install():
    shellpath = getShellProfilePath()
    datapath = getDatastorePath()
    try:
        with open(shellpath, "a") as f:
            f.write('source ' + datapath + '\n')
            f.close()
        return True
    except Exception as e:
        print('Install error: ' + e)
        return False

def uninstall():
    shellpath = getShellProfilePath()
    datapath = getDatastorePath()
    try:
        with open(shellpath, "r") as f:
            lines = f.readlines()
        with open(shellpath, "w") as f:
            for line in lines:
                if datapath not in line:
                    f.write(line)
            f.close()
        return True
    except Exception as e:
        print('Uninstall error: ' + e)
        return False

def getCurrentDir():
    return os.getcwd()

def fileExists(filepath):
    if(os.path.exists(filepath) is not False):
        return True
    return False