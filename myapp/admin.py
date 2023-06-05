from django.contrib import admin
from .models import Home, Doctor, Contact
# Register your models here.
admin.site.register(Home)

admin.site.register(Contact)

class DoctorAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all":("css/main.css",)
        }
        js = ("js/app.js",)
    
admin.site.register(Doctor, DoctorAdmin)