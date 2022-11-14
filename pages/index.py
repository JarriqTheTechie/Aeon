from flask import url_for, redirect, render_template
from mv_components import render_inline
from pip._vendor.chardet.metadata.languages import Language

endpoint = "home"


def default():
    #x = True
    kangaroo = "adgda"
    return render_template('index.html', kangaroo=kangaroo)
