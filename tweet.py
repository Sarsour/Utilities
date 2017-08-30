from twython import Twython

APP_KEY = 'xe6qDF9DfJRe8RazjtLMJo6Ra'
APP_SECRET = 'h0Fm5HA6go2bTHrhOCdgd60HgMFqZTvq36VhcNt06UbewFlnKP'
OAUTH_TOKEN = '27286396-XyJ9so6ZsdJTgEmpkSbwXxMgnkl7lUWo0dj77efvH'
OAUTH_TOKEN_SECRET = 'jODgQ5a32ga87CJT0M2XHMmgIhhQEG5HsjEvsBywN5Y6E'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter.update_status(status='testing')