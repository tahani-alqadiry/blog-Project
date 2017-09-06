
from django.conf.urls import url
from user_profile.views import Profile,Users




urlpatterns = [
    #بروفايل المستخدم
    #/user/username
    url(r'^users/(\w+)/$', Profile.as_view(), name="profile_detail"),

    #show all users
    #users/
    url(r'^$',Users.as_view(),name="go_to_users"),



]
