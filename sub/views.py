import json

import redis
from django.contrib.auth.models import User
from django.core.management import BaseCommand
import logging
from model_subscription.decorators import create_subscription

from pub.models import Post
from pub.serializers import UserSerializer
from sub.Redis import publish_data_on_redis
from sub.models import TestModel


# Create your views here.
class Create_user(BaseCommand):
    def handle(self, *args, **options):
        r = redis.StrictRedis(host='localhost', port=6379, db=1)
        p = r.pubsub()
        p.psubscribe('user.new')
        for message in p.listen():
            if message and message['data'] != 1:
                data = message['data'].decode('utf-8')
                data = json.loads(data)
                # print(data['username'])
                user_create = User.objects.create_user(username=data['username'], password=data['password'], email=data['email'])
                user_create.save()
                post_create = Post.objects.create(title=data['title'], description=data['description'], user=user_create)
                post_create.save()
                print("Post created successfully")
                print("User created successfully")
                user_info = User.objects.filter(id =user_create.id).first()
                user_info = UserSerializer(user_info)
                print(user_info.data)
                print(Post.objects.filter(user=user_create.id).first().title)
                # # print(user_info.data)
                data_json = user_info.data
                publish_data_on_redis(data_json, 'user.created')


log = logging.getLogger(__name__)
# @create_subscription(Post)
# def handle_create(instance):
#     log.debug('Created {}'.format(instance.name))
if __name__ == '__main__':
    Create_user().handle()

