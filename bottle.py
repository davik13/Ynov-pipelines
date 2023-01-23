from bottle import route, run, template
from calcul import calcul




@route('/')
def homepage():
    return 'Hello you !'


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/add/<a>/<b>')
def add(a, b):
    return {'result': calcul(a, b)}


run(host='localhost', port=8080, debug=True, reloader=True)
