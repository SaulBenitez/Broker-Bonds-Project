
import requests

def get_dollar_value():
    endpoint = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno'
    headers = {'Accept': 'application/json',
    'Bmx-Token': 'd9890dbfd40ba36b63db4381430417324cb5a48c2d01130a2e2f2c1d8eb869aa', 
    "Accept-Encoding": "gzip"}

    try:
        response = requests.get(endpoint, headers=headers)
        return float(response.json()['bmx']['series'][0]['datos'][0]['dato'])
    except:
        message = {"detail":"Dollar cannot be obtained"}
        return message

def get_dollar_info():
    endpoint = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno'
    headers = {'Accept': 'application/json',
    'Bmx-Token': 'd9890dbfd40ba36b63db4381430417324cb5a48c2d01130a2e2f2c1d8eb869aa', 
    "Accept-Encoding": "gzip"}

    try:
        response = requests.get(endpoint, headers=headers)
        return response.json()['bmx']['series'][0]['datos'][0]
    except:
        message = {"detail":"Dollar cannot be obtained"}
        return message