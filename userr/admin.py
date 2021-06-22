# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import SearchLogo

# Register your models here.
from . models  import Register
from . models  import search
from . models  import contact

admin.site.register(Register)
admin.site.register(search)
admin.site.register(contact)
admin.site.register(SearchLogo)
