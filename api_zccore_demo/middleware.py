import pytz

from django.utils import timezone


class TimezoneMiddleware(object):
    """
    Middleware class that allows us to set the current timezone
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):

        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()



# class TimezoneMiddleware(object):
#     def process_request(self, request):
#         timezone.activate(pytz.timezone(tzname))