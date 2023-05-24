import argparse
from . import shcmds
#import shcmds

def cli():
    # New SHCMDS class
    shc = shcmds.shcmds()
    
    # Create parser object
    parser = argparse.ArgumentParser(
        prog="shc",
        usage="shc [-options] arguments"
    )
    # Create sub parser object as child of main parser
    subparser = parser.add_subparsers()

    # Add command
    shcAdd = subparser.add_parser("add", help="Add new command alias", usage="shc add NAME COMMAND [-d | --desc] 'string value in quotes'")
    shcAdd.add_argument("NAME", help="name of shorthand command", type=str)
    shcAdd.add_argument("COMMAND", help="command to run on invocation", type=str)
    shcAdd.add_argument("-d", "--desc", dest="desc", help="description of command", type=str, metavar="STRING")
    shcAdd.set_defaults(func=shc._add)

    # List command
    shcList = subparser.add_parser("list", help="List existing command aliases", usage="shc list [-f] NAME")
    shcList.add_argument("-f", "--filter", dest="NAME", help="filter by alias name", type=str, metavar="NAME")
    shcList.set_defaults(func=shc._list)

    # Remove command
    shcRemove = subparser.add_parser("remove", help="Remove/delete a command alias", usage="shc remove NAME")
    shcRemove.add_argument("NAME", help="name of shorthand command", type=str)
    shcRemove.set_defaults(func=shc._remove)

    # Parse arguments
    args = parser.parse_args()
    args.func(args)


# Main
if __name__ == "__main__":
    # Run cli
    cli()