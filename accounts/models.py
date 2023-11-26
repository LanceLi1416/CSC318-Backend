from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(models.Manager):
    def create(self, **kwargs):
        user = self.model(**kwargs)
        user.save()
        return user

    def create_superuser(self, **kwargs):
        user = self.model(**kwargs)
        # user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractUser):
    email = models.EmailField(unique=True,
                              null=False)
    nickname = models.CharField(max_length=50,
                                null=False,
                                default='')
    profile_picture = models.ImageField(upload_to='profile_pics/',
                                        default='default_profile_picture.png',
                                        blank=True)
    bio = models.TextField(default='This user is too lazy to add anything here.',
                           blank=True)
    following = models.ManyToManyField('self',
                                       symmetrical=False,
                                       related_name='followers',
                                       blank=True)

    def save(self, *args, **kwargs):
        if not self.nickname:
            self.nickname = f'User#{self.id}'
        super(User, self).save(*args, **kwargs)
