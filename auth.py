import time

import jwt
from django.conf.global_settings import SECRET_KEY
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions, status
import bcrypt
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User



class NormalAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            raise exceptions.AuthenticationFailed('User not found')
        check = check_password(password, user_obj.password)
        if check is False:
            raise exceptions.AuthenticationFailed('You are not incorect username or password')
        token = generate_jwt(user_obj)
        request.session['token'] = token
        request.session['user_id'] = user_obj.id
        userinfor = {"username": user_obj.username, "email": user_obj.email,'first_name': user_obj.first_name, 'last_name': user_obj.last_name}

        return (userinfor,token)
    def authenticate_header(self, request):
        pass


def generate_jwt(user):
    timestamp = int(time.time()) + 60 * 60 * 4
    jwtencode = jwt.encode(
        {"userid": user.pk, "username": user.username, "exp": timestamp},
        SECRET_KEY)
    return jwtencode