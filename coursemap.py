
'''
This is the entrypoint into our application. This file will become largely
static once we establish some of the basics. We will bootstrap
the app and import the rest of the modules from here. Most work will be in
our custom modules.

--------------------

The application should operate in two distinct modes.
- With a GUI
- Without a GUI as a cli (command line interface)

We do this primarily for a few reasons.
1) As a CLI we can batch process with limited or no interaction.
2) We can easily test and debug the application without GUI distractions.

When we test the application in CLI mode, we should be able to specify various
arguments to operate the application from start to finish in one command or
run pieces of the application.

One of the first steps is to define what the command line arguments might be.
These arguments will be based on our application workflow, business requirements,
and some general best practices.

We whould utilize the argparse module to implement this functionality for us.
https://docs.python.org/3/library/argparse.html

Application arguments shall include the following:
# TODO: -h, --help          to show a brief help message
# TODO: -v, --version       display version information and exit.
# TODO: -d, --debug         print out debugging information
--init              Initialize our SQLite database
# TODO: --input=<file>      CSV file to import into the application
# TODO: --outputdir=<dir>   Directory to output our PDF files
# TODO: --grade=<grade>     The grade to process or 'all'
and...

'''
import lib.input as datainput
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d','--debug', help='Print out debugging information.', action='store_true')
parser.add_argument('--init', help='Initialize our SQLite database.', action='store_true')
# TODO: Add more Arguments as defined in our comments above.

args = parser.parse_args()
# args = parser.parse_args(['--init'])

if args.debug:
    pass # Output debugging information
elif args.init:
    datainput.createSqliteTables()
else:
    parser.print_help()
