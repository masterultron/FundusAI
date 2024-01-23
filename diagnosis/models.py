# models.py in the diagnosis app

from django.db import models

class Diagnosis(models.Model):
    image = models.ImageField(upload_to='fundus_images/')
    result = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_file_url(self):
        return self.image.url
