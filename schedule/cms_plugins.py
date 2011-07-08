from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import *
from django.utils.translation import ugettext as _

from django.utils.datetime_safe import datetime
from datetime import timedelta

class CMSCalendarEvents(CMSPluginBase):
    model =  CMSCalendarPlugin
    name = _("Schedule Events")
    render_template = "schedule/events.html"

    def render(self, context, instance, placeholder):
        context.update({
            'events':instance.calendar_plug.occurrences_after(datetime.now()-timedelta(hours=1)),
            'object':instance,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSCalendarEvents)