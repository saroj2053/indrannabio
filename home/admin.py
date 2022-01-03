from django.contrib import admin
from home.models import Contact
from home.models import Feedback
from home.models import Booking

# Register your models here.

admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Booking)
