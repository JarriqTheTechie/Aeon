import win32api
from flask import session

import config.aeon
from application.interfaces.ActionInterface import ActionInterface
from packages.ADAuthenticator.Impersonate import Impersonate


class CreateSessionAction(ActionInterface):
    @classmethod
    def handle(self, data: dict):
        session['username'] = data.get('username')
        impersonator = Impersonate(data.get('username'), data.get("password"), config.aeon.config.get('auth').get('DOMAIN'))
        # Get Username by impersonating user
        impersonator.logon()
        fullname = win32api.GetUserNameEx(3)
        impersonator.logoff()
        session['FullName'] = fullname