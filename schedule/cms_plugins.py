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
        
        start_time = datetime.now()
        if instance.show_today == True:
            start_time = start_time.replace(hour=0, minute=0, second=0)
        else:
            start_time = start_time -timedelta(hours=1)
            
        if instance.instances == 0:
            # show all
            events = instance.calendar_plug.occurrences_after(start_time)
        else:
            events=list()
            loops = instance.instances
            for object in instance.calendar_plug.occurrences_after(start_time):
                loops = loops -1
                events.append(object)  
                if loops == 0:
                    break

        context.update({
            'events':events,
            'object':instance,
            'placeholder': placeholder,
            'instances': instance.instances
        })
        return context

plugin_pool.register_plugin(CMSCalendarEvents)