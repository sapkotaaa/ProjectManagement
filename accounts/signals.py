from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from .models import User,Profile


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        
        Profile.objects.create(user = instance)
        print(instance)
        print('profile created')
        

        

@receiver(post_save,sender=User)
def udpate_profile(sender,instance,created,**kwargs):
    if created == False:
        instance.profile.save()
        print('Profile Saved')