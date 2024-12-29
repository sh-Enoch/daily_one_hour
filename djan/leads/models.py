from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    

# Create your models here.
class Lead(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}."


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.email


#def a signal to create a user profile whenever a user is created

def post_user_created(sender, instance, created, **kwargs):
    """This event is triggered whenever a user is created

    Args:
        sender ([type]): [description]
        instance ([type]): [description]
        created ([type]): [description]
        **kwargs ([type]): [description]

    Returns:

    """
    print(instance, created)

    if created:
        UserProfile.objects.create(user=instance)


#post_save listens for the User model and when a user is created, it calls the post_user_created function
post_save.connect(post_user_created, sender=User)