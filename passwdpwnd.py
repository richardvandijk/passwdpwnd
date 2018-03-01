# 

# dependencies
import requests
import hashlib
import getpass
import SecureString

api_url_base = 'https://api.pwnedpasswords.com/range/'

headers = {'Content-Type': 'application/text',
           'User-Agent': 'Check-for-pyscript'}


# ask for password and hash it with sha1           
password = getpass.getpass('Please enter a password: ').encode('utf-8')
hash_object = hashlib.sha1(password)
SecureString.clearmem(password)
hashed_pass = hash_object.hexdigest()

# API call with first 5 characters from hashed_pass
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
hash_dict = ()
