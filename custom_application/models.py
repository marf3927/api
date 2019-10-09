from django.db import models
from user.models import User


class CstApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.IntegerField(default=0)
    personal_info_agreed = models.BooleanField(default=False)
    text_agreed = models.BooleanField(default=False)
    is_picked = models.BooleanField(default=False)
    image = models.ImageField(upload_to='uploads/items_image/')
