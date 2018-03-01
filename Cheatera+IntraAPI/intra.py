import urllib3
from requests_oauth2 import OAuth2

auth = OAuth2('', authorization_url='https://api.intra.42.fr', token_url='oauth/token')
token = auth.token_url

print(token)