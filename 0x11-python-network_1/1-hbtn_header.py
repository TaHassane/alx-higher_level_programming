#!/usr/bin/python3
"""fetch the value of the X-Request-ID variable"""

if __name__ == '__main__':
    import urllib.request
    from sys import argv
    with urllib.request.urlopen(argv[1]) as response:
        xrequestid = response.getheader('X-Request-ID')
    print(xrequestid)
