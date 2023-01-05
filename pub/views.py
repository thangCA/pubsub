import json

from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from Enum_condition import Condition_enums, next_step_enums
from Subscription import subscribe
from pub.Redis import publish_data_on_redis, Response_User_Infor
from pub.models import Post, Conditions, log

# Create your views here.

"""
    Create User
        + Request:
            {
                "username": "admin",
                "password": "admin",
                "email": ""
            }
        + send to redis:
        + Response: User Infor when sub create user
"""
class create_user(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        query = User.objects.filter(username=request.data['username']).first()
        if query is not None:
            return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        json_data = {
            'username': request.data['username'],
            'password': request.data['password'],
            'email': request.data['email'],
        }
        publish_data_on_redis(json_data, 'user.new')
        message = Response_User_Infor.handle(self)
        if message is not None:
            return Response(message, status=status.HTTP_201_CREATED)
register_user = create_user.as_view()


class create_post(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            title = request.data['title']
            description = request.data['description']
            user = self.request.user
            Post.objects.create(title=title, description=description, user=user)
            return Response({"message": "Create post successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "You are not logged in"}, status=status.HTTP_400_BAD_REQUEST)
create_posts = create_post.as_view()
# @login_required
class create_sub(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            user = self.request.user
            check = subscribe(user, request.data['id'])
            if check:
                return Response({"message": "Subscribe successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Subscribe failed"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "You are not logged in"}, status=status.HTTP_400_BAD_REQUEST)
create_subs = create_sub.as_view()

class create_condition(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            user = self.request.user
            post = Post.objects.filter(id=request.data['id']).first()
            data = request.data['data']
            logs = []
            for i in data:
                field = i['field']
                value = i['value']
                condition = Condition_enums(i['condition']).name if i['condition'] else None
                if condition is None:
                    return Response({"message": "Condition is not valid"}, status=status.HTTP_400_BAD_REQUEST)
                next_condition = next_step_enums(i['next_condition']) if i['next_condition'] else None
                Conditions.objects.create(feild=field, value_change=value, condition=condition, next_condition=next_condition)
                logs.append({
                    'field': field,
                    'value': value,
                    'condition': condition,
                    'next_condition': next_condition
                })
            before = {
                'user': post.user.username,
                'log':  log.objects.filter(id_post=post).first().log if log.objects.filter(id_post=post).first() else None,
                'post': post.id
            }
            after = {
                'user': user,
                'log': logs,
                'post': post.id
            }
            log_create = log.objects.create(id_user=user, id_post=post, before=json.dumps(before), after=json.dumps(after),check_change=True)
            log_create.save()
            return Response({"message": "Create condition successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "You are not logged in"}, status=status.HTTP_400_BAD_REQUEST)
create_conditions = create_condition.as_view()













