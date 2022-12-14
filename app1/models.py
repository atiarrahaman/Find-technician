from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField
# Create your models here.
  
class User(AbstractUser):
    is_customer=models.BooleanField('আমি কাস্টমার', default=False )
    is_mistri=models.BooleanField('আমি মিস্ত্রী', default=False)
    is_tutor=models.BooleanField('আমি টিউটর', default=False)


mistri_catagory=(
    ('ইলেক্টিক','ইলেক্টিক'),
    ('টিভি','টিভি'),
    ('মোবাইল','মোবাইল'),
    ('কম্পিউটার','কম্পিউটার'),
    ('পিন্টার','পিন্টার'),
    ('কার মেকানিক','কার মেকানিক'),
    ('ফ্রিজ','ফ্রিজ'),
    ('এসি','এসি'),
    ('সিসিটিভি','সিসিটিভি'),
    ('প্লাম্বার','প্লাম্বার'),
    ('রং মিস্ত্রী','রং মিস্ত্রী'),
    ('কাঠ মিস্ত্রী','কাঠ মিস্ত্রী'),
    ('রাজ মিস্ত্রী','রাজ মিস্ত্রী'),
    ('ভিডিওগ্রাফার','ভিডিওগ্রাফার')
    
) 

address=(
    ('চিনিশপুর','চিনিশপুর'),
    ('দাসপাড়া','দাসপাড়া'),
    ('বেপারিপাড়া','বেপারিপাড়া'),
    ('হাজিপুর','হাজিপুর'),
    ('পুরানপাড়া','পুরানপাড়া'), 
    ('খালপাড়া','খালপাড়া'),
    ('মাধবদী','মাধবদী'), 
    ('সাহেপ্রতাব','সাহেপ্রতাব'), 
    ('আলোকবালী','আলোকবালী'),
    ('চরদিঘলদী','চরদিঘলদী'),
    ('করিমপুর','করিমপুর'),
    ('কাঠালিয়া','কাঠালিয়া'),
    ('নূরালাপুর','নূরালাপুর'),
    ('মেহেড়পাড়া','মেহেড়পাড়া'),
    ('পাইকারচর','পাইকারচর'), 
    ('পাঁচদোনা','পাঁচদোনা'),
    ('শিলমান্দী','শিলমান্দী'),
    ('রায়পুরা ','রায়পুরা'),
    ('পলাশ ','পলাশ'), 
    ('শিবপুর ','শিবপুর'), 
    ('বেলাব ','বেলাব'),
    ('মনোহরদি ','মনোহরদি'),
    
    
 
    
)

classchoice=(
    ('class 1','claas 1'),
    ('class 2','claas 2'),
    ('class 3','claas 3'),
    ('class 4','claas 4'),
    ('class 5','claas 5'),
    ('class 6','claas 6'),
    ('class 7','claas 7'),
    ('class 8','claas 8'),
    ('class 9','claas 9'),
    ('class 10','claas 10'),
    ('Inter First year','Inter First year'),
    ('Inter Second Year','Inter Second Year'),
)

subjects=(
    ('Bangla','Bangla'),
    ('English','English'),
    ('Math','Math'),
    ('Physics','Physics'),
    ('Chemistry','Chemistry'),
    ('Highermath','Highermath'),
    ('ICT','ICT'),
    ('Biology','Biology'),
    ('Financial Accounting','Financial Accounting'),
     
)
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    bio= models.CharField( max_length=150,)
    clases=models.CharField(choices=classchoice,max_length=25 )
    add_more_clases=MultiSelectField(choices=classchoice,max_length=25,blank=True,null=True)
    add_more_subject=MultiSelectField(choices=subjects,max_length=25,blank=True,null=True)
    subjects=models.CharField(choices=subjects,max_length=100,)
     
    skill= models.CharField(choices=mistri_catagory, max_length=50)
    add_more_skill=MultiSelectField(choices=mistri_catagory, max_length=120,blank=True,null=True)
    phone=models.CharField(max_length=15,)
    email=models.EmailField(blank=True,null=True)
    address=models.CharField(choices=address, max_length=120,)
    description=models.CharField( max_length=550,)
    profile_pic=models.ImageField(upload_to='media/mistriprofilepic',default='default.jpg')
    aggre=models.BooleanField(default=False)
    tutor=models.BooleanField(default=False)


    # def __str__(self):
    #      return self.name
    

@receiver(post_save,sender=User)
def create_profile(sender,instance ,created,**kwargs):
    if created:
         Profile.objects.create(user=instance)