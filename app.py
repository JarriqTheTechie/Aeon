import pprint
import random
import secrets

from flask import Flask, request
from mv_components import MVComponent
from packages.Commands import Commands
from packages.FileBasedRouter import FileBasedRouter

app = Flask(__name__)
FileBasedRouter(app)
Commands(app) # Loads a series of commands.
MVComponent(app) # Loads mv-components.


#pprint.pprint(FileBasedRouter().routes_export(), depth=50, sort_dicts=True, indent=4, compact=True)




if __name__ == '__main__':
    app.run()
