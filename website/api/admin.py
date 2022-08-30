from django.contrib import admin

from .models import Question, PhoneRequest, Application, Comment, Picture

admin.site.register(Application)
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(PhoneRequest)
admin.site.register(Picture)


