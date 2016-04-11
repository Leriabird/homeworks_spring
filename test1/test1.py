#!/usr/bin/python3.4
import argparse
import os.path
#import shutil
import subprocess
#from os import listdir

parser = argparse.ArgumentParser(description="two required args: percentage and path; one optional arg: path to new file")

parser.add_argument("percentage",
                    type=str,
                    help="% of compression")
parser.add_argument("path",
                    type=str,
                    help="PATH to file/folder")
parser.add_argument("newpath",
                    type=str,
                    help="path to new file",
                    nargs='?')

# parsing arguments and making them as attributes
args = parser.parse_args()
percentage = args.percentage
path = args.path
newpath = args.newpath

if os.path.isfile(path):
    if newpath:
        subcommand = "convert " + path + " -resize " + percentage + "% " + newpath # the callname passed to subprocess
        subprocess.run(subcommand, stdin=None, input=None, stdout=None, shell=True, check=False)
    else:
        subcommand = "convert " + path + " -resize " + percentage + "% " + path # the callname passed to subprocess
        subprocess.run(subcommand, stdin=None, input=None, stdout=None, shell=True, check=False)
elif os.path.isdir(path):
    subcommand = "find . -iregex '.*.jpg' -exec convert '{}' -resize " + percentage + " png:'{}' \;"
    subprocess.run(subcommand, stdin=None, input=None, stdout=None, shell=True, check=False)
    subcommand = "find . -iregex '.*.png' -exec convert '{}' -resize " + percentage + " jpg:'{}' \;"
    subprocess.run(subcommand, stdin=None, input=None, stdout=None, shell=True, check=False)
else:
    print('Error: unsupported data type')

    #.*.(png|jpg)


    #.*\(deb\|vmdk\)$