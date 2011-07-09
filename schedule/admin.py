from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin

from schedule.forms import RuleForm

from schedule.models import Calendar, Event, CalendarRelation, Rule

class CalendarAdminOptions(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']

class RuleAdmin(admin.ModelAdmin):
    form = RuleForm

admin.site.register(Calendar, CalendarAdminOptions)
admin.site.register(Rule, RuleAdmin)
#admin.site.register([Event, CalendarRelation])
admin.site.register(Event,PlaceholderAdmin)
admin.site.register(CalendarRelation)

