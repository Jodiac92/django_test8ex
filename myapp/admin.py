from django.contrib import admin
from myapp.models import Buser

# Register your models here.
class BuserAdmin(admin.ModelAdmin):
    list_display = ('buser_no','buser_name','buser_loc','buser_tel')
    
admin.site.register(Buser, BuserAdmin)