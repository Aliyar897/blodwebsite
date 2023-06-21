
from django.contrib import admin# Register your models here.

from .models import SignUp
from .models import WriteToUs

admin.site.register(SignUp)
admin.site.register(WriteToUs)