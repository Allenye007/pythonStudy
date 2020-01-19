def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]

# uwsgi --http :8001 --wsgi-file test.py
