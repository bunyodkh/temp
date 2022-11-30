from django.contrib import admin

from .models import Consultant, Competence, Sphere, Language, Type

admin.site.register(Consultant)
admin.site.register(Sphere)
admin.site.register(Competence)
admin.site.register(Language)
admin.site.register(Type)
