#!/usr/bin/python3
""" Fetch https://alx-intranet.hbtn.io/status using the requests package"""

if __name__ == '__main__':
    import requests
    reqst = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:\n\t- type: {}'.format(type(reqst.text)))
    print('\t- content: {}'.format(reqst.text))
