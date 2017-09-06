from django.db import models
from user_profile.models import User


class Category(models.Model):
    """
        This model made to store all category information

    """
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    """
        This model made to store all post information

    """
    content = models.TextField(max_length=5000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    release_date = models.DateTimeField(auto_now_add=True)
    image = models.CharField(default='https://www.mediafire.com/convkey/82cc/5pherhmaeju7un56g.jpg?size_id=5',
                             max_length=1000,editable=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
        This model made to store all user comments on his post or others posts
        with some comment info

    """
    user_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE )
    content = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content



