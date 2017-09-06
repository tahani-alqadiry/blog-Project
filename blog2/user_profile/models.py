from django.db import models
from django.contrib.auth.models import AbstractBaseUser



class User(AbstractBaseUser):
    """
    This model made to store all user information

    """
    username = models.CharField('username', max_length=10, unique=True, db_index=True)
    email = models.EmailField('email address', unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    user_image = models.CharField(default='https://www.mediafire.com/convkey/9870/99zv8tz2ai0jndl6g.jpg?size_id=5',
                     max_length=1000, editable=True)
    birth_date = models.DateField()
    bio = models.CharField(default='this user has no bio',max_length=1000, editable=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username



