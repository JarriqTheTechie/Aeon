from flask import url_for, redirect, render_template
from mv_components import render_inline
from pip._vendor.chardet.metadata.languages import Language

endpoint = "home"


def default():
    return render_inline(
        """
                <!DOCTYPE html>
                <html lang="en">
                  <head>
                    <meta charset="UTF-8" />
                    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                    <script src="https://unpkg.com/htmx.org@1.8.0"></script>
                    <script src="https://unpkg.com/hyperscript.org@0.0.5"></script>
                    <link rel='stylesheet' href='https://bootswatch.com/5/simplex/bootstrap.min.css'>
                    <title>AEON Demo</title>
                  </head>
                </head>
                <body>
                  <div class='container-fluid'>
                    <mv-Button label='Help'></mv-Button>
                  </div>
                </body>
                </html>
                
                
            """
    )
