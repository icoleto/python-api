from flask import Response
import json

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


def toJsonResponse(obj):
    if hasattr(type(obj), '__iter__'):
        return Response(json.dumps([ob.__dict__ for ob in obj]), mimetype='application/json')
    else:
        return Response(json.dumps(obj.__dict__), mimetype='application/json')
