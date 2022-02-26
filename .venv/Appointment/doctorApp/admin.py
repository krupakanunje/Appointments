from django.contrib import admin
from doctorApp.models import pd_doc,family_doc,p_name,f_name
# Register your models here.
admin.site.register(family_doc)
admin.site.register(pd_doc)
admin.site.register(p_name)
admin.site.register(f_name)