from django.http import response
from django.test import TestCase
from rest_framework.test import APITestCase, URLPatternsTestCase
from .serializers import EventSerializer
from rest_framework import status
from django.urls import path, include, reverse

# Create your tests here.

class EventSerializerTest(APITestCase):


    def setUp(self):
        self.test_event = EventSerializer()
        self.create_url = reverse('create-event')
        

    

    
    def test_create_event(self):
        """
        Ensure we can create a new event object
        """
        #url = reverse('create-event')
        data = {
            'event_title' : 'weekend_get_away',
            'start_date' : '24/01/20',
            'end_date' : '26/02/21',
            'start_time' : '09:06',
            'end_time' : '10:04',
            'time_zone' : 'UTC', 
            'description' : 'example', 
            'all_day' : '..' , 
            'event_tag' : 'yes',
            'event_colour' : 'green'
     }
        #response = self.client.post(url, data, format='json')

        response = self.client.post(self.create_url, data, format='json')
        # self.assertEqual(EventSerializer())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['event_title'], data['event_title'])
        self.assertEqual(response.data['start_date'], data['start_date'])
        self.assertEqual(response.data['end_date'], data['end_date'])
        self.assertEqual(response.data['start_time'], data['start_time'])
        self.assertEqual(response.data['end_time'], data['end_time'])
        self.assertEqual(response.data['time_zone'], data['time_zone'])
        self.assertEqual(response.data['description'], data['description'])
        self.assertEqual(response.data['all_day'], data['all_day'])
        self.assertEqual(response.data['event_tag'], data['event_tag'])
        self.assertEqual(response.data['event_colour'], data['event_colour'])
    

    
#     def test_create_no_event_title(self):
#         """
#         Ensure we can create a new event title
#         """
#         url = reverse('create-event')

#         data = {

#         'event_title' : '', 
#         'start_date' : '24/01/20',
#         'end_date' : '26/02/21',
#         'start_time' : '09:06',
#         'end_time' : '10:04',
#         'time_zone' : 'UTC', 
#         'description' : 'foobar@example.com', 
#         'all_day' : '..' , 
#         'event_tag' : 'foo',
#         'event_colour' : 'green', 

#      }
#         response = self.client.post(self.create_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         # self.assertEqual(EventSerializer(), 1)
#         self.assertEqual(len(response.data['event_title']), 1)



       
        


# # class EventSerializerTest(APITestCase, URLPatternsTestCase):
# #     urlpatterns = [
# #         path('api/', include('calendar_data_logic.urls'))
# #     ]

# #     def test_create_event(self):
# #         """
# #         Ensure we can create a new event title
# #         """
# #         url = reverse('create-event')
# #         response = self.client.get(url, format='json')
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(len(response.data), 10)
        
    



# # Create your tests here.
