import fnmatch
import os
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


class Router:
    def __init__(self):
        self.possible_routes = []
        self.route = None

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
            path = path.replace("application.pages.", "/")
            path = path.replace(".", "/")
            path = path.replace("default", "")
            path = path.replace("index/", "")

            opening_braces = '\\(\\['
            closing_braces = '\\)\\]'
            non_greedy_wildcard = '.*?'
            path = str(re.sub(f'[{opening_braces}]{non_greedy_wildcard}[{closing_braces}]', '.*', path))

            if path == "/":
                pass
            else:
                path = path.rstrip("/")
            self.route_map.append({path: fqdn})
            self.route_paths.append(path)
        return self

    def get_from_dict_OLD(self):
        for route in self.route_map:
            if route.get(request.path):
                self.route = list(route.values())[0]
        if self.route:
            return self
        else:
            self.route = "TODO : Add extendable not found logic here."

    def get_from_dict(self):
        route_keys = ["".join(list(route.keys())) for route in self.route_map]
        regex_route_keys = list(map(re.compile, route_keys))
        print(regex_route_keys)
        if any(regex.match(request.path) for regex in regex_route_keys):
            print(any(regex.match(request.path) for regex in regex_route_keys))
        if request.path == "/":
            self.route = list(self.get_item(self.route_map, "/").values())[0]
            return self
        else:
            self.route = self.get_matching_pattern(regex_route_keys, request.path)
            for route in self.route_map:
                if self.route in route.keys():
                    self.route = route[self.route]
            return self


    def launch(self):
        self.find_routes_files().generate_fqns().fqdns_to_route_path().get_from_dict()
        try:
            route_function = to_class(self.route)
            return route_function()
        except:
            return self.route

    def get_matching_pattern(self, pattern_list: list, path):            ## Function name changed
        matches = []
        for pattern in pattern_list:
            if pattern == re.compile("/"):
                pass
            else:
                match = re.search(pattern, path)   ## Use re.search method
                if match:                              ## Correct the indentation of if condition
                    print(pattern, match)
                    #return match.string                      ## You also don't need an else statement


    def get_item(self, collection, key):
        return next((item for item in collection if item[key]), None)


