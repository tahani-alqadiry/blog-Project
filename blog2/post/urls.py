
from django.conf.urls import url
from post.views import Detail,AllPosts,Create_post,Delete_post,All_category,All_comments



urlpatterns = [

    #show all posts within a category
    #عرض المنشورات الخاصة بتصنيف معين
    #posts/category/category_id
    url(r'^category/(?P<Category_id>[0-9]+)/$', Detail.as_view(), name="detail"),

    #view all published posts
    #posts/
    url(r'^$', AllPosts.as_view()),

    #create post
    #posts/create/post_name
    url(r'^create/(\w+)/$',Create_post.as_view()),

    #delete post
    #posts/delete/post_name
    url(r'^delete/(\w+)/$',Delete_post.as_view()),


    #show all categories
    #posts/category/
    url(r'^category/$', All_category.as_view(), name='go_to_categories'),

    #show post comments
    #/post/<post_id>/comments
    url(r'^(?P<post_id>[0-9]+)/comments/$', All_comments.as_view(),name="go_to_post")








]
