from django.db import models
from .validators import validate_file_extension

class Analytics(models.Model):
	file = models.FileField(upload_to='analytics/', validators=[validate_file_extension])