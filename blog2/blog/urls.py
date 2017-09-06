
from django.conf.urls import url, include
from django.contrib import admin
from post.views import Index
from user_profile.views import Profile,Users

# from post import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #/index page
    url(r'^$',Index.as_view(), name="home"),

    #posts/
    url(r'^posts/', include('post.urls')),

    #show all users
    #users/
    url(r'^users/',include('user_profile.urls')),



]
