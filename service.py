import json
from bottle import request, route, run

@route('/',method='POST')
def index()
     data=request.params.get('data')
     print "your data = {data}".format(data=data)
     return "sucess"

run(host='0.0.0.0', port=8080, debg=True)
