# Shorthand Commands (shcmds)
A simple CLI utility that lets you easily create and manage command aliases for your specific shell environment. Currently supports **`zsh`** and **`bash`** shell environments.

### How it works
This CLI tool allows you to easily create naitve shell `aliases` with a simple command line interface. These aliases get written to a data file and that file is then added to your shell profile as a `source` include.
Everytime you add/remove an alias, the CLI tool will reload your shell profile config. No more having to manually edit your shell profile files to add or remove aliases. SHCMDS aliases are also global, once the shell profile is reloaded aliases will work globallay. 

Alias names can be what ever you want them to be. They will automatically be prefixed with `shc-` to avoid conflicts with any existing aliases you may have.

### Available commands
This CLI provides simple commands to manage your shell aliases.
- `shc add NAME COMMAND` - Add new shorthand command
- `shc remove NAME` - Remove shorthand command by name
- `shc list` - List all available shorthand commands
- `shc export FILEPATH` - Export shorthand command data (json)
- `shc import FILEPATH` - Import shorthand command data (json)

#### Add shorthand command
**Usage**: `shc add NAME COMMAND [-d | --desc] "string" [-f | --force]`  
Add a new shorthand command.
##### Arguments
- **NAME**: Name of shorthand command.
- **COMMAND**: Command to run on invocation, complex commands require proper nesting or escaping of quotes.
##### Options
- **-d | --desc**: Description of command to run.
- **-f | --force**: If shorthand command name already exists, replace with new data.

#### Remove shorthand command
**Usage**: `shc remove NAME`  
Remove an existing shorthand command.
##### Arguments
- **NAME**: Name of shorthand command.

#### List shorthand commands
**Usage**: `shc list [-s | --search] NAME`  
List shorthand commands.
##### Options
- **-s | --search**: Search all shorthand commands by name, limits results in list to matching or similar names.

#### Export shorthand command data
**Usage**: `shc export FILEPATH [-o | --output] "FILENAME"`  
Export all shorthand command data as a JSON file.
##### Arguments
- **PATH**: Filepath location to save file.
##### Options
- **-o | --output**: Filename for generated file

#### Import shortand command data
**Usage**: `shc import FILEPATH`  
Import shorthand command data as JSON.
##### Arguments
- **PATH**: Complete filepath (with filename) to valid JSON file.

### Use an alias
To use an alias, just simply call the **`shc-NAME`**. For example, say you created an alias to print out your hosts file: `shc add hosts "cat /etc/hosts" -d "some description"`. To invoke that alias, you would only need to call `shc-hosts`.

### Trouble shooting
If an added alias fails to run and you recieve a `command not found` error. You can manually reload your shell profile in your current session with `source ~/.{PROFILE_FILE_NAME}`. Or you can simply open a new shell session.

If you do not use `zsh` or `bash` you could still use this CLI tool. You will just need to add the `.schdata` filepath (see below) to your shell profile.

### Filesystem
This CLI tool will attempt to modify your existing shell profile, by appending a single line to include the `.shcdata` file that stores your created aliases. The `.shcdata` file can be found on unix systems at: `/usr/local/lib/pythonX.X/site-packages/shcmds/src/.shcdata`.

### Local build/install
Build the python module:  
`python3 -m build`

Install the module globally:  
`pip3 install dist/WHEEL_FILE --force-reinstall`