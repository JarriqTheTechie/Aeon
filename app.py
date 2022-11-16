from flask import Flask, session
from packages.AEON import AEON


app = Flask(__name__, template_folder='pages')
AEON(app)




@app.before_request
def rf():
    #session['Role'] = "Director"
    session.clear()

#pprint.pprint(FileBasedRouter().routes_export())

@app.template_global()
def double(n):
    return 2 * n


if __name__ == '__main__':
    app.run()
