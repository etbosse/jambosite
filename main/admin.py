from django.contrib import admin
from .models import Event
from .models import Activity
from .models import Trail
from .models import LimActivity
from .models import Vehicle
from .models import VehicleReg
from django.db import models
import json
from tinymce.widgets import TinyMCE


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    # fields = ["eventName",
    #          "eventPublished",
    #          "eventDescription"]
    fieldsets = [
        ("Event/Published", {"fields": ["eventName", "eventPublished"]}),
        ("Description", {"fields": ["eventDescription"]}),
        ("EventID", {"fields": ["eventId"]}),
    ]


#class ActivityAdmin(admin.ActivityAdmin):
#    fields = ["activityId",
#              "activityStart",
#              "activityEnd",
#              "activityVolunteerId",
#              "eventId"]


admin.site.register(Event, EventAdmin)
admin.site.register(Activity)
admin.site.register(Trail)
admin.site.register(LimActivity)
admin.site.register(Vehicle)
admin.site.register(VehicleReg)