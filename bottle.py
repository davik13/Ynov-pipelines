from bottle import route, run, template
from calcul import calcul


@route('/')
def homepage():
    return 'Hello you !'


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/add/<a>/<b>')
@route('/add/<a:int>/<b:int>/')
def add(a, b):
    return {'result': calcul(a, b)}
    

if __name__ == "__main__":
    run(host="localhost", port=8080, reloader=True)
