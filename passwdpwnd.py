# python3 only
# returns True if in dictonary & number of times

# todo:
# handling of response.status_code = 404

import requests
import hashlib

api_url_base = 'https://api.pwnedpasswords.com/range/'

headers = {'Contect-Type': 'application/text',
           'User-Agent': 'Check-for-pyscript'}


# ask for password and hash it with sha1           
password = input('Please enter a password: ').encode('utf-8')
hash_object = hashlib.sha1(password)
hashed_pass = hash_object.hexdigest()

# API call with first 5 characters from hash_password
def password_check():
	api_url = format(api_url_base)+format(hashed_pass[:5].upper())
	response = requests.get(api_url, headers=headers)
	
	if response.status_code != 200:
		return response.status_code
	
	if response.status_code == 200:
		return response.content.decode('utf-8')
		    
hashes = password_check()

# convert text result to dictonary by splitting it on ':'
hash_dict = dict(item.split(':') for item in hashes.split())

print(hashed_pass[5:].upper() in hash_dict, hash_dict[hashed_pass[5:].upper()])
