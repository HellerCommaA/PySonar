class ImportError(ImportError):

	def __init__(self, message, errors):

		super(ImportError, self).__init__(message)
		self.errors = errors