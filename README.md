# passwdpwnd
Python script to test if your password is pwnd. Test your password against the \
'Have I Been Pwnd' database by Troy Hunt.

## Dependencies

* requests
* getpass
* hashlib
* SecureString

## Inner workings

* hashes input password
* sends first 5 characters of hash to HaveIBeenPwnd.com
* erases password from memory

