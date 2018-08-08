"Python script to test password against known passwordleaks published at HIBP."

# dependencies
import hashlib
import getpass
import requests
import SecureString
from huepy import *

API_URL_BASE = 'https://api.pwnedpasswords.com/range/'
HEADERS = {'Content-Type': 'application/text',
           'User-Agent': 'passwdpwnd.py'}
PREFIX_LEN = 5

# ask for password and hash it with sha1
PASSWORD = getpass.getpass('Please enter a password: ').encode('utf-8')
HASH_OBJECT = hashlib.sha1(PASSWORD)
SecureString.clearmem(PASSWORD)
HASHED_PASS = HASH_OBJECT.hexdigest()


def password_check():
    "API call with first 5 characters from hashed_pass"

    api_url = format(API_URL_BASE)+format(HASHED_PASS[:PREFIX_LEN].upper())
    response = requests.get(api_url, headers=HEADERS)

    if response.status_code == 200:
        return response.content.decode('utf-8')


HASHES = password_check()

if HASHES is not None:

    # convert text result to dictionary by splitting it on ':'
    HASH_DICT = dict(item.split(':') for item in HASHES.split())
    if HASHED_PASS[PREFIX_LEN:].upper() in HASH_DICT:
        print (info("Found password in HIBP: " \
            + str(HASH_DICT[HASHED_PASS[PREFIX_LEN:].upper()]) + " times"))
    else:
        print (good("Password not found in HBIP!"))

    # clear hash_dict
    HASH_DICT = ()

else:
    print (bad("Request failed"))
