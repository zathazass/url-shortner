import random
import string
from django.db import models


class URLCollection(models.Model):
    redirect_url = models.CharField(max_length=2048, unique=True)
    url_name = models.CharField(max_length=256, null=True, blank=True)
    short_url = models.CharField(max_length=32, unique=True, db_index=True)
    redirect_count = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.short_url} - {self.redirect_url} - {self.redirect_count}'

    def set_short_url(self):
        letters = string.ascii_letters + string.digits
        length = random.choice(range(3,16))
        short_url = ''.join(random.choices(letters, k=length))

        is_unique = False
        while not is_unique:
            try:
                self.__class__.objects.get(short_url=short_url)
            except self.__class__.DoesNotExist:
                self.short_url = short_url
                is_unique = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_short_url()
        return super().save(*args, **kwargs)
