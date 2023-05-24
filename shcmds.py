import src.shcmds_parser as shcPARSE
import src.shcmds_sys as shcSYS
import json
import prettytable

class shcmds:

    # 
    # Defined constants
    # 
    SHELL_PROFILE_PATH = shcSYS.getShellProfilePath()
    SHELL_TYPE = shcSYS.getShellType()
    DATASTORE_PATH = shcSYS.getDatastorePath()
    DATASTORE_DATA = shcPARSE.readFileLines(DATASTORE_PATH)

    #
    # Class constructor
    #
    def __init__(self):
        pass

    #
    # Add alias
    #
    def _add(self, args):
        # Build data object
        data = { "name": args.NAME, "command": args.COMMAND, "desc": args.desc }
        # Search for existing shortcut name
        if shcPARSE.findLinesFromFile(args.NAME, self.DATASTORE_PATH, True) is False:
            try:
                # Write data to datastore
                shcSYS.saveToDatastore(data)
                # Print result
                print(f"New alias saved: {data['name']}")
                # Reload config for shell
                shcSYS.reloadShell()
            except Exception as e:
                print(f"Error trying to save alias: {data['name']}")
                print(e)
        else:
            print(f"Alias `{data['name']}` already exists")

    #
    # List command
    #
    def _list(self, args):
        # Try to execute
        try:
            # Read lines of file
            lines = self.DATASTORE_DATA
            # Configure output 
            table = prettytable.PrettyTable()
            table.align = 'l'
            table.field_names = ["Name", "Runs command", "Description"]
            # If NAME is not None
            if args.NAME:
                lines = shcPARSE.findLinesFromFile(args.NAME, self.DATASTORE_PATH)
            # For each line in file
            for line in lines:
                if args.NAME is None:
                    # Format line as list, strip() new line characters
                    line = shcPARSE.formatLine(line.strip())
                # Add a new table row with values
                table.add_row([
                    line[0], #name
                    line[1], #command
                    line[2], #desc
                ])
            # Print out table
            print("\nTo use a Shorthand Command alias, simply call: shc-NAME\n")
            print(table)

        # Catch exceptions
        except Exception as e:
            print('Error listing aliases.')
            print(e)

    #
    # Remove command
    #
    def _remove(self, args):
        try:
            # Set filepath to data
            filepath = shcSYS.getDatastorePath()
            # See if args.NAME exists in file
            target = shcPARSE.findLinesFromFile(args.NAME, self.DATASTORE_PATH, True)
            # If target exists
            if target is not False:
                # Open file
                with open(self.DATASTORE_PATH, 'w') as f:
                    # For each line in datastore
                    for line in self.DATASTORE_DATA:
                        # Format line as list, strip() new line characters
                        item = shcPARSE.formatLine(line.strip())
                        if target[0] != item[0]:
                            f.write(line)
                    # Print message
                    print(f"Removed alias: `{args.NAME}`")
            else:
                # Print error
                print(f"Alias: `{args.NAME}` was not found.")
        
        # Catch exception
        except Exception as e:
            print(f"Error trying to remove alias: `{args.NAME}`")
            print(e) 

    #
    # Export command
    #
    def _export(self, args):
        print("Export method")
        return

    #
    # Import command
    #
    def _import(self, args):
        print("Import method")
        return