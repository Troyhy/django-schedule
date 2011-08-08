from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin

from schedule.forms import RuleForm

from schedule.models import Calendar, Event, CalendarRelation, Rule

class CalendarAdminOptions(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']

class RuleAdmin(admin.ModelAdmin):
    form = RuleForm
    

    
class EventAdmin(PlaceholderAdmin):
    
    actions = ['copy_event']
    
    def copy_event(self, request, queryset):
        for event in queryset:
            new_event = Event()
            new_event.duplicate_from(event)
            new_event.save();
    
    copy_event.short_description = "Make copy of selected event"


admin.site.register(Calendar, CalendarAdminOptions)
admin.site.register(Rule, RuleAdmin)
#admin.site.register([Event, CalendarRelation])
admin.site.register(Event,EventAdmin)
admin.site.register(CalendarRelation)


