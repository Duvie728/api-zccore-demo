from types import DynamicClassAttribute
from django.utils import timezone as _timezone
from core.utils import get_timezones, DEFAULT_TIMEZONE
from colorfield.fields import ColorField
from rest_framework import serializers




class EventSerializer(serializers.Serializer):


    # EVENT_COLOR_CHOICES = [

    #     ("#FFFFFF", "white"),
    #     ("#fafafa", "neutral"),
    #     ("#8b0000", "red"),
    #     ("#ffff00", "yellow"),
    #     ("#006400","green")
    #  ]

    _id = serializers.ReadOnlyField()
    event_title = serializers.CharField(required=True)
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)
    start_time = serializers.TimeField(required=True)
    end_time = serializers.TimeField(required=True)
    time_zone = serializers.ChoiceField(choices=get_timezones(), default=DEFAULT_TIMEZONE)
    description = serializers.CharField(max_length=250, required=True)
    all_day = serializers.BooleanField(required=True)
    event_tag = serializers.CharField(required=True)
    event_colour = serializers.CharField(required=True)


    # def get_event_color(self, obj):
    #     return obj.event.color

    