# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    gender_choice=[("male","Male"),
                   ("female","Female")]
    gender=models.CharField(max_length=6,choices=gender_choice,blank=False,null=False)
    date_of_birth=models.DateField(blank=False,null=False)
    bg_choice=[("B+","B+"),
               ("B-","B-"),
               ("A+","A+"),
               ("A-","A-"),
               ("O+","O+"),
               ("O-","O-"),
               ("AB+","AB+"),
               ("AB-","AB-")]
    blood_group=models.CharField(max_length=3,choices=bg_choice,blank=False,null=False)
    phone=models.CharField(max_length=13,blank=False,null=False)
    email=models.EmailField(max_length=100,blank=False,null=False)
    aadhar_no=models.CharField(max_length=12,blank=False,null=False,unique=True)
    area=models.CharField(max_length=100,blank=False,null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    pincode = models.IntegerField( blank=False, null=False)
    last_blood_donated_date=models.DateField(blank=True,null=True)
    disease_ans=[("yes","Yes"),
                ("no","No")]
    any_disease=models.CharField(max_length=3,choices=disease_ans,blank=False,null=False)
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        if not self.last_blood_donated_date:
            self.last_blood_donated_date=None
        super(Register, self).save(*args,**kwargs)

class search(models.Model):
    candidate_name=models.CharField(max_length=100,blank=False,null=False)
    bg_choice = [("B+", "B+"),
                 ("B-", "B-"),
                 ("A+", "A+"),
                 ("A-", "A-"),
                 ("O+", "O+"),
                 ("O-", "O-"),
                 ("AB+", "AB+"),
                 ("AB-", "AB-")]
    required_blood_group = models.CharField(max_length=3, choices=bg_choice, blank=False, null=False)
    purpose=models.CharField(max_length=100,blank=False,null=False)
    pincode=models.IntegerField(blank=False,null=False)





class contact(models.Model):
        name=models.CharField(max_length=100,null=False,blank=False)
        email_id = models.EmailField(max_length=100, blank=False, null=False)
        message=models.TextField(max_length=100,null=False,blank=False)

