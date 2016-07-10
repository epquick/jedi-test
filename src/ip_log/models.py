from django.db import models


class RequestLog(models.Model):
	'''Model to store information about ip_log service POST requests'''
	ip = models.GenericIPAddressField()
	request_dt = models.DateTimeField(auto_now_add=True)
