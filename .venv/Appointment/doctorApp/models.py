from django.db import models
#import datetime
# Create your models here.
class family_doc(models.Model):
    dc_name=models.TextField(max_length=30,default="Dr. Nene")
    aval_timing= models.DateTimeField(null=True)
    class Meta:  
        db_table = "family_doc"  
class f_name(models.Model):
    fname=models.TextField(max_length=30,default="Dr. Nene")
   
    class Meta:  
        db_table = "fnames"  
class p_name(models.Model):
    fname=models.TextField(max_length=30,default="Dr. Nene")
   
    class Meta:  
        db_table = "pnames"  
        
class pd_doc(models.Model):
    dc_name=models.TextField(max_length=30,default="Dr.Rao")
    aval_timing= models.DateTimeField(null=True)
    class Meta:  
        db_table = "pd_doc"  
class Contact(models.Model):
    name= models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=11)
    desc=models.TextField()
    dates=models.DateField()
    class Meta:  
        db_table = "contact" 

class booking(models.Model):
   dc=models.TextField(max_length=30,default="Rao")
   aval_timing= models.DateTimeField(null=True)
   Patient_name= models.TextField(max_length=30,default="R")
   contact_no = models.IntegerField(default=101)
    
   class Meta:  
        db_table = "booking" 
                