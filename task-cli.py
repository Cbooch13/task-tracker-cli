# Task tracker implemented in python run through the CLI.  Roadmap.sh project
# Caleb Bucci
# 2024-09-23

import argparse


#Argument parser
parser = argparse.ArgumentParser(
    prog = "task-cli",
    description = "Task tracker in CLI",
    epilog = "Program Usage : python3 task-cli filename.json"
)

parser.add_argument('-a', '--add', help="Adds task to json file", required=False)