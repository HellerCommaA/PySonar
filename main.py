"""
Written by Adam Heller
for NextGenVest.com
Licensed under what ever my code is supposed to be licensed under
"""

# settings.SONAR_PUB
# settings.SONAR_PRIV
# settings.SONAR_URL


import requests
from django.conf import settings
import json

# print settings.SONAR_PUB


class SonarError(Exception):
	"""
	base error class for PySonar. Nothing special here.
	"""
	def __init__(self, message, errors):

		# Call the base class constructor with the parameters it needs
		super(Exception, self).__init__(message)

		# Now for your custom code...
		self.errors = errors

class InvalidPhoneNumber(SonarError): 
	""" just another exception class to raise"""
	pass



def send(to, message, image_url = None):
	"""
	sends a message to a phone number. 

	:param to: a phone number to send a message to
	:type to: string format (No checking needed, sendsonar will handle it)
	:param message: a message to send to 'to' <= length of 159 suggested
	:type message: string, you can send emjoi as well
	:param image_url: an image to associate with the user
	:type image_url: string, 'http://www.myhost.com/image1.png' style format
	:returns: JSON from successful POST to sonar's API, else: error SonarError or InvalidPhoneNumber
	:rtype: JSON
	"""

	payload = {
		'to': to,
		'text': message,
		'image_url': image_url
	}
	headers = {
		'Content-type': 'application/json',
		'X-Token': settings.SONAR_PRIV
	}

	r = requests.post(settings.SONAR_URL + 'messages', data=json.dumps(payload), headers = headers)
	# print r.text
	return err_check(r)

def customer(to, email = 'None', first_name = 'None', last_name = 'None', properties = 'None', picture_url = 'None'):
	payload = {
		'phone_number': to,
		'email': email,
		'first_name': first_name,
		'last_name': last_name,
		'picture_url': picture_url,
		'properties': properties
	}
	headers = {
		'Content-type': 'application/json',
		'X-Token': settings.SONAR_PRIV
	}

	r = requests.post(settings.SONAR_URL + 'customers', data=json.dumps(payload), headers = headers)
	return err_check(r)

def err_check(r):
	x = r.json()
	try:
		if x['error'] == 'Invalid Phone Number':
			raise InvalidPhoneNumber('Invalid Phone Number. Response %s ' % r.json(), r.json())
	except KeyError:
		pass
	if r.status_code == 202 or r.status_code == 200:
		return r.text
	else:
		raise SonarError('Returned non 202 status. Status code: %s' % r.status_code, r.status_code)