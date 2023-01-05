from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from pub import views
from pub.login_views import CustomTokenObtainPairView

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("create_post/", views.create_posts, name="create_post"),
    path('subscribe/', views.create_subs, name='subscribe'),
    # path('unsubscribe/<int:pk>/', views.unsubscribe_post, name='unsubscribe'),
    path("create_condition/", views.create_conditions, name="create_conditions"),
]