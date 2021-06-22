# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import random

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    gender_choice=[("male","Male"),
                   ("female","Female")]
    gender=models.CharField(max_length=6,choices=gender_choice,blank=False,null=False)
    date_of_birth=models.DateField(blank=False,null=False)
    bg_choice=[("b+","B+"),
               ("b-","B-"),
               ("a+","A+"),
               ("a-","A-"),
               ("o+","O+"),
               ("o-","O-"),
               ("ab+","AB+"),
               ("ab-","AB-")]
    blood_group=models.CharField(max_length=3,choices=bg_choice,blank=False,null=False)
    phone=models.CharField(max_length=13,blank=False,null=False)
    email=models.EmailField(max_length=100,blank=False,null=False)
    area=models.CharField(max_length=100,blank=False,null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    pincode = models.IntegerField( blank=False, null=False)
    disease_ans=[("yes","Yes"),
                ("no","No")]
    any_disease=models.CharField(max_length=3,choices=disease_ans,blank=False,null=False)
    def __str__(self):
        return self.name

class search(models.Model):
    candidate_name=models.CharField(max_length=100,blank=False,null=False)
    bg_choice = [("b+", "B+"),
                 ("b-", "B-"),
                 ("a+", "A+"),
                 ("a-", "A-"),
                 ("o+", "O+"),
                 ("o-", "O-"),
                 ("ab+", "AB+"),
                 ("ab-", "AB-")]
    required_blood_group = models.CharField(max_length=3, choices=bg_choice, blank=False, null=False)
    purpose=models.CharField(max_length=100,blank=False,null=False)
    pincode=models.IntegerField(blank=False,null=False)



class SearchLogo(models.Model):
    title = models.CharField(blank=True, null=True, max_length=10)
    logo_number = models.IntegerField(blank=True, null=True)
    logo_image = models.ImageField(upload_to='logo')


    def __str__(self):
        return self.title

class contact(models.Model):
        name=models.CharField(max_length=100,null=False,blank=False)
        email_id = models.EmailField(max_length=100, blank=False, null=False)
        message=models.TextField(max_length=100,null=False,blank=False)

