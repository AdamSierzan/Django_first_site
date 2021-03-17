from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    # each class is going to be it's own table in the database
    # now we will create some attribute, and each attribute will be
    #a different field in the database

    # each title is going to be a character field, with max
    title = models.CharField(max_length=100)
    # content field is similar to title field
    content = models.TextField()
    # now we create date_posted, but we will use default with django.utils timezone,
    # so we have better control of the time of posting
    date_posted = models.DateTimeField(default=timezone.now)
    # we didn't put parenthesis after timezone, it is a function
    # but we dont want to execute that function at that point
    # now we have to put author, but since the author is a different
    # table, so we need to import user module and django created that
    # in the location, we need to import it.
    # Since it's a many to one relationship we can use ForeignKey
    # on_delete means that if our user is deleted his post will be deleted as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

