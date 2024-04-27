#!/usr/bin/python3
"""Fetch the value of the X-Request-ID variable"""

if __name__ == '__main__':
    import requests
    from sys import argv
    reqst = requests.get(argv[1])
    print(reqst.headers.get('X-Request-ID'))
