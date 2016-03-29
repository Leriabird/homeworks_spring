#!/usr/bin/python3.4
import argparse
import os.path
import shutil
import subprocess
from os import listdir

parser = argparse.ArgumentParser(description="two acceptable commands: store and diff")

parser.add_argument("command", choices=['store', 'diff'],
                    type=str,
                    help="'store' or 'diff")
parser.add_argument("path",
                    type=str,
                    help="PATH to working directory")
# parsing arguments and making them as attributes
args = parser.parse_args()
command = args.command
path = args.path

if command == 'store':
    if os.path.isfile(path):
        shutil.copy(path, "/Users/Leria/Documents/Bioinformatics_institute_2/Python/sad")
    else:
        fileslist = [f for f in listdir(path) if isfile(join(path, f))]
        for char in fileslist:
            if command == 'store':
                shutil.copy(path + "/" + char, "/Users/Leria/Documents/Bioinformatics_institute_2/Python/sad")
            elif command == 'diff':
                name = str(path.split('/')[-1])
                subcommand = "diff " + path + " ./sad/" + name # the callname passed to subprocess
                print(subprocess.run(subcommand, stdin=None, input=None, stdout=None, shell=True, check=False))
            else:
                print("Wrong command")
elif command == 'diff':
    name = str(path.split('/')[-1])
    subcommand = "diff " + path + " ./sad/" + name # the callname passed to subprocess
    print(subprocess.run(subcommand, stdin=None, input=None, stdout=None, shell=True, check=False))
else:
    print("Wrong command")