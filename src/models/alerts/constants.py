import os
__author__ = 'jslvtr'


#URL = "https://api.mailgun.net/v3/<>.mailgun.org/messages"
#API_KEY = "key-<>"
#FROM = "Mailgun Sandbox <postmaster@<>.mailgun.org>"
URL = os.environ.get('MAILGUN_DOMAIN')
API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM = os.environ.get('MAILGUN_FROM')
ALERT_TIMEOUT = 10
COLLECTION = "alerts"