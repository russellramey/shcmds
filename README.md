# Shorthand Commands (shcmds)
A simple CLI utility that lets you easily create and manage command aliases for your specific shell environemnt. Currently supports **`zsh`** and **`bash`** shell environments.

### How it works
This CLI tool allows you to easily create naitve shell `aliases` with a simple command line interface. These aliases get written to a data file and that file is then added to your shell profile as a `source` include.
Everytime you add/remove an alias, the CLI tool will reload your shell profile config. No more having to manually edit your shell profile files to add or remove aliases. SHCMDS aliases are also global, once the shell profile is reloaded aliases will work globallay. 

Alias names can be what ever you want them to be. They will automatically be prefixed with `shc-` to avoid conflicts with any existing aliases you may have.

### Available commands
This CLI provides simple commands to manage your shell aliases.
- `shc add NAME COMMAND [-d | --desc] "string"` - Add new alias
- `shc remove NAME` - Remove alias by name
- `shc list` - List all available aliases
- `shc export FILEPATH [-fn | --filename] "string"` - Export alias data (json)
- `shc import FILEPATH` - Import alias data (json)

### Use an alias
To use an alias, just simply call the **`shc-NAME`**. For example, say you created an alias to print out your hosts file: `shc add hosts "cat /etc/hosts" -d "some description"`. To invoke that alias, you would only need to call `shc-hosts`.

### Local build/install
```bash
python3 -m build
```

```bash
pip3 install dist/WHEEL_FILE --force-reinstall
```