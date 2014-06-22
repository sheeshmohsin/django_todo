from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoList(models.Model):
	user = models.ForeignKey(User)
	task = models.TextField()
	status = models.CharField(max_length=10)

	def __unicode__(self):
		return self.task
