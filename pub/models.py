from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from model_subscription.models import SubscriptionModel


# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
class MySubscription(SubscriptionModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'post')
    def __str__(self):
        return f'{self.user} - {self.post}'
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class Conditions(models.Model):
    feild = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    value_change = models.CharField(max_length=100)
    next_condition = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.feild


class log(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    before = models.JSONField(default=dict)
    after = models.JSONField(default=dict)
    conditions = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    check_change = models.BooleanField( default=True)


    def __str__(self):
        return f'{self.id_user} - {self.id_post}'


