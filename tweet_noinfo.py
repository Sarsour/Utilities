from twython import Twython

APP_KEY = 'XXX'
APP_SECRET = 'XXX'
OAUTH_TOKEN = '27286396-XXX'
OAUTH_TOKEN_SECRET = 'XXX'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter.update_status(status='testing')