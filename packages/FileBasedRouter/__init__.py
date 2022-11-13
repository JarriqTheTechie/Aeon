import fnmatch
import os
import secrets
from pydoc import locate
import dpath.util
from typing import Any
import re
from flask import request



def to_class(path: str) -> Any:
    """
        Converts string class path to a python class

    return:
        mixed
    """
    try:
        class_instance = locate(path)
    except ImportError:
        print('Module does not exist')
    return class_instance or None


class FileBasedRouter:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        for route in FileBasedRouter().routes_export():
            app.add_url_rule(route.get('path'), view_func=route.get('view_func'), endpoint=route.get('endpoint'),
                             methods=[route.get('method')])

    def find_routes_files(self):
        self.possible_routes = []
        for root, dirnames, filenames in os.walk(r'application/pages'):
            for filename in fnmatch.filter(filenames, '*.py'):
                if filename is None:
                    pass
                else:
                    self.possible_routes.append(os.path.join(root, filename).lstrip("application/pages").lstrip("\\").replace("\\", "."))
        return self
    def generate_fqns(self):
        self.fqdns = []
        for route in self.possible_routes:
            fqdn = f"application.pages.{route.rstrip('.py')}.default"
            self.fqdns.append(fqdn)
        return self
    def fqdns_to_route_path(self):
        self.route_paths = []
        self.route_map = []
        for path in self.fqdns:
            fqdn = path
            path = path.replace("default", "")
            path = path.replace("application.pages.", "/")
            path = path.replace(".", "/")

            path = path.replace("index/", "")
            path = path.replace("[", "<").replace("]", ">")

            method = fqdn.split(".")[-2]
            if method in ["GET", "POST", "PUT", "DELETE", "PATCH"]:
                method = method
            else:
                method = "GET"
            if path == "/":
                pass
            else:
                path = path.rstrip("/")
            self.route_map.append({
                "path": path,
                "view_func": to_class(fqdn),
                "endpoint": secrets.token_urlsafe(8),
                "method": method
            })
        return self

    def routes_export(self):
        return self.find_routes_files().generate_fqns().fqdns_to_route_path().route_map

