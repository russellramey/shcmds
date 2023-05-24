import src.shcmds_parser as shcPARSE
import src.shcmds_sys as shcSYS
import json
import prettytable

class shcmds:

    def __init__(self):
        pass

    #
    # Add alias
    #
    def _add(self, args):
        # Build data object
        data = { "name": args.NAME, "command": args.COMMAND, "desc": args.desc }
        # Get filepath to data
        filepath = shcSYS.getDatastorePath()
        # Search for existing shortcut name
        if shcPARSE.findLinesFromFile(args.NAME, filepath) is False:
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
            # Set filepath to data
            filepath = shcSYS.getDatastorePath()
            # Read lines of file
            lines = shcPARSE.readFileLines(filepath)
            # Configure output 
            table = prettytable.PrettyTable()
            table.align = 'l'
            table.field_names = ["Name", "Runs command", "Description"]
            # For each line in file
            for line in lines:
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
        print("Remove method")

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