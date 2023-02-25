from django.contrib import admin

# Register your models here.
from .models import Students
from .models import Users, Infor_school


#from .models import Get_images

admin.site.register(Students)
admin.site.register(Users)
admin.site.register(Infor_school)