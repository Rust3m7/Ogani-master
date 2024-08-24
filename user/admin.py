from django.contrib import admin
from user.models import MyUser

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
      list_display = ("username", "email", "phone", "address")
      search_fields = ("username", "email", "phone", "address")
      
