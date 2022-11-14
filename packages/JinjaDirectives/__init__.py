from flask import session
from jinja2_simple_tags import StandaloneTag, ContainerTag


class UnlessDirective(ContainerTag):
    tags = {"unless"}

    def render(self, var, caller=None):
        if var:
            return caller()
        else:
            return ""

class AuthDirective(ContainerTag):
    tags = {"auth"}

    def render(self, roles, caller=None):
        if type(roles) == str:
            if roles == session.get("Role"):
                return caller()
            else:
                return ""
        if type(roles) == list:
            for role in roles:
                if role == session.get('Role'):
                    return caller()
            return ""


class GuestDirective(ContainerTag):
    tags = {"guest"}

    def render(self, roles=None, caller=None):
        if type(roles) == str:
            if roles == session.get("Role") or not session.get("Role"):
                return caller()
            else:
                return ""
        if type(roles) == list:
            for role in roles:
                if role == session.get('Role'):
                    return caller()
            return ""
        if not session.get("Role"):
            return caller()
        else:
            return ""


class ProductionDirective(ContainerTag):
    tags = {"else","production"}

    def render(self, environment, caller=None):
        from flask import Flask, current_app
        if current_app.debug:
            return ""
        return caller()