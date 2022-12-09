from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField
# Create your models here.
  
class User(AbstractUser):
    is_customer=models.BooleanField('is customer', default=False )
    is_mistri=models.BooleanField('is mistri', default=False)


mistri_catagory=(
    ('electic','electic'),
    ('tv','tv'),
    ('mobail','mobail'),
    ('microwave','microwave'),
    ('carmechaig','carmechaig'),
    ('freezer','frezzer'),
    ('computer','computer'),
    ('printer','printer'),
    ('plumber','plumber'),
    ('color-prainter','color-prainter'),
    ('rajmisrti','rajmisrti'),
    ('katmistri','katmistri'),
    
)


address=(
    ('alokbali','alokbali'),
    ('hajipur','hajipur'),
    ('karimpur','karipur'),
    ('chinispur','chinispur'),
    ('brammondi','brammondi'),
    ('beparipara','beparipara'),
 
    
)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    bio= models.CharField( max_length=150,)
    skill= models.CharField(choices=mistri_catagory, max_length=50)
    add_more_skill=MultiSelectField(choices=mistri_catagory, max_length=120,blank=True,null=True)
    phone=models.CharField(max_length=15,)
    email=models.EmailField()
    address=models.CharField(choices=address, max_length=120,)
    description=models.CharField( max_length=550,)
    profile_pic=models.ImageField(upload_to='media/mistriprofilepic',default='default.jpg')
    aggre=models.BooleanField(default=False)

    # def __str__(self):
    #      return self.name
    

@receiver(post_save,sender=User)
def create_profile(sender,instance ,created,**kwargs):
    if created:
         Profile.objects.create(user=instance)