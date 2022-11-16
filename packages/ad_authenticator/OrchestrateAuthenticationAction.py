from flask import redirect, url_for

import config.aeon
from application.interfaces.ActionInterface import ActionInterface
from packages.ad_authenticator.ADAuthAction import ADAuthAction
from packages.ad_authenticator.CreateSessionAction import CreateSessionAction


class OrchestrateAuthenticationAction(ActionInterface):
    @classmethod
    def handle(self, data: dict) -> bool:
        auth: bool = ADAuthAction.handle(data)
        if auth:
            start_session = CreateSessionAction.handle(data)
            CHAINABLE_AUTH_SERVICES: list = config.aeon.config.get('auth').get("CHAINABLE_AUTH_SERVICES")
            if CHAINABLE_AUTH_SERVICES:
                for SERVICE in CHAINABLE_AUTH_SERVICES:
                    SERVICE.handle(data)
            return True
        return False

    @classmethod
    def as_controller(self, data: dict):
        if self.handle(data):
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('do_login', error='yes'))


