import masoniteorm
import win32con
import win32security
from flask import redirect, url_for
from application.interfaces.ActionInterface import ActionInterface
from config.database import DB


class Impersonate:
    def __init__(self, login, password, domain):
        self.domain = domain
        self.login = login
        self.password = password

    def logon(self):
        self.handle = win32security.LogonUser(self.login, self.domain, self.password,
                                              win32con.LOGON32_LOGON_INTERACTIVE, win32con.LOGON32_PROVIDER_DEFAULT)
        win32security.ImpersonateLoggedOnUser(self.handle)

    def logoff(self):
        win32security.RevertToSelf()  # terminates impersonation
        self.handle.Close()  # guarantees cleanup


