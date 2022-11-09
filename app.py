import glob
from flask import Flask
from mv_components import MVComponent
from packages.Commands import Commands


app = Flask(__name__)
Commands(app) # Loads a series of commands.
MVComponent(app) # Loads mv-components.


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
