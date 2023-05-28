import prettytable
from . import shcmds_parser as shcPARSE
from . import shcmds_sys as shcSYS

class shcmds:

    # 
    # Defined constants
    # 
    SHELL_PROFILE_PATH = shcSYS.getShellProfilePath()
    SHELL_TYPE = shcSYS.getShellType()
    DATASTORE_PATH = shcSYS.getDatastorePath()
    TEXT_BOLD = '\033[1m'
    TEXT_DEFAULT = '\033[0m'

    #
    # Class constructor
    #
    def __init__(self):
        # Create data file if it does not exists
        if shcSYS.fileExists(self.DATASTORE_PATH) is False:
             # Create data file
            file = open(self.DATASTORE_PATH, 'w')
            file.close()
            # Install
            self.__install()

        # Set golbal data
        self.DATASTORE_DATA = shcPARSE.readFileLines(self.DATASTORE_PATH)

    #
    # Add command
    #
    def _add(self, args):
        # Build data object
        data = { "name": args.NAME, "command": args.COMMAND, "desc": args.desc }
        # Search for existing shortcut name
        if shcPARSE.findLinesFromFile(args.NAME, self.DATASTORE_PATH, True) is False:
            # Try to save to file
            try:
                # Write data to datastore
                self.__saveData(data)
                # Print result
                print(f"{self.TEXT_BOLD}New alias saved{self.TEXT_DEFAULT}: {data['name']}")
                # Reload message
                self.__reloadShellHelper()
            
            # Catch exception
            except Exception as e:
                print(f"{self.TEXT_BOLD}Error trying to save alias{self.TEXT_DEFAULT}: {data['name']}")
                print(e)
        else:
            print(f"Alias {self.TEXT_BOLD}{data['name']}{self.TEXT_DEFAULT} already exists")

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
            table.field_names = [
                f"{self.TEXT_BOLD}Name{self.TEXT_DEFAULT}", 
                f"{self.TEXT_BOLD}Runs command{self.TEXT_DEFAULT}", 
                f"{self.TEXT_BOLD}Description{self.TEXT_DEFAULT}"]
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
                    shcPARSE.truncateString(line[1], 60), #command
                    shcPARSE.truncateString(line[2], 40), #desc
                ])
            # Print out table
            print(f"\nUse a command alias with: {self.TEXT_BOLD}shc-NAME{self.TEXT_DEFAULT}\n")
            print(table)
            print(f"View alias details with: {self.TEXT_BOLD}shc show NAME{self.TEXT_DEFAULT}\n")

        # Catch exceptions
        except Exception as e:
            print(f'{self.TEXT_BOLD}Error listing aliases{self.TEXT_DEFAULT}.')
            print(e)

    #
    # Show command
    #
    def _show(self, args):
        # Get target alias
        target = shcPARSE.findLinesFromFile(args.NAME, self.DATASTORE_PATH, True)
        # Search for existing shortcut name
        if target is not False:
            print(f"{self.TEXT_BOLD}Alias name{self.TEXT_DEFAULT}: {target[0]}")
            print(f"{self.TEXT_BOLD}Description{self.TEXT_DEFAULT}: {target[2]}")
            print(f"{self.TEXT_BOLD}Command{self.TEXT_DEFAULT}: {target[1]}")
            print(f"{self.TEXT_BOLD}Usage{self.TEXT_DEFAULT}: shc-{target[0]}")
        else:
            # Print error
            print(f"Command alias {self.TEXT_BOLD}{args.NAME}{self.TEXT_DEFAULT} was not found.")
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
                print(f"{self.TEXT_BOLD}Removed alias{self.TEXT_DEFAULT}: `{args.NAME}`")
                # Reload message
                self.__reloadShellHelper()
            else:
                # Print error
                print(f"Alias: {self.TEXT_BOLD}{args.NAME}{self.TEXT_DEFAULT} was not found.")
        
        # Catch exception
        except Exception as e:
            print(f"{self.TEXT_BOLD}Error trying to remove alias{self.TEXT_DEFAULT}: `{args.NAME}`")
            print(e) 

    #
    # Export command
    #
    def _export(self, args):
        try:
            # Validate arguments
            if args.PATH == '.':
                args.PATH = shcSYS.getCurrentDir()
            if args.NAME is None:
                args.NAME = 'shcdata.json'
            # Try to get data as JSON
            json = shcPARSE.textToJson(self.DATASTORE_DATA)
            # Open and write json to file
            with open(args.PATH + '/' + args.NAME, 'w+') as f:
                f.write(json)
                f.close()
            # Success
            print(f"{self.TEXT_BOLD}Successful data export{self.TEXT_DEFAULT}: {args.PATH}/{args.NAME}")
        # Catch exception
        except Exception as e:
            print("Unable to export data:")
            print(e)

    #
    # Import command
    #
    def _import(self, args):
        try:
            # Check if file exists
            if shcSYS.fileExists(args.PATH) is not False:
                # Open file as read
                with open(args.PATH, 'r') as f:
                    # Read/close file
                    data = f.read()
                    f.close()
                # Convert text data to json
                data = shcPARSE.jsonToText(data)
                # Open datasource file
                with open(self.DATASTORE_PATH, 'w') as fn:
                    # Write each line to file
                    for line in data:
                        fn.write(line + '\n')
                    fn.close()
                # Success
                print(f"{self.TEXT_BOLD}Successful data import{self.TEXT_DEFAULT}.")
            else:
                # Error
                print(f"{self.TEXT_BOLD}Unable to import data: file not found{self.TEXT_DEFAULT}.")
        # Catch exception
        except Exception as e:
            print("Unable to import data:")
            print(e)

    # Private: save
    def __saveData(self, data):
        # Create new text line from data
        line = f"alias shc-{data['name']}='{data['command']}' #{data['desc']}"
        # Open file and write line
        with open(self.DATASTORE_PATH, 'a') as f:
            f.write(line + '\n')
            f.close()

    # Private: install
    def __install(self):
        try:
            ## Try to add datastor path to profile
            with open(self.SHELL_PROFILE_PATH, "a") as f:
                f.write('source ' + self.DATASTORE_PATH + '\n')
                f.close()
            # Return
            return True
        except Exception as e:
            print(f'{self.TEXT_BOLD}Install error{self.TEXT_DEFAULT}: ')
            print(e)
            return False

    # Private: uninstall
    def __uninstall(self):
        try:
            with open(self.SHELL_PROFILE_PATH, "r") as f:
                lines = f.readlines()
            with open(self.SHELL_PROFILE_PATH, "w") as f:
                for line in lines:
                    if self.DATASTORE_PATH not in line:
                        f.write(line)
                f.close()
            return True
        except Exception as e:
            print(f'{self.TEXT_BOLD}Uninstall error{self.TEXT_DEFAULT}:')
            print(e)
            return False

    # Private: reload shell
    def __reloadShellHelper(self):
        print(f"* To enable latest alias changes you will need to\n* open a new shell or run:{self.TEXT_BOLD} source {self.SHELL_PROFILE_PATH}{self.TEXT_DEFAULT}")