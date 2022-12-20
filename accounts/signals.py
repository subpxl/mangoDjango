from .models import User,UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)    
def post_save_create_profile_reciever(sender,instance,created,**kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('user profile creaed')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            profile = UserProfile.objects.create(user =instance)
            print('user profile was not existed but i created it now ') 
        print('uer is updated') 
