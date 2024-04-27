#!/usr/bin/python3
"""
display the body of the response
"""

if __name__ == '__main__':
    import urllib.parse
    import urllib.request
    from sys import argv

    url = argv[1]
    values = {'email': argv[2]}

    dato = urllib.parse.urlencode(values)
    dato = dato.encode('ascii')
    reqst = urllib.request.Request(url, dato)
    with urllib.request.urlopen(reqst) as response:
        body = response.read()
    print(body.decode('utf-8'))
