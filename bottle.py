from bottle import route, run
from calcul import calcul


@route('/hello')
def hello():
    return "Hello World! bien tu es sur la page hello"


@route('/add/<a>/<b>')
def add(a, b):
    return {'result': calcul(a, b)}


run(host='localhost', port=8080, debug=True, reloader=True)
