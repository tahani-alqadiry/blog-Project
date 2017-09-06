from django.shortcuts import render,get_object_or_404
from django.views import View
from user_profile.models import User
from .models import Post, Category,Comment


#show contents of index.html
class Index(View):
    def get(self, request):
        params = {}
        posts = Post.objects.all().order_by('-release_date')
        # post = Post.objects.get(content=)
        # Post.objects.order_by('-release_date').filter(author=user)[:3]
        users = User.objects.all()
        categories = Category.objects.all()
        params['posts'] = posts
        params['users'] = users
        params['categories'] = categories
        count = Post.objects.count()
        params['count'] = count
        # s_count = Post.objects.filter(category=1).count()
        # f_count = Post.objects.filter(category=2).count()
        # params['s_count'] = s_count
        # params['f_count'] = f_count
        return render(request, 'index.html', params)




# shows all posts in posts.html
class AllPosts(View):
    def get(self, request):
        params = {}
        posts = Post.objects.all().order_by('-release_date')
        params['posts'] = posts
        return render(request, 'posts.html', params)



# the category details of post
class Detail(View):
    def get(self,request, Category_id):
        category = get_object_or_404(Category, id=Category_id)
        return render(request, 'categ_detail.html', {'category': category})


#show all categories
class All_category(View):
    def get(self,request):
        category = Category.objects.all()
        cont = {'category':category}
        return render(request, 'categories.html', cont)


#create post by url
class Create_post(View):
    def get(self,request,post_name):
        try:
            obj = Post.objects.get(title=post_name)
            content = {'post': obj}
            content['msg1'] = "The post title exists try another one"
            return render(request, 'create.html', content)
        except Post.DoesNotExist:
            c = Category.objects.get(title='news')
            user = User.objects.get(username='tahani')
            obj = Post(content="this is created by user tahani", category=c, title=post_name, author=user, is_active=True)
            obj.save()
            content = {'post': obj}
            content['msg'] = "The post is created"
            return render(request, 'create.html', content)

#delete post by url
class Delete_post(View):
    def get(self, request, post_name):
        try:
            content = {}
            obj = Post.objects.get(title=post_name).delete()
            content['msg'] = "The post is deleted"
            return render(request, 'delete.html', content)
        except Post.DoesNotExist:
            content = {}
            content['msg'] = "post doesn't exist"
            return render(request, 'delete.html', content)

#show all post comments
class All_comments(View):
    def get(self,request,post_id):
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(user_post = post_id)
        params = {}
        params['comments'] = comments
        params['post'] = post
        return render(request, 'user_post.html', params)





