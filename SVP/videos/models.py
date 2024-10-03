from django.db import models
from users.models import Account


# Create your models here.


class Video(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def cover_upload_to(self, filename):
        return f'Files/{self.account.id}/Covers/{filename}'

    def file_upload_to(self, filename):
        return f'Files/{self.account.id}/Videos/{filename}'

    cover = models.FileField(upload_to=cover_upload_to)
    file = models.FileField(upload_to=file_upload_to)

    def __str__(self):
        return self.title
