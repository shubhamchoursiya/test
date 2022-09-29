from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
import time
# Create your models here.


class Ipdetail(models.Model):
	user_name = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
	ipname = models.CharField(max_length=100,null=False,blank=False)

	def __str__(self):
		return self.ipname


class Employee(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=100,null=False,blank=False,unique=True)
    emp_name = models.CharField(max_length=100,null=False,blank=False)
    designation = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(max_length=50,null=False,blank=False,unique=True)
    phone = PhoneNumberField(blank=True,null=True)
    department=models.CharField(max_length=100,null=False)
    salary=models.DecimalField(max_digits=15,decimal_places=10,null=True)
    MALE = 'MA'
    FEMALE = 'FE'
    GENDERS_IN_PROJECT = (
    (MALE, 'male'),
    (FEMALE, 'female'),
    )
    gender = models.CharField(max_length=2,choices=GENDERS_IN_PROJECT,default=MALE)


class EmployeeFace(models.Model):
    emp_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='securite/',blank=True)
    res1 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res2 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res3 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res4 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res5 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res6 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res7 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res8 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res9 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res10 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res12 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res13 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res14 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res15 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res16 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res17 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res18 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res19 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res20 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res21 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res22 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res23 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res24 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res25 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res26 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res27 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res27 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res28 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res29 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res30 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res31 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res32 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res33 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res34 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res35 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res36 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res37 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res38 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res39 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res40 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res41 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res42 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res43 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res44 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res45 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res46 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res47 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res48 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res49 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res50 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res51 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res52 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res53 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res54 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res55 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res56 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res57 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res58 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res59 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res60 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res61 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res62 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res63 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res64 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res65 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res66 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res67 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res68 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res69 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res70 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res71 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res72 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res73 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res74 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res75 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res76 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res77 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res78 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res79 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res80 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res81 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res82 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res83 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res84 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res85 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res86 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res87 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res88 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res89 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res90 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res91 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res92 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res93 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res94 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res95 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res96 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res97 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res98 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res99 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res100 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res101 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res102 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res103 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res104 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res105 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res106 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res107 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res108 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res109 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res110 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res111 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res112 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res113 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res114 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res115 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res116 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res117 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res118 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res119 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res120 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res121 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res122 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res123 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res124 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res125 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res126 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res127 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)
    res128 = models.DecimalField(max_digits=15, decimal_places=10, null=True,blank=True)

    def __str__(self):
        return self.emp_id.emp_id

class Notification(models.Model):
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    Category = models.CharField(max_length=64)
    CameraName = models.CharField(max_length=64)
    ImageURL = models.CharField(max_length=64)
    Stream = models.CharField(max_length=128)
    Time = models.DateTimeField(auto_now_add=True)
    res1 = models.CharField(max_length=100,default=0)
    res2 = models.IntegerField(default=0)

    def __str__(self):
        return self.Category


class Subscriber(models.Model):
	SubscriberID = models.CharField(max_length=500,unique=True)
	user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)
	ReservedField = models.CharField(max_length=500,default=0)

	def __str__(self):
		return self.SubscriberID



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=30)
	MALE = 'MA'
	FEMALE = 'FE'
	GENDERS_IN_PROJECT = (
	(MALE, 'male'),
	(FEMALE, 'female'),
	)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	gender = models.CharField(max_length=2,choices=GENDERS_IN_PROJECT,default=MALE)
	phone = models.CharField(max_length=30, blank=True)
	email = models.EmailField(max_length=50,blank=True)
	image = models.ImageField(upload_to='userpics/',blank=True)


	def __str__(self):
		return self.fullname

	def get_absolute_url(self):
		return reverse('securite:profiledetail',kwargs={'pk':self.pk})

class Camera(models.Model):
	ip = models.CharField(max_length=500,null=False,blank=False,unique=True)
	name = models.CharField(max_length=500,null=False,blank=False)
	user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
	stream = models.CharField(max_length=500,default=0)
	#option = models.CharField(max_length=20)
	#auth_uname = models.CharField(max_length=200)
	#uth_pwd = models.CharField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	created_at = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.name
