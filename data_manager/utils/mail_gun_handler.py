import requests
from utils.base import BASE_DATA as bd

MAILGUN_API_KEY = bd["MAILGUN_API_KEY"]

def mailgun_send(reciever_name, receiver_address, subject, text):
	return requests.post(
		"https://api.mailgun.net/v3/sandboxe277c56e55f74ffb80855759ab1f9484.mailgun.org/messages",
		auth=("api", f"{MAILGUN_API_KEY}"),
		data={
			"from": "Mailgun Sandbox <postmaster@sandboxe277c56e55f74ffb80855759ab1f9484.mailgun.org>",
			"to": f"{reciever_name} <{receiver_address}>",
			"subject": subject,
			"text": text})

# You can see a record of this email in your logs: https://app.mailgun.com/app/logs.

# You can send up to 300 emails/day from this sandbox server.
# Next, you should add your own domain so you can send 10000 emails/month for free.