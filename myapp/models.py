from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class person(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    def __str__(self):
        return self.first_name
    
class FAQ(models.Model):
    ques=models.TextField()
    ans=models.TextField()
    def __str__(self):
        return self.ques   

class myreview(models.Model):
    title=models.CharField(max_length=1000)  
    message=models.TextField()
    def __str__(self):
        return self.title

class helpsupport(models.Model):
    title=models.CharField(max_length=1000)  
    message=models.TextField() 
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    first_name=models.CharField(max_length=30)  
    last_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    subject=models.CharField(max_length=40) 
    website=models.CharField(max_length=40)
    message=models.TextField()
    def __str__(self):
        return self.first_name
    
class user_register(models.Model):
       nm=models.CharField(max_length=40)
       em=models.EmailField()
       pw=models.CharField(max_length=40)
       birthday=models.CharField(max_length=20, blank=True, null=True)
       state=models.CharField(max_length=30, blank=True, null=True)
       country=models.CharField(max_length=30, blank=True, null=True)
       pincode=models.CharField(max_length=30, blank=True, null=True)
       contact=models.CharField(max_length=30, blank=True, null=True)
       gender=models.CharField(max_length=30, blank=True, null=True)
       qualifications=models.CharField(max_length=1000, blank=True, null=True)
       address=models.CharField(max_length=1000, blank=True, null=True)
       hobbies=models.CharField(max_length=100, blank=True, null=True)
       image=models.ImageField(upload_to="data",blank=True, null=True) 
              
       def __str__(self):
           return self.nm

class visa_type(models.Model):
    name=models.CharField(max_length=100)
    image1=models.ImageField(upload_to="data",blank=True)
    image2=models.ImageField(upload_to="data",blank=True)
    about=models.TextField()
    doc=models.TextField()
    def __str__(self):
        return self.name
    
class country(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    image=models.ImageField(upload_to="data",blank=True) 
    def __str__(self):
        return self.name 
    
class con_visa_details(models.Model):
    visa_name=models.ForeignKey(visa_type, on_delete=models.CASCADE)
    country_name=models.ForeignKey(country, on_delete=models.CASCADE)
    image1=models.ImageField(upload_to="data",blank=True) 
    image2=models.ImageField(upload_to="data",blank=True) 
    headings=models.CharField(max_length=200,primary_key=True)
    con_visa_des=RichTextField()   
    def __str__(self):
        return self.headings

class blogs(models.Model):
    title=models.CharField(max_length=500)
    image=models.ImageField(upload_to="data",blank=True)
    description=RichTextField()
    writer=models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
class coaching(models.Model):
    name=models.CharField(max_length=100)
    overview=models.CharField(max_length=1000)
    description=models.TextField()
    image=models.ImageField(upload_to="data",blank=True)
    duration=models.CharField(max_length=500)
    cost=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class eligible(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    status=models.CharField(max_length=100)
    ocuupation=models.CharField(max_length=100)
    cont=models.CharField(max_length=100)
    visa=models.CharField(max_length=100)
    def __str__(self):
        return self.fname    





