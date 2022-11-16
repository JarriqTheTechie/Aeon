from mv_components import MVComponent

from config.aeon import config as _config
from packages.ADAuthenticator import ADAuthenticator
from packages.Commands import Commands
from packages.FileBasedRouter import FileBasedRouter


class AEON:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        FileBasedRouter(app) # Loads file based routing
        Commands(app)  # Loads a series of commands.
        MVComponent(app)  # Loads mv-components.
        ADAuthenticator(app) # Loads Active Directory Based Auth
        app.secret_key = _config.get("auth").get("SECRET_KEY") # Set app secret key

        # Add Custom Jinja Directives
        app.jinja_env.add_extension('packages.JinjaDirectives.UnlessDirective')
        app.jinja_env.add_extension('packages.JinjaDirectives.AuthDirective')
        app.jinja_env.add_extension('packages.JinjaDirectives.GuestDirective')
        app.jinja_env.add_extension('packages.JinjaDirectives.ProductionDirective')

        @app.template_global()
        def config(category, key):
            return _config.get(category).get(key)

