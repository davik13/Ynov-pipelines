from bottle import  run

def hello():
    return "Hello"

run(host='localhost', port=8080, debug=True, reloader=True)