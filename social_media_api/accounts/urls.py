from django.urls import path
from .views import UserFeedView
from .views import register_user, login_user, user_profile
from rest_framework.authtoken.views import obtain_auth_token
from .views import FollowUserView, UnfollowUserView, FollowersListView, FollowingListView


urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('profile/', user_profile, name='profile'),  # New profile route
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Built-in DRF token login
     path('feed/', UserFeedView.as_view(), name='user-feed'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('followers/<int:user_id>/', FollowersListView.as_view(), name='user-followers'),
    path('following/<int:user_id>/', FollowingListView.as_view(), name='user-following'),
]
