from django.contrib import admin
from .models import Events,eType, eStatus


# Register your models here.
admin.site.register(Events)
admin.site.register(eType)
admin.site.register(eStatus)
