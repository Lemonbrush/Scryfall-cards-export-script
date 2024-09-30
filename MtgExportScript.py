import json, time, requests, argparse, os

### Properties

parser = argparse.ArgumentParser()
parser.add_argument('--file', nargs=1,
                    help="JSON file to be processed",
                    type=argparse.FileType('r'))
arguments = parser.parse_args()

archiveLinksFile = json.load(arguments.file[0])

### Functions

if archiveLinksFile["messages"]:
    messages = archiveLinksFile["messages"]
    for dialog in messages:
        first_value = values[0]
        if dialog[first_value]:
            dialogContent = dialog[first_value]
            if dialogContent["error"]:
                print(dialogContent["error"])
