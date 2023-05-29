import argparse
from .src import shcmds
# from src import shcmds

def cli():
    # New SHCMDS class
    shc = shcmds.shcmds()
    
    # Create parser object
    parser = argparse.ArgumentParser(
        prog="shc",
        usage="shc [-options] arguments"
    )
    parser.set_defaults(func=lambda args: parser.print_help())
    # Create sub parser object as child of main parser
    subparser = parser.add_subparsers()

    # Add command
    shcAdd = subparser.add_parser("add", help="Add new command alias", usage="shc add NAME COMMAND [-d | --desc] 'string value in quotes'")
    shcAdd.add_argument("NAME", help="name of shorthand command", type=str)
    shcAdd.add_argument("COMMAND", help="command to run on invocation", type=str)
    shcAdd.add_argument("-d", "--desc", dest="desc", help="description of command", type=str, metavar="STRING")
    shcAdd.add_argument("-f", "--force", help="override existing shorthand command, if name exists", action='store_true')
    shcAdd.set_defaults(func=shc._add)

    # List command
    shcList = subparser.add_parser("list", help="List existing command aliases", usage="shc list [-s | --search] NAME")
    shcList.add_argument("-s", "--search", dest="NAME", help="search shorthand commands by name", type=str, metavar="NAME")
    shcList.set_defaults(func=shc._list)

    # Show command
    shcShow = subparser.add_parser("show", help="Show single command alias details", usage="shc show NAME")
    shcShow.add_argument("NAME", help="name of shorthand command", type=str)
    shcShow.set_defaults(func=shc._show)

    # Remove command
    shcRemove = subparser.add_parser("remove", help="Remove/delete a command alias", usage="shc remove NAME")
    shcRemove.add_argument("NAME", help="name of shorthand command", type=str)
    shcRemove.set_defaults(func=shc._remove)

    # Export command
    shcExport = subparser.add_parser("export", help="Export all aliases to a json file", usage="shc export PATH [-o | --output] FILENAME")
    shcExport.add_argument("PATH", help="filepath for generated file", type=str)
    shcExport.add_argument("-o", "--output", dest="NAME", help="filename for generated file", type=str)
    shcExport.set_defaults(func=shc._export)

    # Export command
    shcImport = subparser.add_parser("import", help="Export all aliases to a json file", usage="shc import PATH")
    shcImport.add_argument("PATH", help="path to data file (json)", type=str)
    shcImport.set_defaults(func=shc._import)

    # Parse arguments
    args = parser.parse_args()
    args.func(args)

# Main
if __name__ == "__main__":
    # Run cli
    cli()