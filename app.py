import pprint
import random
import secrets

from flask import Flask, request, redirect, url_for, session
from mv_components import MVComponent
from packages.Commands import Commands
from packages.FileBasedRouter import FileBasedRouter
from packages.JinjaDirectives import UnlessDirective

app = Flask(__name__, template_folder='pages')
app.secret_key = "dfadfad"
FileBasedRouter(app)
Commands(app) # Loads a series of commands.
MVComponent(app) # Loads mv-components.

app.jinja_env.add_extension('packages.JinjaDirectives.UnlessDirective')
app.jinja_env.add_extension('packages.JinjaDirectives.AuthDirective')
app.jinja_env.add_extension('packages.JinjaDirectives.GuestDirective')
app.jinja_env.add_extension('packages.JinjaDirectives.ProductionDirective')

@app.before_request
def rf():
    #session['Role'] = "Director"
    session.clear()

#pprint.pprint(FileBasedRouter().routes_export())

@app.template_global()
def double(n):
    return 2 * n


if __name__ == '__main__':
    app.run()
