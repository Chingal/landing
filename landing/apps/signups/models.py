from django.db import models
from django.utils.encoding import smart_unicode


class SignUp(models.Model):
    for_you    = models.BooleanField(default=True, verbose_name="This is for you?")
    first_name = models.CharField(null=True, max_length=140, blank=True)
    last_name  = models.CharField(null=True, max_length=140, blank=True)
    email      = models.EmailField()
    timestamp  = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = ('SignUp')
        verbose_name_plural = ('SignUps')

    def __unicode__(self):
        return smart_unicode(self.email)