from pyotp import TOTP
import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Reconfigure logging again, this time with a file.
logging.basicConfig(filename = '../myfile.log', level=logging.DEBUG, format='%(filename)s:%(lineno)s---%(asctime)s %(levelname)s:%(message)s',filemode='w')
logger = logging.getLogger()
token_path = "../datafiles/api_key.txt"
key_secret = open(token_path, 'r').read().split()
access_token = open('../datafiles/access_token.txt', 'r').read()
global request_token
totp = TOTP(key_secret[4])
token_totp = totp.now()
kite = ""


