import masoniteorm
import win32api
import win32con
import win32security
from flask import redirect, url_for

import config.aeon
from application.interfaces.ActionInterface import ActionInterface
from config.database import DB



class ADAuthAction(ActionInterface):
    @classmethod
    def handle(self, data: dict) -> bool:
        username = data.get("username").lower()
        domain = config.aeon.config.get('auth').get("DOMAIN")
        print(domain)
        token = win32security.LogonUser(
            username,
            domain,
            data.get("password"),
            win32security.LOGON32_LOGON_NETWORK,
            win32security.LOGON32_PROVIDER_DEFAULT)
        authenticated = bool(token)
        return authenticated

