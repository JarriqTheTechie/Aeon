from flask import Flask, request
from mv_components import MVComponent
from packages.Commands import Commands
from packages.Router import Router

app = Flask(__name__)
Commands(app) # Loads a series of commands.
MVComponent(app) # Loads mv-components.



@app.errorhandler(404)
def page_handler(e):
    return Router().launch()




if __name__ == '__main__':
    app.run()
