from django.db import models

from pub.models import User, Post
from model_subscription.mixin import SubscriptionModelMixin
from model_subscription.models import SubscriptionQuerySet, SubscriptionModel


# Create your models here.

class Sub_log(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    before = models.TextField()
    after = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    check_change = models.BooleanField(default=True)

    def __str__(self):
        return self.id_user.name

class TestModel(SubscriptionModel):
    name = models.CharField(max_length=255)

