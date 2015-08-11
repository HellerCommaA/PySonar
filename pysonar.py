import errors
try:
	import requests
except ImportError, e:
	raise errors.ImportError('Can not import %s. Be sure it\'s installed and in your pip requirements.txt file' % e, e)