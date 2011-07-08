from django.db import models
from cms.models import CMSPlugin

from schedule.models.calendars import *
from schedule.models.events import *
from schedule.models.rules import *

class CMSCalendarPlugin(CMSPlugin):
    calendar_plug = models.ForeignKey(Calendar, verbose_name="Select calendar")
    instances = models.IntegerField(verbose_name="show how many?")
    show_today = models.BooleanField(verbose_name="show all from today?")
    
    

from schedule.signals import *
