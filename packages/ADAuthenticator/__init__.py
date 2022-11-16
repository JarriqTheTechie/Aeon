from functools import wraps
from flask import request, redirect, url_for, session, abort
import config.aeon
from packages.ADAuthenticator.OrchestrateAuthenticationAction import OrchestrateAuthenticationAction


class ADAuthenticator:
    def __init__(self, app=None):
        from jinja2 import Environment, PackageLoader
        self.jinja_env = Environment(
            autoescape=True,
            loader=PackageLoader(__name__, 'templates'))
        if app is not None:
            self.init_app(app)


    def init_app(self, app):
        from packages.Requester import Requester
        from flask import render_template, redirect, url_for, Blueprint

        bp = Blueprint('myext', __name__, template_folder='templates', static_folder='resources')
        app.register_blueprint(bp)

        @app.get('/welcome')
        @login_required
        def welcome():
            return redirect(config.aeon.config.get('auth').get('SUCCESS_URL'))

        @app.get(config.aeon.config.get('auth').get('LOGIN_URL'))
        def login():
            if Requester.input('error'):
                return render_template('login.html', error=True)
            return render_template('login.html')

        @app.post(config.aeon.config.get('auth').get('LOGIN_URL'))
        def do_login():
            username = Requester.input('username')
            password = Requester.input('password')
            data = {
                "username": username,
                "password": password
            }
            return OrchestrateAuthenticationAction.as_controller(data)

        @app.get(config.aeon.config.get('auth').get('LOGOUT_URL'))
        def do_logout():
            session.pop('username', None)
            return redirect(url_for('login'))


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def roles_allowed(roles=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if session.get('role') is None:
                return abort(403)
            accepted_roles_found = []
            for role in roles:
                if role == session.get('role'):
                    accepted_roles_found.append(role)
                    break
            if len(accepted_roles_found) != 0:
                return f(*args, **kwargs)
            else:
                return abort(403)
        return decorated_function
    return decorator


def roles_denied(roles=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if session.get('role') is None:
                return abort(403)
            denied_roles_found = []
            for role in roles:
                if role == session.get('role'):
                    denied_roles_found.append(role)
                    break
            if len(denied_roles_found) != 0:
                return abort(403)
            else:
                return f(*args, **kwargs)
        return decorated_function
    return decorator

