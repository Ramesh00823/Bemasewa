from django.contrib import admin
from .models import Service, Application,LifeInsuranceApplication,PanCardApplication


admin.site.register(Service)
admin.site.register(Application)
admin.site.register(LifeInsuranceApplication)
admin.site.register(PanCardApplication)



# Register your models here.
